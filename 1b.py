with open("input1a.txt", 'r') as f:
# with open("test1a.txt", 'r') as f:
    lines = [line.rstrip('\n') for line in f]

moves = [int(turn[1:]) if turn[0] == "R" else -int(turn[1:]) for turn in lines]
moves = [(turn % 100, turn // 100) if turn > 0 else (turn % -100, turn // -100) for turn in moves]
dial = 50
password = 0
for turn, rots in moves:
    result = dial + turn
    password += rots
    if result > 100 or (result < 0 and dial > 0):
        password += 1
    dial = (dial + turn) % 100
    if dial == 0:
        password += 1
print(password)
