str=input("Enter a string :")

vowel=0
consonant=0
digit=0
space=0
for ch in str:
    if ch.lower() in "a,e,i,o,u" or ch.lower() in "A,E,I,O,U":
        vowel+=1
    elif ch.isalpha():
        consonant+=1
    elif ch.isnumeric():
        digit+=1
    elif ch.isspace():
        space+=1
print("Vowels :", vowel)
print("Consonants :", consonant)
print("Digits :", digit)
print("Spaces :", space)
