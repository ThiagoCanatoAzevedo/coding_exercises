def generate(numRows):
    final_sequence = []

    for i in range(1, numRows+1):
        actual_sequence = []
        
        if len(final_sequence) >= 1:
            linha_anterior = final_sequence[-1]
                        
        if i <= 2:
            actual_sequence = [1]*i
        else:
            actual_sequence.append(1)
            for j in range(len(linha_anterior)-1): 
                actual_sequence.append(linha_anterior[j] + linha_anterior[j+1])
            actual_sequence.append(1)
                
        final_sequence.append(actual_sequence)
    
    return final_sequence
        
print(generate(5))

"""
Anotações importantes por exercício:
- Nome exercício: Pascal's Triangle
- Data realizado: 04/06/2026
- Tempo de desenvolvimento: 1 hora
- Dificuldade (leetcode): Fácil
- Dificuldade (pessoal): Médio
- Tópico trabalhado: Array e Dynamic Programming
- Complexidade (Time/space): O(n²) e O(n²)

- Resolvi sozinho? (sim / dica / solução): Com dicas do ChatGPT
- Resumo da solução/ideia: Enquanto o tamanho das linhas não for maior que 2, fazer o caso base (sempre 1 nos arrays). Após isso, fazer a soma dos valores adjacentes. 
- Onde travei: Travei em entender como fazer os arrays após os casos bases (quando numRows > 2)
"""
