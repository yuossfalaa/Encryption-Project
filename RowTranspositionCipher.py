import math

import numpy
import numpy as np


def __delete_spaces(PlainText: str) -> str:
    new_plaintext = ''
    for i in range(0, len(PlainText)):
        if PlainText[i] not in ' ':
            new_plaintext += PlainText[i]
    return new_plaintext


def __make_cipher_matrix(PlainText: str, EncryptionKeyList: list, col: int, row: int) -> numpy.array:
    matrix = np.zeros([row, col], dtype=object)
    for i in range(0, col):
        matrix[0, i] = EncryptionKeyList[i]
    char_index = 0
    for i in range(1, row):
        for j in range(0, col):
            if char_index < len(PlainText):
                matrix[i, j] = PlainText[char_index]
                char_index += 1
            else:
                matrix[row-1, col-1] = 'x'
    return matrix


def __make_decipher_matrix(EncryptedText: str, EncryptionKeyList: list, col: int, row: int) -> numpy.array:
    matrix = np.zeros([row, col], dtype=object)
    for i in range(0, col):
        matrix[0, i] = EncryptionKeyList[i]
    char_index = 0
    EncryptionKeyListSorted = sorted(EncryptionKeyList)
    for key_index in EncryptionKeyListSorted:
        col_index = np.where(matrix == key_index)[1]
        for i in range(1, row):
            matrix[i, col_index] = EncryptedText[char_index]
            char_index += 1
    return matrix


def Encrypt(PlainText: str, EncryptionKey: str) -> str:
    PlainText = __delete_spaces(PlainText)
    EncryptionKeyList = list(EncryptionKey)
    col = int(len(EncryptionKeyList))
    row = int(math.ceil(len(PlainText) / col)) + 1
    CipherMatrix = __make_cipher_matrix(PlainText, EncryptionKeyList, col, row)
    EncryptionKeyListSorted = sorted(EncryptionKeyList)
    EncryptedText = ""
    for key_index in EncryptionKeyListSorted:
        col_index = np.where(CipherMatrix == key_index)[1]
        for i in range(1, row):
            EncryptedText += CipherMatrix[i, col_index]
    EncryptedText = ''.join(EncryptedText)
    return EncryptedText


def Decrypt(EncryptedText: str, EncryptionKey: str) -> str:
    EncryptionKeyList = list(EncryptionKey)
    col = int(len(EncryptionKeyList))
    row = int(math.ceil(len(EncryptedText) / col)) + 1
    DeCipherMatrix = __make_decipher_matrix(EncryptedText, EncryptionKeyList, col, row)
    PlainText = ""
    for i in range(1, row):
        for j in range(0, col):
            PlainText += DeCipherMatrix[i, j]
    PlainText = ''.join(PlainText)
    return PlainText
