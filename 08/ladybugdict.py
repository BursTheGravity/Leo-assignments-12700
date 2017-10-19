import random

alphabetAnd_ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"

num_games = int(input())

def ladybug_game():
    num_cells = random.randrange(100)
    board = ""
    space = False
    char_tracker = {}
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
    
    #for all chars on board, make a dict of frequencies
    for char in board:
        if char == "_":
            space = True
        elif char in char_tracker.keys():
            char_tracker[char] += 1
        else:
            char_tracker.setdefault(char, 1)
    
    #check if any char appears once, and return false if true
    if 1 in char_tracker.values():
        return False

    return space
            
    #board is good as long as there is at least one "_",
    #and at least two copies of every letter that appears
            
for i in range(num_games):
    print(ladybug_game())
    
    
