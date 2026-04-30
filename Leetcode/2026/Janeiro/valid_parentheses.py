def isValid(s):
    stack = []
    dict_keys = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for char in s:
        if char in dict_keys:
            stack.append(char)
        else:
            if not stack:
                return False
            last = stack.pop()
            if dict_keys[last] != char:
                return False

    return not stack

"""
Anotações importantes por exercício:
- Nome exercício: Valid Parentheses
- Data realizado: 17/01/2025
- Tempo de desenvolvimento: 50min
- Dificuldade (leetcode): Fácil
- Dificuldade (pessoal): Médio
- Tópico trabalhado: String e Stack (Pilha - LIFO)
- Complexidade (Time/space): O(n)/O(n)

- Resolvi sozinho? (sim / dica / solução): dica
- Resumo da solução/ideia: Percorrer a string usando uma pilha, ou seja, empilhar aberturas e, ao encontrar um fechamento, 
                           verificar se ele corresponde à última abertura. No final, a pilha deve estar vazia.
- Onde travei: Na tentativa de resolver comparando apenas caracteres adjacentes (i e i+1) ou separando aberturas e fechamentos, 
               sem considerar que o problema exige validar aninhamento. Faltou perceber que a regra correta é LIFO (último que abre, primeiro que fecha), o que exige o uso de uma pilha.
"""
