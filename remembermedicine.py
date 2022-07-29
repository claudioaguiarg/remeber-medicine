import datetime
print(datetime.time())
remedios = {}
quantidade_remedios = int(input('Quantos remédios você quer cadastrar? '))

for q in range(1,quantidade_remedios+1):
    remedios[f'remedio{q}'] = str(input(f'Nome do {q}º remédio: ')).strip().lower()
    remedios[f'horario{q}'] = int(input('Que horas você tomou? [HORA CHEIA]'))
    freq = int(input('Com que frequência você deve tomar o remédio? '))
    if remedios[f'horario{q}'] + freq < 24:
        remedios[f'prox_hora{q}'] = datetime.time(remedios[f'horario{q}']).hour + datetime.time(freq).hour
    else:
        remedios[f'prox_hora{q}'] = datetime.time((remedios[f'horario{q}']+freq)-24).hour

print(f'{"Nº":<4}|{"Remédio":^18}|{"Horário":^10}|{"Próximo horário:":^20}')
for c in range(1,quantidade_remedios+1):
    print(f'{c}{remedios[f"remedio{c}"]:^26}{remedios[f"horario{c}"]:}H{remedios[f"prox_hora{c}"]:>14}H')
