def singleNumber(nums):
    contagem = {}

    for num in nums:
        contagem[num] = contagem.get(num, 0) + 1

    for num in contagem:
        if contagem[num] == 1:
            return num


print(singleNumber([2,2,1]))


"""
Anotações importantes por exercício:
- Nome exercício: Single Number
- Data realizado: 15/05/2026
- Tempo de desenvolvimento: 30 minutos
- Dificuldade (leetcode): Easy
- Dificuldade (pessoal): Medium
- Tópico trabalhado: Array e Bit Manipulation
- Complexidade (Time/space): O(n) e O(n)

- Resolvi sozinho? (sim / dica / solução): Dica
- Resumo da solução/ideia: Não cheguei a pensar em usar dicionário python para salvar a chave (valor da lista) e valor (quantidade de vezes que aparece). Assim, com 2 laços for, um para popular o dicionário e outro para verificar o valor que possui apenas 1 (valor da lista que aparece apenas uma vez), fica simples de resolver esse exercício
- Onde travei: Em lembrar de usar dicionários.
"""
