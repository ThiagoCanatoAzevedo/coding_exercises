def removeElement(nums, val):   
    nums[:] = ([value for value in nums if value != val])
    return len(nums)
        
print(removeElement(nums=[3,2,2,3], val=3))

"""
Anotações importantes por exercício:
- Nome exercício: Remove Element
- Data realizado: 13/06/2026
- Tempo de desenvolvimento: 20 minutos
- Dificuldade (leetcode): Easy
- Dificuldade (pessoal): Easy
- Tópico trabalhado: Array e Two Pointers
- Complexidade (Time/space): O(n) e O(n)

- Resolvi sozinho? (sim / dica / solução): Sim
- Resumo da solução/ideia: A ideia é remover os valores iguais a "val". Porém, essa solução não é a melhor, visto que a complexidade de espaço é O(n), mas poderia ser O(1) se eu fizesse uma list comprehension melhor
- Onde travei: Não travei
"""
