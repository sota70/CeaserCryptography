from decrypter import Decrypter

class UpperTextDecrypter(Decrypter[str]):

    def __init__(self, shift_count: int):
        super().__init__(shift_count)
    
    def decrypt(self, input: str) -> str:
        ascii_code: int = ord(input)
        num: int = ascii_code - ord('A')
        num = (num - self._shift_count) % 26
        ascii_code = num + ord('A')
        return chr(ascii_code)
