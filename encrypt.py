def encrypt(plainText,shiftNum):
    newText = ""
    for letter in plainText: 
        numIndex = abcd.index(letter)
        index2 = numIndex + shiftNum
        newNum = str(abcd[index2])
        newText += newNum
    return newText

def decrypt(plainText,shiftNum):
    newText = ""
    for letter in plainText: 
        numIndex = abcd.index(letter)
        index2 = numIndex - shiftNum
        newNum = str(abcd[index2])
        newText += newNum
    return newText

abcd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','j','u','v','w','z','y','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','j','u','v','w','z','y']

choice = input("Would you like to encrypt or decrypt?(E/D): ")
if choice == "E":
    plainText = input("Write down the word you want to encrypt: ")
    shiftNum = int(input("How many charachters would you like to shift? "))
    print(encrypt(plainText,shiftNum))
else:
    plainText = input("Write down the word you want to decrypt: ") 
    shiftNum = int(input("How many charachters would you like to shift? "))   
    print(decrypt(plainText,shiftNum))

