def lengthOfLongestSubstring(s):
    atual = ""
    bkp = ""

    for i in range(len(s)):
        if s[i] in atual:
            pos = atual.index(s[i])
            atual = atual[pos + 1:]

        atual += s[i]

        if len(atual) > len(bkp):
            bkp = atual

    return len(bkp)


"""
Anotações importantes por exercício:
- Nome exercício: Longest Substring Without Repeating Characters
- Data realizado: 14/01/2026
- Tempo de desenvolvimento: 50 minutos
- Dificuldade (leetcode): Médio
- Dificuldade (pessoal): Médio
- Tópico trabalhado: Strings e Sliding Window
- Complexidade (Time/space): O(n²) / O(n)

- Resolvi sozinho? (sim / dica / solução): Dica
- Resumo da solução/ideia: Percorrer a string mantendo uma substring sem repetição e, ao encontrar um caractere repetido, 
                           remover apenas até essa repetição, atualizando o maior tamanho encontrado.
- Onde travei: Travei em assumir que, ao encontrar uma repetição, a substring atual deveria ser resetada (atual = ""). 
               Isso fazia perder caracteres que ainda poderiam compor a próxima substring válida, impedindo o algoritmo de 
               encontrar a maior substring sem repetição.
"""
