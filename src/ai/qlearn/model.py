import torch.nn as nn
from torch import save as torch_save
from torch import load as torch_load
from torch import Tensor
from os import PathLike


class ModelAdapter(nn.Module):
    def __init__(self):
        super().__init__()

    def run(self, x: Tensor) -> Tensor:
        raise Exception("This is an abstract class!")



class ModelHandler():
    def __init__(self, model: nn.Module) -> None:
        super().__init__()
        self.__model: nn.Module = model

    def save(self, path: PathLike) -> None:
        torch_save(self.__model, path)

    def load(self, path: PathLike) -> None:
        self.__model = torch_load(path)


