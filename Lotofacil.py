import Jogo as j

def main():

    n_games = input("Quantos jogos diferentes deseja fazer? ")  #pede-se o numero de apostas desejadas

    while (1):
        game =j.Jogo(int(n_games))
        bolao = game.create_games()
        for jogo in bolao:
            print(jogo)
        is_ok = input("Se estiver de acordo, tecle (y), se não, pressione qualquer tecla.\n")  #caso queira outros jogos aleatorios, basta pressionar qualquer tecla diferente de y
        if is_ok == 'y':
            break
        
    print(f'Você gastou {game.getValor()} reais.')
    print('Está na hora de conferir se temos um vencedor!')
    game.confere(bolao)
if __name__ == "__main__":
    main()  