import tkinter
from tkinter import *
from tkinter import messagebox

class game:
    def __init__(self):
        #Initializing grid and first player
        self.player='X'
        self.grids=[['','',''],['','',''],['','','']]
        
        self.root=tkinter.Tk() #root window creation
        self.root.title('Tic Tac Toe') #root window title
        
        self.buttons=[] #dummy board for buttons
        for i in range(3):
            row=[] #dummy row
            for j in range(3):
                button=Button(self.root,width='10',height='15',text='',command=lambda i=i,j=j:self.move(i,j))
                button.grid(row=i,column=j)
                row.append(button)
            self.buttons.append(row) #all rows appending to the dummy board
    
    def move(self, row, col): #For movement and assigning Values
     if self.grids[row][col] == '':
         self.grids[row][col] = self.player
         self.buttons[row][col].config(text=self.player)
         
         if self.check_winner(self.player):
             messagebox.showinfo('Game Over','Winner is '+self.player)
             self.root.destroy()    
         elif self.check_draw():
             messagebox.showinfo('Game Over','Its A Draw')
             self.root.destroy()
         
         self.player = 'O' if self.player == 'X' else 'X' #Reassigning player type
    
    
    def check_winner(self,player):#Checking for winner
        for i in range(3):
            if player==self.grids[0][i]==self.grids[1][i]==self.grids[2][i]:
                return True
            elif player==self.grids[i][0]==self.grids[i][1]==self.grids[i][2]:
                return True
            elif player==self.grids[0][0]==self.grids[1][1]==self.grids[2][2]:
                return True
            elif player==self.grids[0][2]==self.grids[1][1]==self.grids[2][0]:
                return True
                
        
    def check_draw(self):#checking for draw
        for row in self.grids:
            if '' in row:
                return False
        return True
            
    def run(self):#Running the window
        self.root.mainloop()
        
out=game()#Object Creation for game
out.run()#Running Game