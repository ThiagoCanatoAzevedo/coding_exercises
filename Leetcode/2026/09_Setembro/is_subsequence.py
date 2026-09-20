def isSubsequence(s: str, t: str):
    s_pos = 0
    for char in t:
        if s_pos < len(s) and s[s_pos] == char:
            s_pos += 1
    
    return s_pos == len(s)

    
print(isSubsequence("aaaaaa", "bbaaaaaa"))

"""
Anotações importantes por exercício:
- Nome exercício: Is Subsequence
- Data realizado: 20/09/2026
- Tempo de desenvolvimento: 30 minutos
- Dificuldade (leetcode): Easy
- Dificuldade (pessoal): Easy
- Tópico trabalhado: Two Pointers, String e Dynamic Programming
- Complexidade (Time/space): O(n) e O(1)

- Resolvi sozinho? (sim / dica / solução): Com dica
- Resumo da solução/ideia: Apenas ver se, com base na posição da letra em s, se ela é igual a letra atual em t. Se sim, aumenta um na posição s, se não, já retorna do 
laço como falso, visto que as letras devem estar na sequência correta
- Onde travei: Travei em pegar essa sacada das posições... Fiquei tentando algo parecido, mas que não ia a lugar nenhum
"""

