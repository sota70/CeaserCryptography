from typing import Generic, TypeVar

T = TypeVar("T")

class Decrypter(Generic[T]):

    def __init__(self, shift_count: int):
        self._shift_count: int = shift_count
    
    def decrypt(self, input: T) -> T:
        raise NotImplementedError()
