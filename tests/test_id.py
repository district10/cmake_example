import cmake_example as m
# print(m.__file__)

p = m.Pod()
beeds = set()
for _ in range(5):
    beeds.add(id(p.beed()))
print(beeds)
