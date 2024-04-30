"""
This module contains the class for handling FizzBuzz operations in the Flaskr application.
"""

from typing import Any
from .Interfaces.i_problem_solver import IProblemSolver

class FizzBuzz(IProblemSolver):
    """
    Class for handle IProblemSolver and fizzBuzz
    """

    def __init__(self) -> None:
        pass

    def compute_one_result(self, data: Any) -> Any:

        return self.__fizz_buzz(int(data))

    def __fizz_buzz(self,number: int) -> str:
        result = str(number)
        fizz_flag = False

        if number % 3 == 0:
            result = "Fizz"
            fizz_flag = True

        if number % 5 == 0:
            if fizz_flag:
                result += "Buzz"
                return result
            result = "Buzz"

        return result
