def caesar_encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted < ord('a'):  shifted = ord('z') - (ord('a')- shifted - 1)%26 
                if shifted > ord('z'):  shifted = (shifted - ord('z') - 1)%26 + ord('a')
            elif char.isupper():
                if shifted < ord('A'): shifted = ord('Z') - (ord('A')- shifted - 1)%26 
                if shifted > ord('Z'): shifted =(shifted - ord('Z') - 1)%26 + ord('A')
            result += chr(shifted)
        else:
            result += char
    return result
plaintext = input()
key = int(input())
ma_hoa = caesar_encrypt(plaintext, key)
print(ma_hoa)
