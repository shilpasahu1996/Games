Player_1 = input("Player_1 Enter: ")
Player_2 = input("Player_2 Enter: ")

if Player_1== 'rock' and Player_2 == 'paper':
    print(f'Congratulations Player 2 wins')
elif Player_1== 'rock' and Player_2 == 'scissor':
    print(f'Congratulations Player 1 wins')
elif Player_1== 'paper' and Player_2 == 'rock':
    print(f'Congratulations Player 1 wins')
elif Player_1== 'paper' and Player_2 == 'scissor':
    print(f'Congratulations Player 2 wins')
elif Player_1 == 'scissor' and Player_2 == 'paper':
    print(f'Congratulations Player 1 wins')
elif Player_1 == 'scissor' and Player_2 == 'rock':
    print(f'Congratulations Player 2 wins')
elif Player_1== 'rock' and Player_2 == 'rock':
    print(f'tie')
elif Player_1== 'paper' and Player_2 == 'paper':
    print(f'tie')
elif Player_1== 'scissor' and Player_2 == 'scissor':
    print(f'tie')
else:
    print('Invalid Enter')





