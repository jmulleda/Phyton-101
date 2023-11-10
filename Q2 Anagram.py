import string

# Ask two sets of strings from user
string1 = str(input ("Please type string # 1: "))
string2 = str(input ("Please type string # 2: "))

# Convert to lower case and remove spaces
# Sort letters
string1 = sorted(string1.lower().replace(' ', ''))
string2 = sorted(string2.lower().replace(' ', ''))

# Display sorted letters
print("Sorted string 1:", string1)
print("Sorted string 2:", string2)

# Test string1 and string2
def anagram():
    if (string1 == string2):
        return "TRUE. The strings are anagrams."
    else:
        return "FALSE. The strings are NOT anagrams."
print(anagram())