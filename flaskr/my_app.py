"""
This module contains the main application logic.
"""

from .db import DbStorage
from .fizz_buzz import FizzBuzz
from .Interfaces.i_data_sorage import IdStorage

class MyApp():
    """
    This class models the application logic. Class controller
    """
    def __init__(self) -> None:
        self.db:IdStorage = DbStorage()
        self.fizz_buzz = FizzBuzz()


    def get_number(self,number):
        """
        This method makes the logic of getting by a number the 
        fizzBuzz of that number if the number its on yhe database
        """

        sql_result = self.db.get_active_data_by_number(number)

        if sql_result is None:
            return "Not Found", 404

        return sql_result["result"], 200

    def post_number(self, num):
        """
        This method post a number an its FizzBuzz value if its not on the database,
        if it is but its deactivate it actives it, 
        if its all ready active just returns the fizzBuzz value
        """
        data = {'number': num, 'result': self.fizz_buzz.compute_one_result(num)}

        sql_result_exits = self.db.get_data_by_number(num)

        if sql_result_exits is not None:

            if sql_result_exits['active'] == 0:
                self.db.update_active_data(num)
                return sql_result_exits['result'], 200

            return sql_result_exits['result'], 409

        self.db.post_data(data)
        return str(data.get('result')) , 201

    def delete_number(self, num):
        """
        This method deactivate de number of the databes if it exist,
        if not it returns Not Found
        """

        sql_result_exits = self.db.get_active_data_by_number(num)

        if sql_result_exits is not None:
            self.db.update_deactive_data(num)
            return "",204

        return "Not Found", 404

    def get_range(self,min_value,max_value):
        """
        This method returns the numbers and the fizzbuzz values, between to numbers
        """

        sql_result = self.db.get_number_by_range(min_value, max_value)

        if not sql_result:
            return "Not Found", 404

        print(sql_result)
        result = ""

        for row in sql_result:
            line = f"{row['request']} : {row['result']}\n"

            result = result + line

        return result, 200
