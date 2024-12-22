def main():

    game = [
        [1, 1, 2],
        [1, 0, 2],
        [1, 2, 1]
    ]
    result(game)

def result(game):
    if (
            (game[0][0] == game[0][1] == game[0][2] == 'X') or
            (game[1][0] == game[1][1] == game[1][2] == 'X') or
            (game[2][0] == game[2][1] == game[2][2] == 'X') or
            (game[0][0] == game[1][0] == game[2][0] == 'X') or
            (game[0][1] == game[1][1] == game[2][1] == 'X') or
            (game[0][2] == game[1][2] == game[2][2] == 'X') or
            (game[0][0] == game[1][1] == game[2][2] == 'X') or
            (game[0][2] == game[1][1] == game[2][0] == 'X')
    ):
        return 'Player 1 wins'
    elif (
            (game[0][0] == game[0][1] == game[0][2] == '0') or
            (game[1][0] == game[1][1] == game[1][2] == '0') or
            (game[2][0] == game[2][1] == game[2][2] == '0') or
            (game[0][0] == game[1][0] == game[2][0] == '0') or
            (game[0][1] == game[1][1] == game[2][1] == '0') or
            (game[0][2] == game[1][2] == game[2][2] == '0') or
            (game[0][0] == game[1][1] == game[2][2] == '0') or
            (game[0][2] == game[1][1] == game[2][0] == '0')
    ):
        return 'Player 2 wins'
    elif '' in game[0] or '' in game[1] or '' in game[2]:
        return 'game to be played'
    else:
        return 'Game Tied'





if __name__ == '__main__':
    main()