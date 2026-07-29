N, M = [int(i) for i in input.split()]
cows_height = [int(i) for i in input.split()]
tree_height = [int(i) for i in input.split()]

for i in range(M):
    total_candy_eaten = 0

    for j in range(N):

        eaten += min(tree_height[j], cows_height[j]) - total_candy_eaten
        if eaten <= 0:
            continue
        total_candy_eaten += eaten
        cows_height[j] += eaten
        if total_candy_eaten == tree_height:
            break

for i in range(j):
    print(cows_height[i])