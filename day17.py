from itertools import *

s = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]

def powerset(iterable):
  "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
  s = list(iterable)
  return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

minContainers = min([len(p) for p in powerset(s) if sum(p) == 150])

print len(
  [p
    for p
    in powerset(s)
    if sum(p) == 150 and len(p) == minContainers
  ]
)

