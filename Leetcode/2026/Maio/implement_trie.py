class Trie:
    def __init__(self):
        self.struct = []

    def insert(self, word: str) -> None:
        self.struct.append(word)
        
    def search(self, word: str) -> bool:
        return True if word in self.struct else False
     
    def startsWith(self, prefix: str) -> bool:
        for i in self.struct:
            if i.startswith(prefix):
                return True
        
        return False
        
trie = Trie();
trie.insert("apple");
trie.search("apple");   
trie.search("app");     
trie.startsWith("app"); 
trie.insert("app");
trie.search("app");     


"""
Anotações importantes por exercício:
- Nome exercício: Implement Trie (Prefix Tree)
- Data realizado: 19/05/2026
- Tempo de desenvolvimento: 20 minutos
- Dificuldade (leetcode): Medium
- Dificuldade (pessoal): Easy
- Tópico trabalhado: Hash Table, String, Design e Trie
- Complexidade (Time/space): 

- Resolvi sozinho? (sim / dica / solução):
- Resumo da solução/ideia:
- Onde travei:
"""
