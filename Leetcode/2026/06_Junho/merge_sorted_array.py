def merge(nums1, m, nums2, n):
    nums1[:]=sorted(nums1[:m]+nums2)
    return nums1

print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))


"""
Anotações importantes por exercício:
- Nome exercício: Merge Sorted Array
- Data realizado: 13/06/2026
- Tempo de desenvolvimento: 10 minutos
- Dificuldade (leetcode): Easy
- Dificuldade (pessoal): Easy
- Tópico trabalhado: Array, Two Pointers e Sorting
- Complexidade (Time/space): O(m+n) e O(1)
- Resolvi sozinho? (sim / dica / solução): Sim
- Resumo da solução/ideia: Apenas tive que perguntar para o GPT o que ele queria, pois a explicação no LeetCode está péssima. Mas, em linhas gerais, apenas modifiquei o array "nums1" para a soma dele (a partir do indice m) com o "nums2". Como aqui não tinha restrição de complexidade de tempo, pude usar o "sorted()" do python
- Onde travei: Apenas em entender o que o exercicio queria
"""
