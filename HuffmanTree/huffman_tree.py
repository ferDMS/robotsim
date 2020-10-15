import json

symbols = []
freq = []
with open('HuffmanTree/ht.json') as json_file:
    ht = json.load(json_file)
    symbols = ht["symbols"]
    freq = ht["freq"]

class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None

def get_huffman_root():#builds the tree and returns root
    node_list = []
    for x in range(len(symbols)-1):
        new_node = Node(freq[x], symbols[x])
        node_list.append(new_node)

    parent_node = []
    parent_node.append(node_list.pop(0))
    root = parent_node[0]

    while len(node_list) > 0 and len(parent_node) > 0:
        if not parent_node[0].data:
            parent_node[0].left = node_list[0]
            if node_list[1]:
                parent_node[0].right = node_list[1]
                parent_node.append(node_list.pop(0))
            parent_node.append(node_list.pop(0))
        parent_node.pop(0)

    return root

def print_huff(root):
    node_order = []
    node_order.append(root)

    while len(node_order) > 0:
        print(node_order[0].freq)
        if node_order[0].left:
            node_order.append(node_order[0].left)
        if node_order[0].right:
            node_order.append(node_order[0].right)
        node_order.pop(0)

def main():
    root = get_huffman_root()
    print_huff(root)

# if __name__ == "__main__":
#     main()

