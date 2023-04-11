from random import sample
import random
import requests
random.seed(87)  #seed do meu número favorito xd

class Jogo:
    def __init__(self, n_games):
        self.n_games = n_games
    """Método construtor, onde o único atributo é 
        o número de jogos desejado pelo usuário"""

    def create_games(self):  #método para criar jogos, aonde serão criados
                             #n jogos informados pelo usuário
        bet = []  #lista de apostas
        inlist = []  #lista de backup (para obter apostas distintas)
        for aposta in range(self.n_games):
            luck = sample(range(1, 26), 15)  #cria a aposta (15 valores entre 1 e 25)
            luck.sort()  #ordena a lista
            if luck not in inlist:  #se a aposta estiver fora da lista de backup
                bet.append(luck)  #insere na lista de de apostas
                inlist.append(luck)  #insere na lista de backup
            else:
                aposta -=1  #caso aposta repetida, refaz a lista aleatória
        return bet
    
    def getValor(self):
        return self.n_games*2.5  #retorna o valor gasto nas apostas
    
    def confere(self, jogo):
        r = requests.get('https://loteriascaixa-api.herokuapp.com/api/lotofacil/latest')
        if r.status_code  == 200:
            r1 = r.json()
            resultado = r1['dezenas']
            r_to_int = []
            for cast in resultado:
                cast = int(cast)
                r_to_int.append(cast)
            print("Resultado:")
            print(r_to_int)
            losses = 0
            wins = 0
            for confere in jogo:
                if(len(set(r_to_int) & set(confere)) == 15):
                    print(f"Você ganhou o prêmio máximo! O jogo campeão foi o {confere}")
                    wins +=1
                elif (len(set(r_to_int) & set(confere)) == 14):
                    print(f"Você ganhou o segundo prêmio! O jogo premiado foi o {confere}")
                    wins +=1
                elif (len(set(r_to_int) & set(confere)) > 10 and len(set(r_to_int) & set(confere)) <=13):
                    print(f"Você Acertou {len(set(r_to_int) & set(confere))}! O jogo premiado foi o {confere}")
                    wins +=1
                else:
                    losses += 1
            print(f"Total de jogos premiados: {wins}\nTotal de jogos perdidos: {losses}")
        else:
            print('Ue')