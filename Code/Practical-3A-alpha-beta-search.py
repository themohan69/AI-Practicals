tree = [[[5, 1, 2], [8, -8, -9]], [[9, 4, 5], [-3, 4, 3]]]
root = 0
pruned = 0

def children(branch, depth, alpha, beta):
    global tree
    global root
    global pruned
    i = 0
    for child in branch:
        if isinstance(child, list):
            nalpha, nbeta = children(child, depth + 1, alpha, beta)
            if depth % 2 == 1:
                beta = min(beta, nalpha)
            else:
                alpha = max(alpha, nbeta)
            branch[i] = alpha if depth % 2 == 0 else beta
            i += 1
        else:
            if depth % 2 == 0 and alpha < child:
                alpha = child
            if depth % 2 == 1 and beta > child:
                beta = child
        if alpha >= beta:
            pruned += 1
            break
    if depth == root:
        tree = alpha if root == 0 else beta
    return alpha, beta

def alphabeta():
    global tree
    global pruned
    global root
    alpha, beta = children(tree, root, -float('inf'), float('inf'))
    print("(alpha, beta): ", alpha, beta)
    print("Result: ", tree)
    print("Times pruned: ", pruned)
    return alpha, beta, tree, pruned

if __name__ == "__main__":
    alphabeta()
