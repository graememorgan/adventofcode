from itertools import groupby

s = "1113222113"

def lookandsay(string):
  return "".join(["%d%s" % (len(list(g)), k) for k, g in groupby(string)])

for i in range(50):
  s = lookandsay(s)

print len(s)

