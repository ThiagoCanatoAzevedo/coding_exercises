def stopWords(text, k):
    phrase_list = text.split()
    last_phrase = []
    for i in phrase_list:
        if phrase_list.count(i) >= k and i not in last_phrase:
            last_phrase.append(i)
    
    return(last_phrase)
    
print(stopWords("a mouse is smaller than a dog but a dog is stronger", 2))