import torch
import torch.nn as nn
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28,312), nn.ReLU(),
            nn.Linear(312,256), nn.ReLU(),
            nn.Linear(256,10)
        )
    def forward(self, input):
        x = self.flatten(input)
        return self.linear_relu_stack(x)

if __name__ == '__main__':
    model = NeuralNetwork()
    print(model)
    # 获取参数个数
    sum = 0
    for i in model.parameters():
        print('该层结构：'+str(list(i.size())))
        acc = 1
        for j in i.size(): acc *= j
        print('该层参数和：'+str(acc))
        sum += acc
    print('总参数数量和：'+str(sum))

