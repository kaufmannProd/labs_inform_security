def encryption(fock):
    encrypt = fock
    key = 3
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet += alphabet.lower()
    encrypted = ""
    for letter in encrypt:
        position = alphabet.find(letter)
        newPosition = position + key
        if letter in alphabet:
            encrypted = encrypted + alphabet[newPosition]
        else:
            encrypted = encrypted + letter
    return encrypted

f1 = open('file.txt', 'r')
text = "".join(f1)
gg = encryption(text)
f2 = open('encrypted.txt', 'w')
f2.writelines(gg)
f2.close()
