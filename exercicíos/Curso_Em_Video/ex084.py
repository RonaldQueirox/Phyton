def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 4, 3, 2, 4, 7]
dobra(valores)
print(valores)

