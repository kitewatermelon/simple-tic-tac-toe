board = [x+1 for x in range(9)]
print("""
======== TIC-TAC-TOE ========  
O first, X second
!! LET'S START !!
ONLY below inputs are allowed 
1 <= number <= 9
============================= 
      """)

END_FLAG = 1
def is_draw(board):
    end_count = 0
    for i in range(9):
        if type(board[i]) == type('a'):
            end_count += 1
        if end_count == 9:
            print("GAME OVER IT'S DRAW")
            return 0
    return 1

def is_win(board, player):
    # 가로
    for i in range(0, 7, 3):
        if board[i:i+3] == [player,player,player] :
            print(f'{player} IS WINNER')
            return 0
        
    for i in range(3):
        if [board[i],board[i+3],board[i+6]] == [player,player,player] :
            print(f'{player} IS WINNER')
            return 0
        
    if [board[0],board[4],board[8]] == [player,player,player] or\
         [board[2],board[4],board[6]] == [player,player,player]:
            print(f'{player} IS WINNER')
            return 0
         
    return 1

player = "O"
n = 0

while END_FLAG:
        
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])
    
    print("input where you want")
    n = input()
    n = int(n)
    
    # 위치 판별기
    while n > 9 or n < 1 :
        print("worng number! input again!")
        n = input()
        n = int(n)
        
    while type(board[n-1]) == type('a'):
        print("it's not a empty space! input again!")
        n = input()
        n = int(n)
        
    
    board[n-1] = player
    END_FLAG = is_draw(board)
    END_FLAG = is_win(board, player)
    
    
    if player == 'O':
        player = 'X'
    else : 
        player = 'O'