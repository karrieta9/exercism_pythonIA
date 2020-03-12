def score(word):
    word = word.upper()
    cont_score = 0
    score_one = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
    score_two = ['D', 'G']
    score_three = ['B', 'C', 'M', 'P']
    score_four = ['F', 'H', 'V', 'W', 'Y']
    score_five = ['K']
    score_eigth = ['J', 'X']
    score_ten = ['Q', 'Z']

    for i in word:
        if i in score_one:
            cont_score += 1
        elif i in score_two:
            cont_score += 2    
        elif i in score_three:
            cont_score += 3    
        elif i in score_four:
            cont_score += 4    
        elif i in score_five:
            cont_score += 5    
        elif i in score_eigth:
            cont_score += 8    
        elif i in score_ten:
            cont_score += 10
            
    return cont_score
