class CustomGradientCallback(Callback):
    def __init__(self, model_path=None):
        super(CustomGradientCallback, self).__init__()
        self.previous_gradients = defaultdict(lambda: None)
        self.model_path = model_path

    def on_epoch_begin(self):
        # 如果是第一个epoch并且提供了模型文件路径
        if self.epoch == 0 or self.model_path is not None:
            checkpoint = torch.load(self.model_path) #dict
            loaded_gradients = checkpoint['gradients']
	    self.model.load_state_dict(checkpoint['model_state_dict'])

            for name, grad in loaded_gradients.items():
                if grad is not None:
                    self.previous_gradients[name] = grad.clone().detach()
		else:
		    self.previous_gradients[name] = None

    def on_backward_end(self):
        # 在loss.backward()后执行
        for name, param in self.model.named_parameters():
            # 计算梯度，但不更新权重
            if param.grad is not None:
                current_gradient = param.grad.data.clone().detach()

                # 如果上一个epoch有该层的梯度
                if self.previous_gradients[name] is not None:
                    prev_gradient = self.previous_gradients[name]
                    dot_product = torch.dot(torch.mean(prev_gradient,dim=0),torch.mean(current_gradient,dim=0))
                    # 如果夹角大于90度（点乘小于0）
                    if dot_product < 0:
                        param.requires_grad = False

                # 存储当前梯度为"上一个梯度"，以供下一个epoch使用
                self.previous_gradients[name] = current_gradient
	  else:
		self.previous_gradients[name] = None
		param.requires_grad = False

    def on_epoch_end(self):
        # 保存模型及梯度
        torch.save({
            'model_state_dict': self.model.state_dict(),
            'gradients': {name: param.grad for name, param in self.model.named_parameters()}
        }, f"model_with_gradients_epoch_{self.epoch}.pth")

        # 如果你需要在下一个epoch解冻所有层，可以在此处添加：
        for param in self.model.parameters():
            param.requires_grad = True