# Tic-Tac-Toe

board = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
         'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
         'low-l': ' ', 'low-m': ' ', 'low-r': ' '}

def update_board(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-----')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-----')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])

def your_move(pos):
    if board[pos] != ' ':
        return print('Target is occupied. Try again.')
    board[pos] = 'X'
    for k in board:
        if board[k] == ' ':
           board[k] = 'O'
           break
    update_board(board)

def check_winner(board):
    if all(v == 'X' or 'O' for v in board.values()):
        return
    elif board['top-l'] == board['top-m'] == board['top-r']:
        return print('Winner: ' + board['top-l'])
    elif board['mid-l'] == board['mid-m'] == board['mid-r']:
        return print('Winner: ' + board['mid-l'])
    elif board['low-l'] == board['low-m'] == board['low-r']:
        return print('Winner: ' + board['low-l'])
    else:
        return print('Winner: ' + board['mid-l'])

while any(v == ' ' for v in board.values()):
    position = input('Your Move: ')
    check_winner(board)
    your_move(position)

print('Tie')
