ordem = 10

for i in range(ordem):
    for j in range(ordem):
        if i + j == ordem - 1:
            print(f"{i,j}")
