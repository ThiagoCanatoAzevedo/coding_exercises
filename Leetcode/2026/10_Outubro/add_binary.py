def addBinary(a: str, b: str):
    return f"{int(a, 2) + int(b, 2):b}"


print(addBinary("1010","1011"))

"""
Anotações importantes por exercício:
- Nome exercício: Add Binary
- Data realizado: 10/10/2026
- Tempo de desenvolvimento: 5 minutos
- Dificuldade (leetcode): Easy
- Dificuldade (pessoal): Easy
- Tópico trabalhado: Math, String, Bit Manipulation e Simulation
- Complexidade (Time/space):

- Resolvi sozinho? (sim / dica / solução): Dica
- Resumo da solução/ideia: Pensei no simples: passar o valor em binário de a e b para decimal, somar e depois retornar para binario
- Onde travei: Não sabia que era possível passar a base que quero na função int com python. Com isso fica muito mais facil, visto que consigo retornar os 2 já em decimal,
fazer a soma e, com o format (f) retornar em binario novamente
"""

