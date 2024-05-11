import os
import random
os.system("clear")

class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    def display(self):
        #print("───────────")
        print("┌───┬───┬───┐")
        print("│ %s │ %s │ %s │" % (self.cells[1], self.cells[2], self.cells[3]))
        print("├───┼───┼───┤")
        print("│ %s │ %s │ %s │" % (self.cells[4], self.cells[5], self.cells[6]))
        print("├───┼───┼───┤")
        print("│ %s │ %s │ %s │" % (self.cells[7], self.cells[8], self.cells[9]))
        print("└───┴───┴───┘")
    def update_cell(self,cell_choice,player):
        if self.cells[cell_choice]==" ":
           self.cells[cell_choice]=player

    def is_winner(self,player):
        if self.cells[1]==player and self.cells[2]==player and self.cells[3]==player:
            return True
        if self.cells[3]==player and self.cells[4]==player and self.cells[5]==player:
            return True
        if self.cells[6]==player and self.cells[7]==player and self.cells[8]==player:
            return True
        if self.cells[1]==player and self.cells[4]==player and self.cells[7]==player:
            return True
        if self.cells[2]==player and self.cells[5]==player and self.cells[8]==player:
            return True
        if self.cells[3]==player and self.cells[6]==player and self.cells[9]==player:
            return True
        if self.cells[1]==player and self.cells[5]==player and self.cells[9]==player:
            return True
        if self.cells[3]==player and self.cells[5]==player and self.cells[7]==player:
            return True
        
    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    
    def full_board(self):
        point = [1,2,3,4,5,6,7,8,9]
        for i in point:
            if self.cells[i]!=" ":
               return False
        return True
    def is_Tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell!=" ":
                used_cells+=1
        if used_cells == 9:
            return True
        else:
            return False
    def AI_move(self,player):
      
        #When the match start AI chose the Center's Board

        if self.cells[5] == " ":
            self.update_cell(5,player)

        
        #AI block you
        
        #AI can win you
       
        #AI chose random

        else:
            for i in range(1,10):
              if self.cells[i]==" ":
                self.update_cell(i,player)
                break



board = Board()
board.display()

def print_header():
    print("WELCOME TIC TAC TOE GAME")

def refresh_screen():

    #Clear the screen
    os.system("clear")

    #Print header Game
    print_header()

    #Show the Board

    board.display()

while True:
    refresh_screen()

    print("This is your turn.")

    #Get X input
    
    x_choice=int(input("(X) Chose your input form 1 to 9 >"))

    #Update X input
    board.update_cell(x_choice,"X")

    #Refresh the screen
    refresh_screen()

    #Check for X win

    if board.is_winner("X"):
        print("YOU WIN\n")

        play_again = input("Would you like to play again? (YES/NO) >").upper()

        if play_again == "YES":
            board.reset()
            continue
        else:
            break
    #Check for no winner

    if board.is_Tie():
        print("\nA TIE GAME!\n")
        play_again = input("Would you like to play again? (YES/NO) >").upper()

        if play_again == "YES":
            board.reset()
            continue
        else:
            break

    print("This is AI's turn.")

   
    board.AI_move("O")
  
    refresh_screen()

    #Check for O win

    if board.is_winner("O"):
        print("AI WIN")
        play_again = input("Would you like to play again? (YES/NO) >").upper()

        if play_again == "YES":
            board.reset()
            continue
        else:
            break


    #Check for no winner

    if board.is_Tie():
        print("\nA TIE GAME!\n")
        play_again = input("Would you like to play again? (YES/NO) >").upper()

        if play_again == "YES":
            board.reset()
            continue
        else:
            break




