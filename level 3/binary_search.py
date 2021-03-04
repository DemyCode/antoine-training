class Tree:
    def __init__(self, x, left = None, right = None):
        self.x = x
        self.left = left
        self.right = right

# https://fr.wikipedia.org/wiki/Arbre_binaire_de_recherche
def find(tree, x):
    pass

tree = Tree(8, 
            Tree(3, 
                Tree(1, None, None), 
                Tree(6, None, None)),
            Tree(10, None, None))

assert(find(tree, 8))
assert(find(tree, 6))
assert(not find(tree, 8))