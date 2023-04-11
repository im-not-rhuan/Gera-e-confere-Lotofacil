import Jogo as j
# import Confere as c

def main():

    n_games = input("Quantos jogos diferentes deseja fazer? ")

    while (1):
        game =j.Jogo(int(n_games))
        bolao = game.create_games()
        for jogo in bolao:
            print(jogo)
        is_ok = input("Se estiver de acordo, tecle (y), se não, pressione qualquer tecla.\n")
        if is_ok == 'y':
            break
        
    print(f'Você gastou {game.getValor()} reais.')
    print('Está na hora de conferir se temos um vencedor!')
    game.confere(bolao)
if __name__ == "__main__":
    main()