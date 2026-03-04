from sys import stdin

instances = int(input())
cases = list(map(lambda y: y, stdin.readlines()))

for i in range(0, instances*3, 3):
    print(f"Instancia {int(i/3 + 1)}")
    team1, team2 = 0, 0
    idx_mistake_t1, idx_mistake_t2 = None, None
    
    for j in range(len(cases[i])):
        if cases[i][j] == cases[i + 1][j]: 
            team1 += 1
        else: 
            if idx_mistake_t1 is None:
                idx_mistake_t1 = j

        if cases[i][j] == cases[i + 2][j]: 
            team2 += 1
        else: 
            if idx_mistake_t2 is None:
                idx_mistake_t2 = j

        if idx_mistake_t1 is not None and idx_mistake_t2 is not None:
            if idx_mistake_t1 == idx_mistake_t2:
                idx_mistake_t1 = None
                idx_mistake_t2 = None

    if team1 > team2:
        print("time 1\n")
    elif team2 > team1:
        print("time 2\n")

    elif idx_mistake_t1 is not None or idx_mistake_t2 is not None:
        if idx_mistake_t1 > idx_mistake_t2:
            print("time 1\n")
        elif idx_mistake_t2 > idx_mistake_t1:
            print("time 2\n")
    else:
        print("empate\n")