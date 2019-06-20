# Simulador de Árbitro de Barramento 

# Entradas

n_perifericos = int(input('Insira a quantidade de perifericos: '))

perifericos = []

print('\nInforme quais são os perfirecos:')
for i in range(0,n_perifericos):
    perifericos.append(int( input() ))

periferico_prioridade = {}

print('\nInforme a prioridade de cada periferico:')
for i in perifericos:
    periferico_prioridade[i] = (int( input() ))

print('\nInforme a ordem de solicitação dos periféricos (1 a 3, sendo 1 a mais baixa) (Digite S para sair): ')
ordem_time_solicitacao = []

while (True):
    valor = input()
    if (valor == 's' or valor =='S'):
        break
    else:
        ordem_time_solicitacao.append([int(valor),0])

print('\nInforme o tempo (multiplo de 5) para cada periferico')
for i in ordem_time_solicitacao:
    i[1] = int(input())


print('\nPeriferico e prioridade:\n',periferico_prioridade)
print('\nOrdem e tempo:\n',ordem_time_solicitacao, '\n')


# Dayse chaning

def daisyChaining (ordem_time): 
    dayse_chaning = []
    for i in ordem_time:
        dayse_chaning.append(i[0])

    print("Dayse Chaning:", ' '.join(map(str, dayse_chaning)))
    return dayse_chaning


# Fixa

def prioridadeFixa(ordem_time, peri_prioridade):
    fixa = []
    for i in range(1,4):  #esse for considera que a prioridade varia de 1 a 3
        prioridade_atual = 4 - i
        for j in ordem_time:
            if peri_prioridade[j[0]] == prioridade_atual:
                fixa.append(j[0])

    print("Prioridade fixa:", ' '.join(map(str, fixa)))
    
    return fixa


# Rotativa

def rotativa(ordem_time, peri_prioridade): 
   
    peri_prioridade_inverso = peri_prioridade.copy()
    
    #inverte prioridades considerando que varia de 1 a 3
    for key, value in peri_prioridade_inverso.items():
        if value == 3:
            peri_prioridade_inverso[key] = 1
        elif value == 1:
            peri_prioridade_inverso[key] = 3
        else: 
            pass

    rotativa = []

    for i in range(1,4):  #esse for considera que a prioridade varia de 1 a 3
        prioridade_atual = 4 - i
        for j in ordem_time_solicitacao:
            if peri_prioridade_inverso[j[0]] == prioridade_atual:
                rotativa.append(j[0])

    print("Prioridade rotativa:", ' '.join(map(str, rotativa)))
    
    return rotativa


# Justiça

def justica(ordem_time): 
   
    ordem_time_copy = [row[:] for row in ordem_time]
    justice = []

    while(ordem_time_copy):
        
        for i in ordem_time_copy:
            if i[1] > 0:
                justice.append(i[0])
                i[1] = i[1] - 5
                
        for i in ordem_time_copy:
            if i[1] == 0:
                ordem_time_copy.remove(i)

    print("Justiça:", ' '.join(map(str, justice)))
    
    return justice


daisyChaining(ordem_time_solicitacao)


prioridadeFixa(ordem_time_solicitacao,periferico_prioridade)


rotativa(ordem_time_solicitacao,periferico_prioridade)


justica(ordem_time_solicitacao)