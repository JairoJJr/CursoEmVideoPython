'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocaçõa. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time Corinthians.'''

times = 'BOTAFOGO','PALMEIRAS','CRUZEIRO','FORTALEZA','SÃO PAULO','FLUMINENSE','GRÊMIO','INTERNACIONAL','BAHIA','ATHLETICO-PR','VASCO','RED BULL BRAGANTINO','CUIABÁ','SANTOS','ATLÉTICO-MG','FLAMENGO','CORINTHIANS','GOIÁS','CORITIBA','AMÉRICA-MG'

print(f'Os 5 primeiros são {times[0:5]}')
print(f'Os 4 últimos são {times[-4:]}')
print(f'Em ordem alfabética os 20 times são {sorted(times)}')
print(f'Corinthians está na {times.index("CORINTHIANS")+1}ª posição')