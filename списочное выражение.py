# --- В с-т-р-о-ч-к-у ---
print(' '.join(list(input())))

# --- В с-т-о-л-б-и-к ---
result = [int(x) * "*" for x in input()]
for item in result:
    print(item)

# --- О-п-я-т-ь с-у-м-м-а ц-и-ф-р ---
print(sum([int(x) for x in input()]))

# --- П-о-д-а-р-к-и ф-е-и ---
line = input().split(', ')
gifts = ["flower", "gemstone"]
print('; '.join([gifts[i % 2] for i in range(len(line))]))

# --- З-о-л-у-ш-к-а ---
cereal = input()
result = ' '.join([x for x in input().split() if cereal in x])
print(result)

# --- Д-е-д-л-а-й-н ---
print(' '.join([str(x) for x in range(int(input()), 13)]))

# --- Д-е-д-л-а-й-н 2 ---
print(' '.join([str(x - 2) for x in range(int(input()), 13) if x % 2 == 0]))

# --- С-т-у-п-е-н-ь-к-и ---
n = int(input())
print(', '.join([str(x + 1) if (x + 1) % n != 0 else "БОСИКОМ" for x in range(int(input()))]))

# --- Е-д-и-н-и-ц-ы в к-в-а-д-р-а-т-е ---
n = int(input())
print(', '.join([str(i ** 2) for i in range(1, n + 1) if set(str(i)) == {'1'}]))

# --- К-а-р-е-т-а п-р-е-в-р-а-щ-а-е-т-с-я в т-ы-к-в-у ---
print(' '.join([x[::-1] for x in input().split()]))

# --- С-в-о-б-о-д-а в-ы-б-о-р-а ---
divisor, n, s = input().split()
print(divisor[::-1].join([x for x in s.split(divisor) if len(set(x)) >= int(n)]))