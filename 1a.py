with open("input1a.txt", 'r') as f:
    lines = [line.rstrip('\n') for line in f]

moves = [int(turn[1:]) if turn[0] == "R" else -int(turn[1:]) for turn in lines]
dial = 50
password = 0
for move in moves:
    dial = (dial + move) % 100
    if dial == 0:
        password += 1
print(password)