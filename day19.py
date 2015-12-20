reactions = (("Al", "ThF"), ("Al", "ThRnFAr"), ("B", "BCa"), ("B", "TiB"), ("B", "TiRnFAr"), ("Ca", "CaCa"), ("Ca", "PB"), ("Ca", "PRnFAr"), ("Ca", "SiRnFYFAr"), ("Ca", "SiRnMgAr"), ("Ca", "SiTh"), ("F", "CaF"), ("F", "PMg"), ("F", "SiAl"), ("H", "CRnAlAr"), ("H", "CRnFYFYFAr"), ("H", "CRnFYMgAr"), ("H", "CRnMgYFAr"), ("H", "HCa"), ("H", "NRnFYFAr"), ("H", "NRnMgAr"), ("H", "NTh"), ("H", "OB"), ("H", "ORnFAr"), ("Mg", "BF"), ("Mg", "TiMg"), ("N", "CRnFAr"), ("N", "HSi"), ("O", "CRnFYFAr"), ("O", "CRnMgAr"), ("O", "HP"), ("O", "NRnFAr"), ("O", "OTi"), ("P", "CaP"), ("P", "PTi"), ("P", "SiRnFAr"), ("Si", "CaSi"), ("Th", "ThCa"), ("Ti", "BP"), ("Ti", "TiTi"), ("e", "HF"), ("e", "NAl"), ("e", "OMg"))

result = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"

p = set()

for reactant, product in reactions:
  for i in range(len(result)):
    if result[i:i + len(reactant)] == reactant:
      p.add(result[:i] + product + result[i + len(reactant):])

print len(p)

attempts = set()

reactions = [(b, a) for a, b in reactions]
reactions = sorted(reactions, key = lambda x: len(x[0]), reverse = True)

# this was an attepmt at a recursive greedy brute force solution
def recurse(n, result):
  global attempts
  #print n, result
  if result in attempts:
    return False
  if result == "e":
    print n
    return True
  for product, reactant in reactions:
    if product in result:
      if recurse(n + 1, result.replace(product, reactant, 1)):
        return True
  attempts.add(result)
  return False

from re import findall

# the better observation is that all reactions take the form:
# E -> EE
# E -> ERnAr, ERnEYEAr, ERnEYEYEAr
# where E is any (not necessarily repeated) element
#
# this means there must be only one solution.  Rn and Ar must
# come in pairs, so they can just be discarded. Y only acts a a
# separator between elements.  hence, after removing Rn, Ar, and Y,
# each reaction only adds 1 + (number of Ys) elements.

print len(findall("[A-Z]", result)) - len(findall("Rn|Ar", result)) - 2 * len(findall("Y", result)) - 1

recurse(0, result)
