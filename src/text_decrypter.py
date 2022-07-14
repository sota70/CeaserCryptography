from decrypter import Decrypter
from lower_text_decrypter import LowerTextDecrypter
from upper_text_decrypter import UpperTextDecrypter

class TextDecrypter(Decrypter[str]):

    def __init__(self, shift_count: int):
        super().__init__(shift_count)
        self.__upper_text_decrypter: UpperTextDecrypter = UpperTextDecrypter(shift_count)
        self.__lower_text_decrypter: LowerTextDecrypter = LowerTextDecrypter(shift_count)
    
    def decrypt(self, input: str) -> str:
        decrypted_text: str = ""
        for character in input:
            if character.isupper():
                decrypted_text += self.__upper_text_decrypter.decrypt(character)
            elif character.islower():
                decrypted_text += self.__lower_text_decrypter.decrypt(character)
            else:
                decrypted_text += character
        return decrypted_text