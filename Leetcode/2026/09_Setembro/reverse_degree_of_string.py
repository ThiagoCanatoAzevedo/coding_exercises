def reverseDegree(s):
    sum = 0
    for index, char in enumerate(s):
        pos_in_alphabet_reversed = 27 - (ord(char) - 96)
        sum = (pos_in_alphabet_reversed * (index+1))+sum
    return sum
    
reverseDegree("abc")

"""
Anotações importantes por exercício:
- Nome exercício: Reverse Degree of a String
- Data realizado: 19/09/2026
- Tempo de desenvolvimento: 20 minutos
- Dificuldade (leetcode): Easy
- Dificuldade (pessoal): Easy
- Tópico trabalhado: Mid Level, String, Simulation
- Complexidade (Time/space): O(n) / O(1)

- Resolvi sozinho? (sim / dica / solução): sim
- Resumo da solução/ideia: Apenas pegar a posição da letra no alfabeto e fazer menos 27 (já que o 'a' começa em 1) e, com base na posição dela na string, multiplicar
pelo seu índice
- Onde travei: Não travei
"""

