import sys

M = int(input())
S = [0 for _ in range(21)]
for _ in range(M):
    command = sys.stdin.readline().strip()
    if command[:3] == 'add':
        S[int(command.split()[1])] = 1
    elif command[:3] == 'rem':
        S[int(command.split()[1])] = 0
    elif command[:3] == 'che':
        print(S[int(command.split()[1])])
    elif command[:3] == 'tog':
        num = int(command.split()[1])
        if S[num] == 0:
            S[num] = 1
        else:
            S[num] = 0
    elif command[:3] == 'all':
        S = [0] + [1 for _ in range(20)]
    elif command[:3] == 'emp':
        S = [0 for _ in range(21)]
    