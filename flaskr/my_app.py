from .db import DbStorage
from .fizz_buzz import FizzBuzz
from .Interfaces.i_data_sorage import IdStorage

class MyApp():
    def __init__(self) -> None:
        self.db:IdStorage = DbStorage()
        self.fizzBuzz = FizzBuzz()
    
        
    def get_active_number(self,number):

        sql_result = self.db.get_active_data_by_number(number)

        if sql_result is None:
            return "Not Found", 404

        return sql_result["result"], 200
    
    def post_number(self, num):
        data = {'number': num, 'result': self.fizzBuzz.compute_one_result(num)}

        sql_result_exits = self.db.get_data_by_number(num)

        if sql_result_exits is not None:
            
            if sql_result_exits['active'] == 0:
                self.db.update_active_data(num)
                return sql_result_exits['result'], 200
            
            else:
                return sql_result_exits['result'], 409
            
        else:
            self.db.post_data(data)
            return str(data.get('result')) , 201