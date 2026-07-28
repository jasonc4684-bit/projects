input = open("shell.in")
read = int(input.readlines())
location = [i for i in range(3)]
counter = [0 for _ in range(3)]

for _ in range(read):
    a, b, g = [int(value) - 1  for value in read.readlines().split()]

    location[a], location[b] = location[b], location[a]
    counter[location[g]] += 1

print(max(counter), file = open("shell.out", "w"))