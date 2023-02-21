pasto1 = [['zebras', 'branca', 'bege', 'preta', 'malhada'],

          ['vacas', 'branca', 'marrom', 'preta', 'malhada'],

          ['cavalo', 'branco', 'preto', 'castanho', 'cinza'],

          ['ovelhas', 'branca', 'preta', 'cinza', 'malhada']]



pasto2 = []



pasto2.extend(pasto1[:3])

del pasto1[:3]



print("Animais do Pasto 2:", pasto2)

print("Animais do Pasto 1:", pasto1)