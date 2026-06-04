def findLengthOfLCIS(nums):
    if not nums:
        return 0
    
    cont = 1
    max_cont = 1
    
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            cont += 1
            max_cont = max(max_cont, cont)
        else:
            cont = 1
    
    return max_cont
    
print(findLengthOfLCIS([1,3,5,4,2,3,4]))

"""
Anotações importantes por exercício:
- Nome exercício: Longest Continuous Increasing Subsequence
- Data realizado: 01/05/2026
- Tempo de desenvolvimento: 27 minutos
- Dificuldade (leetcode): Easy
- Dificuldade (pessoal): Easy
- Tópico trabalhado: Mid Level, Array e Pointers
- Complexidade (Time/space): O(n) e O(1)

- Resolvi sozinho? (sim / dica / solução): Não, precisei de ajuda do GPT para entender onde estava inicialmente errando
- Resumo da solução/ideia: Basicamente, através do for, ficar verificando se o valor atual é menor em relação ao valor da frente dele. Se sim, soma um no contado. Se não, não soma nada.
- Onde travei: Travei em perceber que era para pegar a maior substring contínua CRESCENTE. Estava fazendo uma lógica que verificava a diferença da subtração entre o valor atual e o valor a sua frente. Em sua essência, ele fazia isso, mas de forma muito mais complicada. 
"""