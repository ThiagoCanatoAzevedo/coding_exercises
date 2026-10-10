def plusOne(digits):
    digits_cleaned = int("".join(map(str, digits)))+1
    return [int(digit) for digit in str(digits_cleaned)]
    

print(plusOne([9]))

"""
Anotações importantes por exercício:
- Nome exercício: Plus One
- Data realizado: 10/10/2026
- Tempo de desenvolvimento: 10 minutos
- Dificuldade (leetcode): Easy
- Dificuldade (pessoal): Easy
- Tópico trabalhado: Array, Math
- Complexidade (Time/space): O(n) / O(n)

- Resolvi sozinho? (sim / dica / solução): sim
- Resumo da solução/ideia: Apenas transformar, com join, o array em int e, após isso, com list comprehension, passar de int para array
- Onde travei: Não travei
"""

