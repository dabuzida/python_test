import math


def requiredTreeLevel(nodeCount):
    roughlyLevel = math.log2(nodeCount)
    return roughlyLevel

print(requiredTreeLevel(16))

