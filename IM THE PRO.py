kids = ["jonny", "elemelon", "samantha", "joshy"]
for each_kid in kids:
    if each_kid == "jonny":
        print('Cry noob')
    elif each_kid == "elemelon":
        print('LLLL keed')
    elif each_kid == "samantha":
        print('get good L')
    elif each_kid == "joshy":
        print('imagine being toxic')

legs = list(range(1, 61))
for each_leg in legs: # ==> this is a pro loop -Loop
    print(each_leg ** 2) # ==> represent the things we need - what we need

upperleg = [leg ** 2 for leg in legs]
#This is the what we need loop

print(upperleg)
