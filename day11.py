from re import search

s = "hxbxwxba"
# for part 2:
#s = "hxbxxyzz"

def intToBase(n, b):
  digits = []
  while n:
    digits.append(int(n % b))
    n = n / b
  return digits[::-1]

password = sum([(ord(d) - ord('a')) * 26**i for i, d in enumerate(s[::-1])])

while True:
  password += 1
  string = "".join([chr(ord('a') + d) for d in intToBase(password, 26)])

  if search("|".join([chr(ord('a') + i) + chr(ord('b') + i) + chr(ord('c') + i) for i in range(24)]), string) and search(r"(.)\1.*(.)\2", string) and not search("[iol]", string):
    print string
    break

