'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# check current letter and next letter
# if they are 'th' 

# if length of string is less than or equal to 1, return 0

# if first two characters are th, return 1
# recursively call on all characters except 0th

# else, recursively call on all characters except 0th

# iterative to help prep
# def count_th(word):    

#   count = 0
#   for i in range(len(word)-1):

#     if (word[i] + word[i+1]) == 'th':
#       count += 1

#   return count

def count_th(word):  
  if len(word) <= 1:
    return 0
  elif word[0:2] == 'th':
    return 1 + count_th(word[1:])
  else:
    return count_th(word[1:])

# print(count_th('abthcth'))
# print(count_th('abcthefthghith'))