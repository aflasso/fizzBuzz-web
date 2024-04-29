from typing import List
from .Interfaces.i_problem_solver import IProblemSolver

class FizzBuzz(IProblemSolver):
    
    def __init__(self) -> None:
        pass
    
    def compute_one_result(self, data: any) -> any:
       
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