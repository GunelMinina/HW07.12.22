# Крестики-нолики

def draw_board(board):
    print("-------------") 
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = int(input("Куда поставим " + player_token+"? "))
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы сделать ход")

def check_win():
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return True
    return False

board = list(range(1,10))
round = 1
win = False
player = 'X'

while round < 9 or not win:
    draw_board(board)
    take_input(player)
    if round > 4 and check_win():
        draw_board(board)
        print('Победил -', player)
        win = True
        break
    round += 1
    if (player == 'X'):
        player = 'O'
    else:
        player = 'X'


