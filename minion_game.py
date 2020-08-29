def minion_game(string):
    vowels = set('AEIOU')
    stuart = kevin = 0
    for i, c in enumerate(string):
        if c in vowels:
            kevin += len(string) - i
            #0 + 5 - 0
            #5 + 5 - 3
            #7 + 5 - 4 
        else:
            stuart += len(string) - i
            #0 + 5 - 1
            #4 + 5 - 2
    
    if stuart > kevin:
        print('Stuart', stuart)
    elif kevin > stuart:
        print('Kevin', kevin)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input("Enter a word: ")
    minion_game(s)


