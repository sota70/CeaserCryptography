from typing import Generic, TypeVar

T = TypeVar("T")

class Encrypter(Generic[T]):

    def __init__(self, shift_count: int):
        self._shift_count: int = shift_count
    
    def encrypt(self, input: T) -> T:
        raise NotImplementedError()