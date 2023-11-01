list1 = ["Amjad","Zen","Belal",6,23,12,58,21]
for i in range(0,len(list1)):
	for j in range(i+1,len(list1)):
		if list1[i] >= list1[j]:
			list1[i], list1[j] = list1[j], list1[i]
