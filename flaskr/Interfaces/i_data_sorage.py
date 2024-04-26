from abc import ABC, abstractmethod

class IdStorage(ABC):

    @abstractmethod
    def get_data(self, data) -> list[any]:
        pass
    
    @abstractmethod
    def post_data(self, data):
        pass

    @abstractmethod
    def update_data(self, data):
        pass

    @abstractmethod
    def delete_data(self, data):
        pass
