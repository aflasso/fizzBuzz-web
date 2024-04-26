from .db import DbStorage
from .fizz_buzz import FizzBuzz
from .Interfaces.i_data_sorage import IdStorage

class MyApp():
    def __init__(self) -> None:
        self.db:IdStorage = DbStorage()
        self.fizzBuzz = FizzBuzz()
    
        
    def get_number(self,number):

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
            
    def delete_number(self, num):
        
        sql_result_exits = self.db.get_active_data_by_number(num)

        if sql_result_exits is not None:
            self.db.update_deactive_data(num)
            return "",204
        else:
            return "Not Found", 404
        
    def get_range(self,min_value,max_value):

        sql_result = self.db.get_number_by_range(min_value, max_value)

        if not sql_result:
            return "Not Found", 404
        
        print(sql_result)
        result = ""

        for row in sql_result:
            line = f"{row['request']} : {row['result']}\n"

            result = result + line
        
        return result, 200