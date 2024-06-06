"""
This module contains the interface IdStorage
"""
from abc import ABC, abstractmethod

class IdStorage(ABC):
    """
    IdStorage Interface, contains de the methods for any problem
    """

    @abstractmethod
    def get_active_data_by_number(self, data):
        """
        This method makes the logic of getting an active data with a number
        """

    @abstractmethod
    def get_data_by_number(self, data):
        """
        This method makes the logic of getting a data by the number
        """

    @abstractmethod
    def post_data(self, data):
        """
        This method makes the logic of posting a data
        """

    @abstractmethod
    def update_active_data(self, data):
        """
        This method actives a data
        """

    @abstractmethod
    def update_deactive_data(self, data):
        """
        This method deactivate a data
        """

    @abstractmethod
    def delete_hard_number(self, data):
        """
        This method deletes
        """

    @abstractmethod
    def get_number_by_range(self, min_value, max_value):
        """
        This method gets data by a int range
        """
