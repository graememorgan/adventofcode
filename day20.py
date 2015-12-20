s = 33100000

presents = [0] * (s / 10)

for i in range(1, len(presents)):
  for h in range(i, min(len(presents), i * 51), i):
    presents[h] += i * 11

print min([i for i, v in enumerate(presents) if v >= s])
