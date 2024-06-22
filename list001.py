letters=['a','b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters.append('h')
print(letters)

letters.extend(['i', 'j', 'k'])
print(letters)

letters.insert(0, 'z')
print(letters)

letters.remove('a')
print(letters)

letters.pop(1)
print(letters)

print(letters.count('c'))

letters.reverse()
print(letters)

letters.sort()
print(letters)

letters.sort(reverse=True)