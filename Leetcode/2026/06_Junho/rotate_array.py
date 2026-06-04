def rotate(nums, k):
    k %= len(nums)
    nums_splitted = nums[len(nums)-k:]
    del nums[len(nums)-k:]
    nums[:0] = nums_splitted
    
    return(nums)
    
rotate([1,2], 7)

"""
Anotações importantes por exercício:
- Nome exercício: Rotate Array
- Data realizado: 04/06/2026
- Tempo de desenvolvimento: 40 minutos
- Dificuldade (leetcode): Médio
- Dificuldade (pessoal): Médio
- Tópico trabalhado: Array, Math e Two Pointers
- Complexidade (Time/space): O(n) e O(k)

- Resolvi sozinho? (sim / dica / solução): Dica
- Resumo da solução/ideia: Simplesmente pensei em fazer um split do array de acordo com o tamanho dele e de k
- Onde travei: Não imaginei que, para k, poderia vir um valor maior que o tamanho do array. Dito isso, quando em um dos testes o tamanho do array era 2 e k=7, o algoritmo quebrou. Com isso, o ChatGPT me ajudou com a dica simples mas funcional de usar o módulo de k com base no tamanho do array. Assim, qualquer valor de k maior que o tamanho do array será reduzido a um range do tamanho do array
"""
