def majorityElement(nums) -> int:
    candidato = None
    contador = 0
    
    for num in nums:
        if contador == 0:
            candidato = num
        if num == candidato:
            contador += 1
        else:
            contador -= 1
            
    contador_real = 0
    for num in nums:
        if num == candidato:
            contador_real += 1
            
    if contador_real > len(nums) // 2:
        return candidato
    return -1

print(majorityElement([3,2,3]))

"""
Anotações importantes por exercício:
- Nome exercício: Majority Element
- Data realizado: 23/05/2026
- Tempo de desenvolvimento: 15 minutos
- Dificuldade (leetcode): Easy
- Dificuldade (pessoal): Easy
- Tópico trabalhado:Array, Hash Table, Divide and Conquer, Sorting and Counting
- Complexidade (Time/space): O(n) e O(1)

- Resolvi sozinho? (sim / dica / solução): Tive uma diva do do ChatGPT para utilizar o algoritmo de Boyer-Moore
- Resumo da solução/ideia: Utilizar o algoritmo de Boyer-Moore
- Onde travei: Consegui resolver uma vez sozinho, porém, em O(n^2) e O(n). Quando perguntei ao ChatGPT como melhorar o código, ele citou o algoritmo de Boyer-Moore e, com isso, consegui resolver em O(n) e O(1)
"""
