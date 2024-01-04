times = ('Palmeiras','Flamengo','Fluminense','Grêmio','Athletico-PR','Bragantino','Fortaleza','Cuiabá,'
'São Paulo','Atlético-MG','Cruzeiro','Corinthians','Internacional','Goiás','Bahia','Santos','Vasco','Coritiba','América-MG')
print(f'Os  5 primeiros times são: {times[:5]}')
print(f'Os 4 últimos times são: {times[-4:]}')
print(f'A lista de times em ordem alfabetica é:{sorted(times)}')
print(f'O timr Fortaleza esta na posição: {times.index("Fortaleza")+1}')