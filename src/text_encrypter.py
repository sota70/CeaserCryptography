from encrypter import Encrypter
from upper_text_encrypter import UpperTextEncrypter
from lower_text_encrypter import LowerTextEncrypter

class TextEncrypter(Encrypter[str]):

    def __init__(self, shift_count: int):
        super().__init__(shift_count)
        self.__upper_text_encrypter: UpperTextEncrypter = UpperTextEncrypter(shift_count)
        self.__lower_text_encrypter: LowerTextEncrypter = LowerTextEncrypter(shift_count)
    
    def encrypt(self, input: str) -> str:
        encrypted_text: str = ""
        for character in input:
            if character.isupper():
                encrypted_text += self.__upper_text_encrypter.encrypt(character)
            elif character.islower():
                encrypted_text += self.__lower_text_encrypter.encrypt(character)
            else:
                encrypted_text += character
        return encrypted_text