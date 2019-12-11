class Node:
    def __init__(self, value):
        self.value = value
        self.path = 0
        self.links = []

    def set_path(self, path):
        self.path = path
    
    def __str__(self):
        return str(self.value)

class Tree:
    def insert(self, n1, n2):
        n1.links.append(n2)
        
    def transverse(self, root):
        for i in root.links:
            self.transverse(i)
            

    def set_paths(self, root, path_val):
        root.set_path(path_val)
        uv = path_val + 1
        for i  in root.links:
            self.set_paths(i, uv)

    def search(self, root, value):
        if root.value == value:
            return True
        
        for i in root.links:
            val = self.search(i, value)
            if val:
                return True
        
        return False


with open("input/input_6.txt") as f:
    cs = f.readlines()

tree = Tree()
root = Node("COM")
node_dict = {"COM": root}

def get_and_set(_dict, val):
    n = _dict.get(val)
    if not n:
        n = Node(val)
        node_dict[val] = n
    return n

for i in cs:
    q = i.strip().split(")")
    n1 = get_and_set(node_dict, q[0])
    n2 = get_and_set(node_dict, q[1])

    tree.insert(n1, n2)

def part1():
    tree.set_paths(root, 0)

    total = 0
    for i in node_dict.values():
        total += i.path

    print(total)


def part2():
    tree.set_paths(root, 0)

    outs = []
    for i in node_dict.values():
        a = tree.search(i , "YOU")
        b = tree.search(i , "SAN")
        if a and b:
            outs.append(i)
    
    req_node = max(outs, key=lambda x: x.path)
    ans = (node_dict["YOU"].path - req_node.path) + (node_dict["SAN"].path - req_node.path) - 2
    print(ans)


part2()