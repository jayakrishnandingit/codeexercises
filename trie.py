class TrieNode(object):
    def __init__(self, data=''):
        self.data = data
        self.children = {}
        self.is_terminal = False

    def __str__(self):
        return '%s' % self.data

    def __repr__(self):
        return '%s' % self.data


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                node = TrieNode(char)
                current.children.update({char: node})
                current = node
            else:
                current = current.children.get(char)
        current.is_terminal = True

    def find(self, word):
        current = self.root
        if not current.children:
            return -1

        for char in word:
            if char not in current.children:
                return -1
            current = current.children.get(char)
        return self.get_all_related(current, word)

    def get_all_related(self, node, prefix=''):
        suggestions = []
        if node.is_terminal:
            suggestions.append(prefix)
        for child in node.children.values():
            suggestions.extend(self.get_all_related(child, prefix + child.data))
        return suggestions

    def display(self):
        print("All the people in my contacts are ", self.get_all_related(self.root))


if __name__ == '__main__':
    contacts = Trie()
    words = [
        "abhishek",
        "sruthi",
        "anoop",
        "ajith",
        "anusree",
        "anusreekumar",
        "manju",
        "manohar",
        "mekha",
        "sasi",
        "damu",
        "mini",
        "ajithkumar",
        "jayakrishnan",
        "jayasankar",
        "jayasreekumar",
        "jayasree"]
    for word in words:
        contacts.insert(word)
    contacts.display()
    print("Find suggestions for anusree => ", contacts.find("anusree"))
    print("Find suggestions for ajith => ", contacts.find("ajith"))
    print("Find suggestions for sasi => ", contacts.find("sasi"))
    print("Find suggestions for jaya => ", contacts.find("jaya"))
    print("Find suggestions for jayas => ", contacts.find("jayas"))
    print("Find suggestions for jayasree => ", contacts.find("jayasree"))
    print("Find suggestions for b => ", contacts.find("b"))