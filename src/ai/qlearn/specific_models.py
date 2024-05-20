import torch.nn as nn
import torch.nn.functional as func
from torch import Tensor

from ai.qlearn.model import ModelAdapter


class SampleModel(ModelAdapter):
    def __init__(self):
        self.__rows = 6
        self.__cols = 7
        super().__init__()

        self.fc1 = nn.Linear(self.__rows * self.__cols, 64)
        self.fc2 = nn.Linear(64, 128)
        self.fc3 = nn.Linear(128, 64)
        self.output = nn.Linear(64, 7)

    def forward(self, x: Tensor) -> Tensor:
        x = x.view(-1, self.__rows * self.__cols)
        x = func.relu(self.fc1(x))
        x = func.relu(self.fc2(x))
        x = func.relu(self.fc3(x))
        x = self.output(x)
        return func.softmax(x, dim=1)

    def run(self, x: Tensor) -> Tensor:
        return self.forward(x)


