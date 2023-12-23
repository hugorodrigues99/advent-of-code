from math import lcm

def solve():
    input = open('puzzle2.txt', 'r').read().splitlines()
    directions = input[0]
    network = input[2:]

    nodes = createNodes(network)

    startNodes = getStartNodes(nodes)
    steps = []
    for node in startNodes:
        steps.append(getStepsToEndNode(node, nodes, directions))

    return lcm(*steps)

def createNodes(network):
    nodes = {}

    for token in network:
        sourceNode = token[:3]
        leftNode = token[7:10]
        rightNode = token[12:15]

        nodes[sourceNode] = (leftNode, rightNode)

    return nodes

def getStartNodes(nodes):
    startNodes = []

    for node in nodes:
        if node[-1] == "A":
            startNodes.append(node)

    return startNodes

def getStepsToEndNode(node, nodes, directions):
    i = 0
    steps = 0
    currentNode = node
    while currentNode[-1] != "Z":
        i = i % len(directions)
        direction = directions[i]

        leftNode, rightNode = nodes[currentNode]
        currentNode = leftNode if direction == "L" else rightNode

        i += 1
        steps += 1

    return steps

res = solve()
print(res)
