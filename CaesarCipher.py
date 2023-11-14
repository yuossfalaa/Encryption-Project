def Encrypt(PlainText: str, EncryptionKey: int) -> str:
    EncryptedText = ""
    for i in range(0, len(PlainText)):
        if PlainText[i].isupper():
            EncryptedText += chr(((ord(PlainText[i]) - 65 + EncryptionKey) % 26) + 65)
        else:
            EncryptedText += chr(((ord(PlainText[i]) - 97 + EncryptionKey) % 26) + 97)
    return EncryptedText


def Decrypt(EncryptedText: str, EncryptionKey: int) -> str:
    PlainText = ""
    for i in range(0, len(EncryptedText)):
        if EncryptedText[i].isupper():
            PlainText += chr(((ord(EncryptedText[i]) - 65 - EncryptionKey) % 26) + 65)
        else:
            PlainText += chr(((ord(EncryptedText[i]) - 97 - EncryptionKey) % 26) + 97)

    return PlainText
