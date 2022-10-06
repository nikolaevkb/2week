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
var = 'Who keeps company with the wolf, will learn to howl.'

for i in var:
    if i != exclude:
        print((i), end="")
        
