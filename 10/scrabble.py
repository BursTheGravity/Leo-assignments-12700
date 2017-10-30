TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10), (7,7))
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

letter_vals = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':5,'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,'v':4,'w':4,'x':8,'y':4,'z':10}

def make_scrabble_board():
    board=[]
    for i in range(15):
        line=[]
        for i in range(15):
            line.append('_')
        board.append(line)

    for r,c in TRIPLE_WORD_SCORE:
        board[r][c] = 'T'

    for r,c in DOUBLE_WORD_SCORE:
        board[r][c] = 'D'

    for r,c in TRIPLE_LETTER_SCORE:
        board[r][c]='t'

    for r,c in DOUBLE_LETTER_SCORE:
        board[r][c] = 'd'
    return board


def print_board(b):
    for line in b:
        print ( ' '.join(line))
        
def add_word_across(board, word, r, c):
    #Check for out of range:
    if c + len(word) > 15:
        return "Word length exceeds board size. Try again."
    else:
        score = 0
        word_dbl = 0
        word_tpl = 0
        word_value = 0
        for l in word:
            word_value += letter_vals.get(l, 0)
        for letter in word:
            #Scoring letter/word
            board_char = board[r][c]
            letter_score = letter_vals.get(letter, 0)
            #Keeping track of double/triple letter/word bonuses
            if board_char == "_":
                score += letter_score
            elif board_char == "d":
                score += 2*letter_score
            elif board_char == "t":
                score += 3*letter_score
            elif board_char == "D":
                word_dbl += 1
            elif board_char == "T":
                word_tpl += 1
            #Update board: adding letter onto board, increment by one
            board[r][c] = letter
            c += 1
        #Checking word bonuses
        if word_dbl != 0:
            score += word_value * 2 * word_dbl
        if word_tpl != 0:
            score += word_value * 3 * word_tpl
        print("Updating board... ")
        print_board(board)
        return "\nScore for adding '" + word + "': " + str(score)

def add_word_down(board, word, r, c):
    #Check for out of range:
    if r + len(word) > 15:
        return "Word length exceeds board size. Try again."
    else:
        score = 0
        word_dbl = 0
        word_tpl = 0
        word_value = 0
        for l in word:
            word_value += letter_vals.get(l, 0)
        for letter in word:
            #Scoring letter/word
            board_char = board[r][c]
            letter_score = letter_vals.get(letter, 0)
            #Keeping track of double/triple letter/word bonuses
            if board_char == "_":
                score += letter_score
            elif board_char == "d":
                score += 2*letter_score
            elif board_char == "t":
                score += 3*letter_score
            elif board_char == "D":
                word_dbl += 1
            elif board_char == "T":
                word_tpl += 1
            #Update board: adding letter onto board, increment by one
            board[r][c] = letter
            r += 1
        #Checking word bonuses
        if word_dbl != 0:
            score += word_value * 2-1 * word_dbl
        if word_tpl != 0:
            score += word_value * 3-1 * word_tpl
        print("Updating board... ")
        print_board(board)
        return "\nScore for adding '" + word + "': " + str(score)

'''
- Haven't added ability to not overwrite previous words; currently assuming
    user will not overwrite words depending on how we'll be using this?
- Does not account for capital letters in word
- Board could be made "cleaner" by not using t, d, T, D's
- Seeable issue: adding words with t/d/T/D and getting bonuses when
    overwriting the letters with another word
- Word bonus scores calculated based on base score of original word WITHOUT
    any letter bonuses applied, before being added to current score.
    Formula: Current score + word_bonus(dbl/tpl) - 1 * base_word_value * # of bonuses
- But otherwise, does the job of adding words across/down & keeping score
    to produce a final score based on t/d letter bonuses and T/D word bonuses
'''

game_board = make_scrabble_board()

print("Printing game board...")
print_board(game_board)
print("\n")
print(add_word_across(game_board, 'hello', 1, 10))
print(add_word_down(game_board, 'goodbye', 1, 5))