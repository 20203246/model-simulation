import torch
import torch.nn as nn
r"""
nn.Conv2d(
    in_channels=,
    out_channels=,
    kernel_size=,
    stride=,
    padding=,
    dilation=, # 膨胀系数
    groups=, # 依据通道数设置的分离卷积数
    bias=,
    padding_mode=,
    device=,
)
"""

# 深度的定义以及训练参数比较
linear = nn.Linear(in_features=3*28*28,out_features=3*28*28)
linear_params = sum(p.numel() for p in linear.parameters() if p.requires_grad)

conv = nn.Conv2d(in_channels=3,out_channels=3,kernel_size=3)
params = sum(p.numel() for p in conv.parameters() if p.requires_grad)

depth_conv = nn.Conv2d(in_channels=3,out_channels=3,kernel_size=3,groups=3)
point_conv = nn.Conv2d(in_channels=3,out_channels=3,kernel_size=1)
depthwise_separable = nn.Sequential(depth_conv,point_conv)
params_depthwise = sum(p.numel() for p in depthwise_separable.parameters() if p.requires_grad)

print(f'多层感知机使用的参数{linear_params} parameters.')
print(f'普通卷积使用的参数{params} parameters.')
print(f'深度可分离卷积使用的参数{params_depthwise} parameters.')
r"""
多层感知机使用的参数5534256 parameters.
普通卷积使用的参数84 parameters.
深度可分离卷积使用的参数42 parameters.
"""