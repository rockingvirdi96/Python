import random
import re
import string
from string import punctuation


AlphabetList = list(string.ascii_lowercase)
AlphabetListUpper = list(string.ascii_uppercase)
listDigits = [x for x in range(0, 10)]
specialChars = list(set(punctuation))
CipherCodeDict = {AlphabetList[x]: AlphabetList[x+3]
                  for x in range(0, len(AlphabetList)-3)}
extra = {'x': 'a', 'y': 'b', 'z': 'c'}
CipherCodeDict.update(extra)

EncryptedPasswords = []
PassWordStorage = {}
RealPasswords = []
GeneratedPasswords = []

restart = True


def checkPassword(password):
    SpecialChars = re.compile('[@_!#$%^&*.()<>"?/"\"|}{~:]')
    numbers = re.compile('\\d')
    alphabetsUpperCase = re.compile('[A-Z]')
    alphabetsLowerCase = re.compile('[a-z]')
    if (numbers.search(password) is None):
        print("Password not Strong(Digit is missing)")
        return False
    else:
        if (SpecialChars.search(password) is None):
            print(
                "Password Not Strong(Special Char Missing[@_!#$%^&*''().<>?/|}{~:]")
            return False
        else:
            if (alphabetsUpperCase.search(password) is None):
                print("Password not Strong (UpperCaseLetterMissing)")
                return False
            else:
                if (len(password) < 8):
                    print("Atleast 8 character are required.")
                    return False
                else:
                    if (alphabetsLowerCase.search(password) is None):
                        print("Password not Strong(Lower Case char is missing)")
                        return False
        RealPasswords.insert(
            len(RealPasswords), password)
        return True


def GeneratedPassword():
    generatedPassword = ""
    for x in range(0, random.randint(10, 15)):
        choice = random.randint(1, 5)
        if (choice == 1):
            generatedPassword += str(
                listDigits[random.randint(0, len(listDigits)-1)])
        if (choice == 2):
            generatedPassword += str(
                specialChars[random.randint(0, len(specialChars)-1)])
        if (choice == 3):
            generatedPassword += str(
                AlphabetList[random.randint(0, len(AlphabetList)-1)])
        if (choice == 4):
            generatedPassword += str(
                AlphabetListUpper[random.randint(0, len(AlphabetListUpper)-1)])
    print("Password Generated: " + generatedPassword)
    GeneratedPasswords.append(generatedPassword)


def EncryptPassword(passwordString):
    passs = list(passwordString)
    index = -1
    tempDict = {}
    EncryptedPassword = ""
    for x in passs:
        index = index+1
        if x.isupper():
            if x.lower() in CipherCodeDict:
                passs[index] = CipherCodeDict[x.lower()].upper()
        if x.islower():
            if x in CipherCodeDict:
                passs[index] = CipherCodeDict[x]
    for x in passs:
        EncryptedPassword += x
    tempDict = {passwordString: EncryptedPassword}
    EncryptedPasswords.insert(len(EncryptedPasswords), EncryptedPassword)
    PassWordStorage.update(tempDict)


while(restart):
    trial = True
    print("--------PASSWORD WALLET-------------------")
    print("1.Check if your password is strong or not.")
    print("2.Encrypt the password you just entered.")
    print("3.AutoGenerate a Strong Password.")
    print("4.Check the Real and Encrypted Passwords.")
    print("5.Quit")
    choice = int(input())
    if (choice == 1):
        while(trial):
            print("Enter your Password: ")
            password = input()
            if (checkPassword(password)):
                print("Password Accepted")

                trial = False
            else:
                print("Try Again")
    if (choice == 2):
        EncryptPassword(str(RealPasswords[len(RealPasswords)-1]))
        print("Password Encrypted.")
    if (choice == 3):
        GeneratedPassword()
    if (choice == 4):
        print("Real Password: " + str(RealPasswords))
        print("Encrypted Password: " + str(EncryptedPasswords))
        print("Dictionary: " + str(PassWordStorage))
        print("Generated Passwords: " + str(GeneratedPasswords))
    if (choice == 5):
        restart = False

print("Thanks")
