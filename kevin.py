import random

NUMBER_OF_PORTS = 15
MINIMUM_TIME = 8*NUMBER_OF_PORTS
WAVELENGTH = MINIMUM_TIME*5
unsorted_list = []
for x in range(0,10):
	unsorted_list.append([x,random.randint(MINIMUM_TIME, 300)])
print unsorted_list
unsorted_list.sort(key=lambda x: x[1])
print unsorted_list
for x in range(1,len(unsorted_list)):
	S = sum(map(lambda x: x[1], unsorted_list[0:x]))
	print S
	unsorted_list[x][1] = unsorted_list[x][1] -S
print unsorted_list
S = sum(map(lambda x: x[1], unsorted_list))
print S
unsorted_list[0][1] = unsorted_list[0][1] - MINIMUM_TIME
print "the sorted list: " + str(unsorted_list)
print "the delay: " + str(WAVELENGTH-S)
