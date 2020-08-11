str1 = 'w3resource'
dict = {}
for letter in str1:
    dict[letter] = dict.get(letter, 0) + 1
print(dict)