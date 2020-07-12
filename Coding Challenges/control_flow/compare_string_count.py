# Compare Strings by Count of Characters

# Create a function that takes two strings as arguments and return either True or False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.
# Examples

# comp("AB", "CD") ➞ True

# comp("ABC", "DE") ➞ False

# comp("hello", "edabit") ➞ False

# Notes

#     Don't forget to return the result.
#     If you get stuck on a challenge, find help in the Resources tab.
#     If you're really stuck, unlock solutions in the Solutions tab.

# My Soultion
def comp(txt1, txt2):
  text1 = len(txt1)
  text2 = len(txt2)
  if text1 == text2 and text2 == text1:
    return True
  else:
    return False

print(comp("Robin","Hi"))

# Other Soultion
# def comp2(txt1, txt2):
# 	return len(txt1) == len(txt2)

# print(comp2("hi","Hi"))