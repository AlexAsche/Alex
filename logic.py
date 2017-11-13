##### 4 Gewinnt Logik 
#     by Jan Huesmann

import sys
##Variablen: Größe des Spielfeldes
rows = 4
columns = 4

grid = dict()  #Spielfeld ist ein 2-dimensionales Dictonary

#Funktionen
def clearGrid(rows, columns):   #Erstelle Spielfeld
    for x in range(rows):
        for y in range(columns):
            grid[(x, y)] = "."
    return grid

def checkRunningGame():     #Überprüfe, ob es noch freie Felder gibt
    try:
        for x in range(rows):
            for y in range(columns):
                if grid[(x,y)] == ".":
                    return True
    except: return False
    
def setPlayer1():
    y = int(input("Player 1: Please enter column: "))
    x = rows-1
    if grid[0,y] == ".": #Ist Spalte bereits voll?
        while x>-1:
            if grid[x,y] == ".": #Ist Feld bereits voll?
                grid[x,y] = "O" #setze String von Player 1
                return grid
            else:
                x -= 1     #wenn Feld bereits voll: probiere nächst höhere Reihe
    else:
        print("Column is full")
        setPlayer1() #Spalte ist bereits voll: lasse Spieler andere Spalte wählen
    

def setPlayer2():
    y = int(input("Player 2: Please enter column: "))
    x = rows-1

    if grid[0,y] == ".":
        while x>-1:
            if grid[x,y] == ".":
                grid[x,y] = "X"
                return
            else:
                x -= 1
    else:
        print("Column is full")
        setPlayer1()
    
def checkforWin():
    if HorizontalWin() or VerticalWin() or DiagonalWin() == True:
        sys.exit("Game ends")
    if HorizontalWin() == False:
        print("No Win")
        pass
    
def HorizontalWin():
    try:
        for x in range(rows):
            for y in range(columns):
                if grid[(x,y)] == "O" and grid[(x,y+1)] == "O" and grid[(x,y+2)] == "O" and grid[(x,y+3)] == "O":
                    print("Player 1 wins (Horizontal)")
                    return True

    except Exception:
        pass
            
    try:
        for x in range(rows):
            for y in range(columns): 
                if grid[(x,y)] == "X" and grid[(x,y+1)] == "X" and grid[(x,y+2)] == "X" and grid[(x,y+3)] == "X":
                    print("Player 2 wins (Horizontal)")
                    return True
                
    except Exception:
        pass
    return False
                    
def VerticalWin():
    try:
        for x in range(rows):
            for y in range(columns):
                if grid[(x,y)] == "O" and grid[(x+1,y)] == "O" and grid[(x+2,y)] == "O" and grid[(x+3,y)] == "O":
                    print("Player 1 wins (Vertical)")
                    return True
    except Exception:
        pass
        
    try:
        for x in range(rows):
            for y in range(columns): 
                if grid[(x,y)] == "X" and grid[(x+1,y)] == "X" and grid[(x+2,y)] == "X" and grid[(x+3,y)] == "X":
                    print("Player 2 wins (Vertical)")
                    return True
    except Exception:
        pass
    return False
    
def DiagonalWin():
    try:
        for x in range(rows):
            for y in range(columns):
                if grid[(x,y)] == "O" and grid[(x+1,y+1)] == "O" and grid[(x+2,y+2)] == "O" and grid[(x+3,y+3)] == "O":
                    print("Player 1 wins (Diagonal)")
                    return True

    except Exception:
        pass

    try:
        for x in range(rows):
            for y in range(columns): 
                if grid[(x,y)] == "X" and grid[(x+1,y+1)] == "X" and grid[(x+2,y+2)] == "X" and grid[(x+3,y+3)] == "X":
                    print("Player 2 wins (Diagonal)")
                    return True
    except Exception:
        pass
    return False


##Spiel

clearGrid(rows,columns)
print(grid)

while checkRunningGame() == True:
        setPlayer1()
        print(grid)
        checkforWin()
        setPlayer2()
        print(grid)
        checkforWin()

sys.exit("Grid is full: stalemate")
