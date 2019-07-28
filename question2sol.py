str1=input("Enter the string: ")
letterCount=0
digitCount=0
for a in str1:
    if a.isalpha():
        letterCount=letterCount+1
    elif a.isdigit():
        digitCount=digitCount+1
print("Number of letters: ", letterCount)
print("Number of Digits: ", digitCount)
