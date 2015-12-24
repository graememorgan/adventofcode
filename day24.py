import itertools, operator

s = map(int, """1;3;5;11;13;17;19;23;29;31;37;41;43;47;53;59;67;71;73;79;83;89;97;101;103;107;109;113""".split(";"))

t = sum(s) / 3 # 4 for part 2

# enumerating combinations automatically picks the smallest quantum entanglement
def valid(weights, level):
  for l in range(1, len(weights)):
    for c in itertools.combinations(weights, l):
        # 1 -> 2 for part 2
        if sum(c) == t and level == 1:
          return True
        if sum(c) == t and valid(list(set(weights) - set(c)), level + 1):
          return reduce(operator.mul, c, 1)

print valid(s, 0)
