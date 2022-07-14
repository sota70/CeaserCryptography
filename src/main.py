from decrypter import Decrypter
from encrypter import Encrypter
from text_decrypter import TextDecrypter
from text_encrypter import TextEncrypter


if __name__ == "__main__":
    text_encrypter: Encrypter = TextEncrypter(3)
    text_decrypter: Decrypter = TextDecrypter(3)
    encrypted_text: str = text_encrypter.encrypt("pasS_wOrd")
    decrypted_text: str = text_decrypter.decrypt(encrypted_text)
    print(encrypted_text, decrypted_text)
