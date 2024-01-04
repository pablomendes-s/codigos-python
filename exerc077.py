tup = ('cavalo', 'zebra', 'girafa', 'buro', 'cabra', 'cachorro', 'elefante')
for vog in tup:
    print(f'\nA palavra {vog.upper()} possui as vogais:', end='')
    for let in vog:
        if let in 'aeiou':
            print(f'\33[32m{let.lower()}\33[m',end='')
