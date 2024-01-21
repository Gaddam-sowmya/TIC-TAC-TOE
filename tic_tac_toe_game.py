import random


board = [" " for _ in range(9)]

Player_symbol = "X"
computer_symbol= "O"

def draw_board():
    print("-------------")
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print("-------------")
    print("|",board[3],"|",board[4],"|",board[5],"|")
    print("-------------")
    print("|",board[6],"|",board[7],"|",board[8],"|")
    print("-------------")

def check_winner(symbol):
       # check horizontal line
      for i in range(0,9,3):
            if board[i]==board[i+1]==board[i+2]==symbol:
                   return True
        # check vertical line
      for i in range(3):
            if board[i]==board[i+3]==board[i+6]==symbol:
                   return True
        # check diagonal
      if board[0]==board[4]==board[8]==symbol or board[2]==board[4]==board[6]==symbol:
            return True
      return False
def player_turn():
    while True:
        try:
            position = int(input("Enter your move(1 - 9):")) - 1
            if 0 <= position <= 8 and board[position] == ' ':
                board[position] = Player_symbol
                draw_board()
                if check_winner(Player_symbol):
                    print('Congratulations! You win!')
                else:
                    computer_turn()
                break
            else:
                print("Invalid move. Please enter a valid position.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def computer_turn():
      available_moves=[i for i in range(9) if board[i]==' ']
      if len(available_moves) > 0:
         position = random.choice(available_moves)
         board[position]=computer_symbol
         draw_board()
         if check_winner(computer_symbol):
              print('Sorry! You lose!')
         else:
              player_turn()
      else:
           print("It's a tie!")
def main():
     print("Tic Tac Toe Game")
     draw_board()
     player_turn()
     computer_turn()

if __name__=='__main__':
     main()