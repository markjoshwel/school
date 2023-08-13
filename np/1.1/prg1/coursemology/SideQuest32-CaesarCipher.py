def caesarEncrypt(plaintext: str, n: int) -> str:
    abc: str = "abcdefghijklmnopqrstuvwxyz"
    ciphertext: str = ""

    for c in plaintext:
        abcpos = abc.index(c.lower()) + n

        if c.isupper():
            ciphertext += abc[abcpos if (abcpos <= 25) else abcpos - 26].upper()
        else:
            ciphertext += abc[abcpos if (abcpos <= 25) else abcpos - 26]

    return ciphertext
