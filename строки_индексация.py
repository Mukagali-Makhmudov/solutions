# --- Н-а-о-б-о-р-о-т ---
line = input()
for i in range(len(line) - 1, -1, -1):
    print(line[i])


# --- П-о п-о-р-я-д-к-у ---
line = input()
for i in range(1, len(line)):
    if line[i] < line[i - 1]:
        print(line[i])
        break
else:
    print("(:_0_:)")


# --- А-р-и-ф-м-е-т-и-к-а ---
line = input()
res = int(line[0])
i = 1
for i in range(1, len(line), 2):
    if line[i] == "+":
        res += int(line[i + 1])
    else:
        res -= int(line[i + 1])
print(res)


# --- Б-е-з п-о-в-т-о-р-е-н-и-й ---
line = input()
while line:
    if len(line) == len(set(line)):
        print(line)
    line = input()


# --- С-л-е-д-у-ю-щ-и-е т-р-и ---
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter = int(input())
for i in range(4):
    print(abc[(letter - 1 + i) % 26], end='')


# --- М-и-н-и-к-о-м-п-ь-ю-т-е-р ---
s = input()
symbols = set()
for symbol in s:
    symbols.add(ord(symbol))

print(min(symbols), max(symbols), sep=', ')
print('ХВАТИТ' if len(symbols) <= 32 else 'НЕ ХВАТИТ')


