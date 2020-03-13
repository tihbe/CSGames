import string
import numpy as np
import z3

dimension = 4
v = z3.Ints(' '.join(string.ascii_lowercase[:dimension**2]))
v = np.asarray(v).reshape(dimension, dimension)

s = z3.Solver()
for xij in v.flatten():
    s.add(z3.And(0 <= xij, xij <= 9))

answer = z3.Int("answer")
s.add(z3.And(answer >= 0, answer <= 9*dimension**2))

for i in range(dimension):
    s.add(z3.Sum(v[i, :dimension].tolist()) == answer)
    s.add(z3.Sum(v[:dimension, i].tolist()) == answer)

s.add(z3.Sum(v.diagonal().tolist()) == answer)
s.add(z3.Sum(np.fliplr(v).diagonal().tolist()) == answer)

count = 0
while s.check() == z3.sat:
    m = s.model()
    count += 1
    s.add(z3.Or([f()!=m[f] for f in m.decls() if f.arity() == 0]))

print(count)