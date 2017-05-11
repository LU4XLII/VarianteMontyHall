# Variante do problema de Monty Hall
Este script trata-se uma simulação para uma variante do problema de [Monty Hall](https://pt.wikipedia.org/wiki/Problema_de_Monty_Hall) que me foi apresentada pelo Alex Damaceno.

# Enunciado
Você esta na plateia de um programa de auditório e estão fazendo um jogo com uma menina. No jogo são apresentadas 5 portas para a menina e atrás de uma delas está o prêmio de 20mil reais, sendo que para ganhar o prêmio ela precisa escolher a porta certa.  A menina, então, escolhe a porta 3.
Após isso o apresentador decide ajudar um pouco, e para isso ele abre a porta 5 mostrando que ela está vazia. Nesse momento, a menina decide mudar para a porta 4. Para ajudar mais, o apresentador abre a porta 1 e mostra que também está vazia. Em reação, a menina pede para mudar para a porta 2 e o apresentador  anuncia seu último auxílio: ele abre a porta 3 e mostra que não havia nada lá também. Precisando fazer a sua última escolha, a menina diz que oferece 5mil reais do prêmio (caso ela ganhe) se alguém da plateia a ajudar a escolher entre a porta 4 e a 2, dizendo as probabilidades de cada uma ser a correta.

# Solução
## Início
  1: 20%  2: 20%  3: 20%  4: 20%  5: 20%
## A menina escolhe a porta 3 e o apresentador abre a porta 5
1: 26,67% 2: 26,67% 3: 20%  4: 26,67% 5: 0%
## A menina escolhe a porta 4 e o apresentador fecha a porta 1
1: 0% 2: 40%  3: 33,33% 4: 26,67% 5: 0%
## A menina escolhe a porta 2 e o apresentador fecha a porta 3
1: 0% 2: 40%  3: 0% 4: 60%  5: 0%
