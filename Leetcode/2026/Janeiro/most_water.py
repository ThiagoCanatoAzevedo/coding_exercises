def maxArea(height):
    left = 0
    right = len(height)-1
    max_area = 0
    
    while left < right:
        w = right - left
        h = min(height[left], height[right])
        area = w * h
        
        if area > max_area:
            max_area = area
            
        if height[left] < height[right]:
            left+=1
        else:
            right-=1
    
    return max_area
    
maxArea([1,8,6,2,5,4,8,3,7])

"""
Anotações importantes por exercício:
- Nome exercício: Container With Most Water
- Data realizado: 15/01/2026
- Tempo de desenvolvimento: 1h30min
- Dificuldade (leetcode): Médio
- Dificuldade (pessoal): Médio
- Tópico trabalhado: Array e Two Pointers
- Complexidade (Time/space): O(n)/O(1)

- Resolvi sozinho? (sim / dica / solução): Dica para usar Two Pointer do Claude
- Resumo da solução/ideia: Usei two pointer para não ter que fazer todas as combinações possíveis. Posso diminuir a largura, mas mantendo o maior tamanho, sempre acho a maior área
- Onde travei: Travei em entender que deveria ver todas as combinações. Achei, inicialmente, que tinha que pegar apenas do índice do maior valor até o valor em que a área fosse a maior. 
               Porém, desse modo, não estava funcionando
"""
