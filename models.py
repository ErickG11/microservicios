from abc import ABC, abstractmethod

class UserServiceInterface(ABC):
    @abstractmethod
    def create_user(self, name: str, email: str) -> int:
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> dict:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        pass
