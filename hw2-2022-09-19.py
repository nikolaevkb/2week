# №1

letters = 'Who keeps company with the wolf, will learn to howl.'
template = 'w'
exclude = 'l'

sym = 0
for letters in 'Who keeps company with the wolf, will learn to howl.':
    if letters == template:
        sym +=1
print(sym)

# №2

str = 'Who keeps company with the wolf, will learn to howl.'
res_str = str.replace(exclude, '')
print(res_str)
