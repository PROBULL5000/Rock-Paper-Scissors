for pro in list(range(1, 21)):
    print(pro)

prolist = list(range(1, 10000009))
for p in prolist:
    print(p)

print(min(prolist), max(prolist))
print(sum(prolist))

nooblist = list(range(1, ))
for noob in nooblist:
    print(noob)

for bad in list(range(6, 30)):
    if bad % 6==0:
        print(bad)

kid = list(range(1, 7))
cubekid = []
for each_noob in kid:
    print(each_noob ** 6)

cubekid.append(each_noob ** 6)

cubeleg = [each_noob ** 6 for each_noob in list(range(1, 21))]
print(cubeleg)
