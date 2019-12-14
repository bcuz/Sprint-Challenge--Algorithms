'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# do iteratively first?


# check current letter and next letter
# if they are 'th' 


def count_th(word):    
  count = 0
  for i in range(len(word)-1):

    if (word[i] + word[i+1]) == 'th':
      count += 1

  return count

print(count_th('abcthefthghith'))