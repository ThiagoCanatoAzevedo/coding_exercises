def stemmer(text):
    list_words = text.split()
    cannot_be = ["ed", "ly", "ing"]
    finished = []
    
    for i in range (len(list_words)):
        len_word = len(list_words[i])
        
        if list_words[i][-2:] in cannot_be:
            new_word = list_words[i][:len_word-2]
        elif list_words[i][-3:] in cannot_be:
            new_word = list_words[i][:len_word-3]
        else:
            new_word = list_words[i]
            
        if len(new_word) > 8:
            new_word = new_word[:8]
            
        finished.append(new_word)
        
    return(' '.join(finished))
        
        
print(stemmer("the results cannot be extrapolated to other patient group"))