from collections import defaultdict
class Trie:

    def __init__(self):
        self.trie = defaultdict(list)
        

    def insert(self, word: str) -> None:
        self.trie[word[0]].append(word)

    def search(self, word: str) -> bool:
        if word in self.trie[word[0]]:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        for t in self.trie[prefix[0]]:
            if t.find(prefix) == 0:
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
