def reverseWords(s):
    s_arr   = s.split(' ')
    s_final = ""
    for c in s_arr:
        s_final += c[::-1] + " "
    return s_final[:-1]
    
print(reverseWords("Let's take LeetCode contest"))

"""
Anotações importantes por exercício:
- Nome exercício: Reverse Words in a String III
- Data realizado: 01/05/2026
- Tempo de desenvolvimento: 15 minutos
- Dificuldade (leetcode): Fácil
- Dificuldade (pessoal): Fácil
- Tópico trabalhado: Two Pointers e String
- Complexidade (Time/space): O(n²) e O(n)
- Resolvi sozinho? (sim / dica / solução): Sim, apenas com uma dica para evitar if dentro do laço. Esse if servia apenas para verificar se era a última palavra do array e, assim, não adicionar espaço nessa última palavra  
- Resumo da solução/ideia: Coisa simples. Apenas passar cada palavra da string para dentro de um array usando split, fazer um for passando por cada palavra invertendo-a, "somando" essa palavra invertida em uma string e, por fim, retornar essa string
- Onde travei: Em nenhum momento travei
"""
