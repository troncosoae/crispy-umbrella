from typing import Union
import math
import torch.nn as nn
import torch.optim as optim
from torch import Tensor, argmax as torch_argmax, \
        multinomial as torch_multinomial

from ai.qlearn.model import ModelAdapter


class Brain:
    def __init__(self, model: ModelAdapter) -> None:
        self.__model = model

    def run(self, x: Tensor) -> Tensor:
        return self.__model.run(x)

    def choose_best(self, run_result: Tensor) -> int:
        result: Union[int, float] = torch_argmax(run_result).item()
        assert math.isfinite(result)
        return int(result)
        

    def choose_by_dist(self, run_result: Tensor) -> int:
        result: Union[int, float] = torch_multinomial(run_result, 1).item()
        assert math.isfinite(result)
        return int(result)
        


