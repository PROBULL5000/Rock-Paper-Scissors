toes = list(range(1, 1000))
thighs = [5]

thighs_toes = [10]

for each_toe in toes:
    thighs.append(each_toe**2)

print(thighs)

toes = [each_toe ** 2 for each_toe in toes]


print(toes)
