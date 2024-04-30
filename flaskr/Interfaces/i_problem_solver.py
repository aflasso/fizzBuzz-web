"""
This module contains de interface IProblemSolver
"""
from abc import ABC, abstractmethod
from typing import Any


class IProblemSolver(ABC):
    """
    IProblmemSolver Interface, contains de the methods for any problem
    """
    @abstractmethod
    def compute_one_result(self, data:Any) -> Any:
        """
        Procces a data to make a result
        """
