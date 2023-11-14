import numpy
import numpy as np


def __delete_spaces(PlainText: str) -> str:
    new_plaintext = ''
    for i in range(0, len(PlainText)):
        if PlainText[i] not in ' ':
            new_plaintext += PlainText[i]
    return new_plaintext


def __delete_repetitive_char(EncryptionKey: str) -> str:
    charset = []
    for i in range(0, len(EncryptionKey)):
        if EncryptionKey[i] not in charset:
            charset.append(EncryptionKey[i])
    new_key = ''.join(charset)
    return new_key


def __create_key_matrix(EncryptionKey: str) -> numpy.array:
    KeyMatrix = np.zeros([5, 5], dtype=object)
    EncryptionKey = __delete_repetitive_char(EncryptionKey)
    EncryptionKey = __delete_spaces(EncryptionKey)
    col = 0
    row = 0
    EncryptionKeyLen = len(EncryptionKey)
    index = 0
    for row in range(0, 5):
        for col in range(0, 5):
            KeyMatrix[row, col] = EncryptionKey[index]
            index += 1
            if index >= EncryptionKeyLen:
                col += 1
                break
        if index >= EncryptionKeyLen:
            break
    for char in 'abcdefghiklmnopqrstuvwxyz':
        if char not in EncryptionKey:
            KeyMatrix[row, col] = char
            col += 1
        if col >= 5:
            col = 0
            row += 1
    return KeyMatrix


def __creat_text_list(PlainText: str) -> list:
    PlainTextList = []
    new_plaintext = __delete_spaces(PlainText)
    i = 0
    if len(new_plaintext) % 2 == 0:
        while i < len(new_plaintext):
            if i+1 < len(new_plaintext) and new_plaintext[i] != new_plaintext[i + 1]:
                PlainTextList.append(new_plaintext[i] + new_plaintext[i + 1])
                i += 2
            else:
                PlainTextList.append(new_plaintext[i] + "x")
                i += 1
    else:
        while i < len(new_plaintext):
            if i < len(new_plaintext) - 1:
                if new_plaintext[i] != new_plaintext[i + 1]:
                    PlainTextList.append(new_plaintext[i] + new_plaintext[i + 1])
                    i += 2
                else:
                    PlainTextList.append(new_plaintext[i] + "x")
                    i += 1
            else:
                PlainTextList.append(new_plaintext[i] + "z")
                i += 1
    return PlainTextList


def Encrypt(PlainText: str, EncryptionKey: str) -> str:
    EncryptionKey = EncryptionKey.lower()
    PlainText = PlainText.lower()
    KeyMatrix = __create_key_matrix(EncryptionKey)
    PlainText_List = __creat_text_list(PlainText)
    EncryptedText = ""
    for twochars in PlainText_List:
        row_index1, col_index1 = np.where(KeyMatrix == twochars[0])
        row_index2, col_index2 = np.where(KeyMatrix == twochars[1])
        if row_index1 == row_index2:
            newcol_index1 = 0
            newcol_index2 = 0

            if col_index1 + 1 < 5:
                newcol_index1 = col_index1 + 1
            if col_index2 + 1 < 5:
                newcol_index2 = col_index2 + 1

            EncryptedText += KeyMatrix[row_index1, newcol_index1]
            EncryptedText += KeyMatrix[row_index2, newcol_index2]
        elif col_index1 == col_index2:
            newrow_index1 = 0
            newrow_index2 = 0

            if row_index1 + 1 < 5:
                newrow_index1 = row_index1 + 1
            if row_index2 + 1 < 5:
                newrow_index2 = row_index2 + 1

            EncryptedText += KeyMatrix[newrow_index1, col_index1]
            EncryptedText += KeyMatrix[newrow_index2, col_index2]
        else:
            EncryptedText += KeyMatrix[row_index1, col_index2]
            EncryptedText += KeyMatrix[row_index2, col_index1]
    EncryptedText = ''.join(EncryptedText)
    return EncryptedText


def Decrypt(EncryptedText: str, EncryptionKey: str) -> str:
    EncryptionKey = EncryptionKey.lower()
    EncryptedText = EncryptedText.lower()
    KeyMatrix = __create_key_matrix(EncryptionKey)
    EncryptedText_List = __creat_text_list(EncryptedText)
    PlainText = ""
    for twochars in EncryptedText_List:
        row_index1, col_index1 = np.where(KeyMatrix == twochars[0])
        row_index2, col_index2 = np.where(KeyMatrix == twochars[1])
        if row_index1 == row_index2:
            newcol_index1 = 4
            newcol_index2 = 4

            if col_index1 - 1 >= 0:
                newcol_index1 = col_index1 - 1
            if col_index2 - 1 >= 0:
                newcol_index2 = col_index2 - 1

            PlainText += KeyMatrix[row_index1, newcol_index1]
            PlainText += KeyMatrix[row_index2, newcol_index2]
        elif col_index1 == col_index2:
            newrow_index1 = 4
            newrow_index2 = 4

            if row_index1 - 1 >= 0:
                newrow_index1 = row_index1 - 1
            if row_index2 - 1 >= 0:
                newrow_index2 = row_index2 - 1

            PlainText += KeyMatrix[newrow_index1, col_index1]
            PlainText += KeyMatrix[newrow_index2, col_index2]
        else:
            PlainText += KeyMatrix[row_index1, col_index2]
            PlainText += KeyMatrix[row_index2, col_index1]
    PlainText = ''.join(PlainText)
    return PlainText
