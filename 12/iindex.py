import csv

def clean_word(w):
    '''
    input: "word" from a text with puncutation, etc
    output: "clean" word in lowercase and without punctuation
    '''
    all_letters=""
    for l in w:
        if l.isalpha() or l == "'":
            l = l.lower()
            all_letters += l
    return all_letters

def offenders_inverted_txt():
    '''
    input: data from offenders-clean.csv
    output: inverted dictionary containing all words said in each offender's
            last statements and their corresponding TDCJ Numbers
    '''
    
    #reading file using csv.DictReader, adding data to a list
    f = open("offenders-clean.csv")
    csv_dict_reader = csv.DictReader(f)
    l = []
    for line in csv_dict_reader:
        l.append(line)
    f.close()
    
    #final dictionary with
    dict = {}
    
    for offender_data in l:
        #variables for data needed: TDCJ_number and last_statement
        TDCJ_number = offender_data['TDCJ Number']
        last_statement = offender_data['Last Statement']
        #split last_statement into "words"
        for word in last_statement.split(" "):
            #cleans word
            word = clean_word(word)
            #adds word and corresponding TDCJ_number to dict
            dict.setdefault(word, [])
            if TDCJ_number not in dict[word]:
                dict[word].append(TDCJ_number)

    return dict

'''
NOTE:
- I made words lowercase and removed punctuation except for apostrophes ("'")
- There is a lot of data due to the amount of words said in offenders' last
    statements; expect lag when running and when scrolling through data
'''

inverted_data = offenders_inverted_txt()
print(inverted_data)

'''
#Additional test cases for specific words if necessary (also less laggy):
word = "i'm"
print(word, ":", inverted_data[word])
'''