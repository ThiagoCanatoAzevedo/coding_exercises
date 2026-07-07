def lengthOfLastWord(s):
    return len(s.split()[len(s.split())-1])


print(lengthOfLastWord(s = "   fly me   to   the moon  "))

"""
Anotações importantes por exercício:
- Nome exercício: Length of Last Word
- Data realizado: 13/06/2026
- Tempo de desenvolvimento: 5 minutos
- Dificuldade (leetcode): Easy
- Dificuldade (pessoal): Easy
- Tópico trabalhado: String
- Complexidade (Time/space): O(n) e O(n)

- Resolvi sozinho? (sim / dica / solução): Sim
- Resumo da solução/ideia: Apenas dar um splitt na string através do espaço dela, gerando uma lista e, assim, pegando o tamanho do último valor da lista
- Onde travei: Não travei
"""
