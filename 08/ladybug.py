import random

alphabetAnd_ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"

num_games = int(input())

def ladybug_game():
    num_cells = 10 #random.randrange(100)
    board = ""
    space = False
    freq = []
    #create "board" (string of _'s and chars)
    for i in range(num_cells):
        '''
        if random.randrange(10) < 5:
            board += "_"
        else:
        '''
        x = int(random.randrange(len(alphabetAnd_)))
        letter = alphabetAnd_[x]
        board += letter
        
    print("Number of cells: " + str(num_cells))
    print("Board: " + board)
    
    #create freq list of alphabetical chars
    for f in range(len(alphabetAnd_)-1):
        freq.append(0)
    
    for char in board:
        if char == "_":
            space = True
        else:
            c_loc = alphabetAnd_.find(char)
            freq[c_loc] += 1
    
    for x in freq:
        if x == 1:
            return False

    return space
            
    #board is good as long as there is at least one "_",
    #and at least two copies of every letter that appears
            
for i in range(num_games):
    print(ladybug_game())
    
    