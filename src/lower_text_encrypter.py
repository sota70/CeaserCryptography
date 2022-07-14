from encrypter import Encrypter

class LowerTextEncrypter(Encrypter[str]):

    def __init__(self, shift_count: int):
        super().__init__(shift_count)

    def encrypt(self, input: str) -> str:
        ascii_code: int = ord(input)
        num: int = ascii_code - ord('a')
        num = (num + self._shift_count) % 26
        ascii_code = num + ord('a')
        return chr(ascii_code)
