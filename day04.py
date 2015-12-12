from hashlib import md5
s = """yzbqklnj"""

for i in xrange(1000000000):
  m = md5("%s%d" % (s, i)).hexdigest()
  if m[:6] == "000000":
    print(i)
    break
