letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
string = ''
for letter in letters:
    if not letter.isupper():
        string += letter
letters = string
print(letters)