import datetime
print(datetime.time())
remedios = []

quantidade_remedios = int(input('Quantos remédios você quer cadastrar? '))


for q in range(1,quantidade_remedios+1):
    remedio = str(input(f'Nome do {q}º remédio: ')).strip().lower()
    horario = int(input('Que horas você tomou? [HORA CHEIA]'))
    freq = int(input('Com que frequência você deve tomar o remédio? '))
    prox_hora = datetime.time(horario).hour + datetime.time(freq).hour
    dados = (remedio,horario,prox_hora)
    remedios.append(dados)
    print(f'Próximo horario para tomar o remédio: {prox_hora} Horas')
    print(remedios)

print(f'{"Nº":<4}|{"Remédio":^18}|{"Horário":^10}|{"Próximo horário:":^20}')
for c in range(1,len(remedios)+1):
    print(f'{c}{remedios[0].title():^26}{remedios[1]:}H{remedios[2]:>14}H')

