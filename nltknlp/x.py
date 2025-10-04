import torch
import numpy as np

a = torch.tensor(5)
print(a)
# LogBackward
# a.backward()

# torch.MulBackward

# pytorch梯度的计算过程: https://blog.csdn.net/qimo601/article/details/123849789
# 在pytorch中，只有浮点类型的数才有梯度
x = torch.tensor(3.)  # 数字
w = torch.tensor(4., requires_grad=True)  # 数字
b = torch.tensor(5., requires_grad=True)  # 数字
y = w * x + b
y.backward()
"""
x.requires_grad=True
dy/dx: tensor(4.)
dy/dw: tensor(3.)
dy/db: tensor(1.)
去的偏导数？
"""
print('dy/dx:', x.grad,x.grad_fn)
print('dy/dw:', w.grad,x.grad_fn)
print('dy/db:', b.grad,x.grad_fn)
"""
y.grad
<input>:1: UserWarning: The .grad attribute of a Tensor that is not a leaf Tensor is being accessed. Its .grad attribute won't be populated during autograd.backward(). If you indeed want the .grad field to be populated for a non-leaf Tensor, use .retain_grad() on the non-leaf Tensor. If you access the non-leaf Tensor by mistake, make sure you access the leaf Tensor instead. See github.com/pytorch/pytorch/pull/30531 for more informations. (Triggered internally at /Users/runner/work/pytorch/pytorch/pytorch/build/aten/src/ATen/core/TensorBody.h:491.)
"""
print('dy:', b.grad,y.grad_fn)

# Pytorch中的梯度问题汇总: https://blog.csdn.net/qq_37369201/article/details/106851919
# PyTorch中的9种常见梯度下降算法与案例: https://blog.csdn.net/AdamCY888/article/details/129793347
# pytorch常用代码梯度篇（梯度裁剪、梯度累积、冻结预训练层等）： https://jdgqr.blog.csdn.net/article/details/129765732
# https://pytorch-cn.readthedocs.io/zh/latest/

# UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
v = torch.tensor(torch.Tensor([0, 0, 0]), requires_grad=True)
# 注册至 _backward_hooks
h = v.register_hook(lambda grad: grad * 2)  # double the gradient
v.backward(torch.Tensor([1, 1, 1]))
# 先计算原始梯度，再进hook，获得一个新梯度。
print(v.grad.data)
