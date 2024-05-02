# print a table containing multiplication tables


for i in range(1, 12):
    for j in range(1, 12):
        result = i * j
        print(result, end="\t")
    print()