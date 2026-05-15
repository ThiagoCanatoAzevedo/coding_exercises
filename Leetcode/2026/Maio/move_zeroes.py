def moveZeroes(nums):
    amount_zeroes = nums.count(0)
    count = 0
    
    while count < amount_zeroes:
        nums.remove(0)
        count+=1
        
    nums.extend([0] * amount_zeroes)
    return nums
    
    
print(moveZeroes([0,1,0,3,12]))

"""
Anotações importantes por exercício:
- Nome exercício: Move Zeroes
- Data realizado: 15/05/2026
- Tempo de desenvolvimento: 20 minutos
- Dificuldade (leetcode): Easy
- Dificuldade (pessoal): Easy
- Tópico trabalhado: Array e Two Pointers (de acordo com LeetCode, porque não usei Two Pointers)
- Complexidade (Time/space): O(n^2) e O(1)

- Resolvi sozinho? (sim / dica / solução): Sim
- Resumo da solução/ideia: Como resolvo os exercícios em Python, pensei em usar e abusar das funções built-in que ele possui (remove e extend). Porém, apesar de ser mais simples de resolver assim, o time complexity desse código é péssimo. Poderia, sim, ter utilizado ponteiros, mas queria um desenvolvimento mais rápido. Logo que li o exercício, pensei nesses dois formatos de solução: utilizando as funções built-in do Python ou com ponteiro. 
- Onde travei: Apenas em lembrar como as funções eram implementadas.
"""
