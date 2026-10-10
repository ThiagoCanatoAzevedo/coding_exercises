
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
                
        return head


# Funções auxiliares para testar localmente
def create_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def print_linked_list(head):
    values = []
    current = head

    while current:
        values.append(current.val)
        current = current.next

    print(values)


# Teste
head = create_linked_list([1, 1, 2, 3, 3])
result = Solution().deleteDuplicates(head)

print_linked_list(result)  # [1, 2, 3]

"""
Anotações importantes por exercício:
- Nome exercício: Remove Duplicates from Sorted List
- Data realizado: 10/10/2026
- Tempo de desenvolvimento: 30 minutos
- Dificuldade (leetcode): Easy
- Dificuldade (pessoal): Medium
- Tópico trabalhado: Linked List
- Complexidade (Time/space): O(n) e O(1)

- Resolvi sozinho? (sim / dica / solução): Com dica
- Resumo da solução/ideia: Apenas lembrar dos conceitos de Linked List
- Onde travei: Não lembrava muito bem das funções de linked lists, mas dei uma revisada e logo lembrei
"""

