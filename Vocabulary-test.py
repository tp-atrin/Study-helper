import random
right_c = 0
counter = 0
myfile = open("data.txt", 'r')
data_dict = {}
for line in myfile:
    k, v = line.strip().split(':')
    data_dict[k.strip()] = v.strip()
myfile.close()

dd_keys = list(data_dict.keys())
count = int(input("How many time?"))
counter += count
for i in range(count):
    x = random.randint(0,33)
    print(dd_keys[x])
    answer = input("")
    if answer == data_dict[dd_keys[x]]:
        print("*-------correct-------*")
    else:
        print("*-------wrong-------*")



dd_values = list(data_dict.values())
count = int(input("How many time?"))
counter += count
for i in range(count):
    x = random.randint(0,33)
    print(dd_values[x])
    answer = input("")
    if dd_keys.index(dd_keys[x]):
        print("*-------correct-------*")
        right_c += 1
    else:
        print("*-------wrong-------*")
def Note(right_c, counter):
    print("Your point is : " + str(((counter-(counter-right_c))/counter)*100))

Note(right_c,counter)