def solve():
    input = open('puzzle1.txt', 'r').read().splitlines()
    directions = input[0]
    network = input[2:]

    nodes = createNodes(network)

    currentNode = "AAA"
    i = 0
    steps = 0
    while currentNode != "ZZZ":
        i = i % len(directions)
        direction = directions[i]

        leftNode, rightNode = nodes[currentNode]
        currentNode = leftNode if direction == "L" else rightNode

        i += 1
        steps += 1

    return steps

def createNodes(network):
    nodes = {}

    for token in network:
        sourceNode = token[:3]
        leftNode = token[7:10]
        rightNode = token[12:15]

        nodes[sourceNode] = (leftNode, rightNode)

    return nodes

res = solve()
print(res)
