def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)

    if target > nums[len(nums) - 1]:
        return len(nums)

    def binary_search(nums, offset=0):

        if len(nums) == 1:
            if target > nums[0]:
                return offset + 1
            else:
                return offset

        if len(nums) == 2:
            if target < nums[0]:
                return offset
            elif target < nums[1]:
                return offset + 1
            else:
                return offset + 2

        first_number_to_get = int((len(nums) / 2) - 1)
        second_number_to_get = int((len(nums) / 2))

        if (
            target > nums[first_number_to_get]
            and target < nums[second_number_to_get]
        ):
            return offset + second_number_to_get

        else:
            if target > nums[first_number_to_get]:
                return binary_search(
                    nums[second_number_to_get:len(nums)],
                    offset + second_number_to_get
                )
            else:
                return binary_search(
                    nums[0:second_number_to_get],
                    offset
                )

    return binary_search(nums)
    
print(searchInsert([1,3, 5], 4))

"""
Anotações importantes por exercício:
- Nome exercício: Search Insert Position
- Data realizado: 09/05/2026
- Tempo de desenvolvimento: 50 minutos
- Dificuldade (leetcode): Fácil
- Dificuldade (pessoal): Médio
- Tópico trabalhado: Array e Binary Search
- Complexidade (Time/space): O(n) e O(n)

- Resolvi sozinho? (sim / dica / solução): Sozinho, mas com uma dica do ChatGPT para criar o offset
- Resumo da solução/ideia: Pensei rápido em utilizar binary search, mas como nunca tinha implementado, travei um pouco
- Onde travei: Travei em pensar num modo de, quando "sliceado" a lista, ainda "lembrar" dos indices que existiam para retornar o indice real do valor qual estava como target
"""
