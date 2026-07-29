N, M = [int(i) for i in input.split()]
cows_height = [int(i) for i in input.split()]
candy_height = [int(i) for i in input.split()]

for i in range(M):
    total_candy_eaten = 0
    for j in range(N):
        eaten += min(candy_height[i], cows_height[j]) - total_candy_eaten
        if eaten <= 0:
            continue
        total_candy_eaten += eaten
        cows_height[j] += eaten
        if total_candy_eaten == candy_height[i]:
            break

for i in range(N):
    print(cows_height[i])
