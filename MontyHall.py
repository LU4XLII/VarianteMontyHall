import random

#Lista com uma porta contendo prêmio
lista = [1,0,0,0,0]

#Número de testes
n = 1000000

#Número de vezes em que cada porta está correta
porta2 = 0
porta4 = 0

#Função que gera portas não escolhidas
def portaRandomica(lista):
    porta = random.randint(0,4)
    for i in lista:
        if i == porta:
            return portaRandomica(lista)
    return porta
        
#Inicia os testes
print('Iniciando', n,'testes.')
for i in range(n):
    if i % 100000 == 0:
        print('Teste número:', i)
    #Gera o cenário randômico
    random.shuffle(lista)
    for correta in range(4):
        if lista[correta] == 1:
            break
    #Escolha do participante
    escolha = random.randint(0,4)
    #Abre uma porta sem nada
    portaSem1 = portaRandomica([escolha, correta])
    #Abre a segunda porta sem nada
    portaSem2 = portaRandomica([escolha, correta, portaSem1])

    #Aqui complica
    #Simulando aleatoriedade, a porta 2 será a porta demarcada por 1
    #e a porta 4 será a porta demarcada com zero
    portaFinal = portaRandomica([escolha, portaSem1, portaSem2])
    aleatorio = random.randint(0,1)
    #Conta
    if aleatorio == 1:
        if portaFinal == correta:
            porta2 += 1
    if aleatorio == 0:
        if portaFinal != correta:
            porta4 += 1

#Exibe os resultados
n_vitoriosos = porta2+porta4
print('----------------------------------------------------')
print('Número de testes vitoriosos:', n_vitoriosos)
print('Número de testes em que a porta 2 é vitoriosa:', porta2)
print('Probabilidade porta 2:', porta2/n_vitoriosos)
print('Número de testes em que a porta 4 é vitoriosa:', porta4)
print('Probabilidade porta 4:', porta4/n_vitoriosos)
print('----------------------------------------------------')
