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


# --- М-е-д-л-е-н-н-е-е ---
line = input()
for i in range(len(line)):
    print(line[i] * (i + 1), end='')


# --- С-л-о-в-о и-з б-у-к-в ---
word = ''
for i in range(int(input())):
    line = input()
    if i + 1 <= len(line):
        word += line[len(line) - 1 - i]
    else:
        word = ''
        break
if word:
    print(word)
else:
    print(None)



# --- Н-а-и-б-о-л-ь-ш-е-е п-р-о-и-з-в-е-д-е-н-и-е ---
n = input()
max_res = 0
for i in range(4, 1000):
    res = int(n[i - 4]) * int(n[i - 3]) * int(n[i - 2]) * int(n[i - 1]) * int(n[i])
    max_res = max(max_res, res)
print(max_res)



# --- П-р-о-п-и-с-н-ы-е с-т-р-о-ч-н-ы-е ---
letter = input()
if 65 <= ord(letter) <= 90:
    print(chr(ord(letter) + 32))
else:
    print(chr(ord(letter) - 32))



# --- С-л-о-в-а ---
line = input()
for i in range(len(line)):
    if line[i] != ' ':
        print(line[i], end='')
    else:
        print()
