def romanToInteger(roman_number:str):
    base = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    list_roman_numbers = list(roman_number)
    list_integer_numbers = []
    list_final = []
    
    for i in list_roman_numbers:
        if i in base.keys():
            list_integer_numbers.append(base[i])
            
    i = 0
    while i < len(list_integer_numbers):
        if i + 1 < len(list_integer_numbers) and list_integer_numbers[i] < list_integer_numbers[i+1]:
            list_final.append(list_integer_numbers[i+1] - list_integer_numbers[i])
            i+=2
        else:
            list_final.append(list_integer_numbers[i])
            i+=1
            
    return sum(list_final)

"""
Exercise annotations:
- Name: Roman To Integer
- Runtime: 14ms
- Memory: 12.56MB
"""