import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)  # <字符，Node>映射
        self.is_word = False  # 标志是否是单词的结尾
class Trie:

    def __init__(self):
        self.root = TrieNode()

    # 向Trie中添加一个新的单词（将word拆成字符letter，依次加入映射）
    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            current = current.children[letter]  # 自动去重
        current.is_word = True
    # 查询单词word是否在Trie中
    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word
    # 查询是否在Trie中有单词以prefix为前缀
    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True

obj = Trie()
word = 'apple'
prefix = 'app'
notPrefix = 'apr'
obj.insert(word)
print(obj.search(word))
print(obj.startsWith(prefix))
print(obj.startsWith(notPrefix))
