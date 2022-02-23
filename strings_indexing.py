# --- Наоборот ---
line = input()
for i in range(len(line) - 1, -1, -1):
    print(line[i])


# --- По порядку ---
line = input()
for i in range(1, len(line)):
    if line[i] < line[i - 1]:
        print(line[i])
        break
else:
    print("(:_0_:)")


# --- Арифметика ---
line = input()
res = int(line[0])
i = 1
for i in range(1, len(line), 2):
    if line[i] == "+":
        res += int(line[i + 1])
    else:
        res -= int(line[i + 1])
print(res)


# --- Без повторений ---
line = input()
while line:
    if len(line) == len(set(line)):
        print(line)
    line = input()


# --- Следующие три ---
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter = int(input())
for i in range(4):
    print(abc[(letter - 1 + i) % 26], end='')


# --- Мини-компьютер ---
s = input()
symbols = set()
for symbol in s:
    symbols.add(ord(symbol))

print(min(symbols), max(symbols), sep=', ')
print('ХВАТИТ' if len(symbols) <= 32 else 'НЕ ХВАТИТ')

