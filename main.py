import CaesarCipher as CC
import PlayfairCipher as PC
import RowTranspositionCipher as CTC
if __name__ == '__main__':
    # Caesar Cipher
    print("Caesar Cipher Encrypted Text : " + CC.Encrypt("azy", 5))
    print("Caesar Cipher Decrypted Text : " + CC.Decrypt("fed", 5))

    # Playfair Cipher
    EncryptedText = PC.Encrypt("mohammed", "section")
    PlainText = PC.Decrypt(EncryptedText, "section")
    print("Playfair Cipher Encrypted Text : "+EncryptedText)
    print("Playfair Cipher Decrypted Text : " + PlainText)
    # Row Transposition Cipher
    EncryptedText = CTC.Encrypt("welcome to section six", "4213")
    PlainText = CTC.Decrypt(EncryptedText, "4213")
    print("Row Transposition Cipher Encrypted Text : "+EncryptedText)
    print("Row Transposition Cipher Decrypted Text : " + PlainText)
