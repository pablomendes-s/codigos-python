val = []
for rep in range (0,5):
    n = int(input(f'Didite o {rep+1}º número: '))
    if rep == 0 or n > val[-1]:
        val.append(n)
    else:
        for pos, x in enumerate(val):
            if n <= x:
                val.insert(pos, n)
                break
print(val)
