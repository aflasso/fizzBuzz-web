from abc import ABC, abstractmethod

class IdStorage(ABC):

    @abstractmethod
    def get_active_data_by_number(self, data) -> any:
        pass
    
    @abstractmethod
    def get_data_by_number(self, data) -> any:
        pass
    
    @abstractmethod
    def post_data(self, data):
        pass

    @abstractmethod
    def update_active_data(self, data):
        pass

    @abstractmethod
    def update_deactive_data(self, data):
        pass

    @abstractmethod
    def get_number_by_range(self, min_value, max_value):
        pass
