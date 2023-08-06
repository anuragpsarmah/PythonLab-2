#append(), inser(), extend()

myDomain = ["User Profile", "Health Metrics", "Exercise Log", "Nutrition Log", "Fitness Goal"]
print("Original: ", myDomain)
myDomain.append("Health Assessment")
print("Appended: ", myDomain)
myDomain.insert(2, "Wellness Dashboard")
print("Inserted: ", myDomain)
extended_list = ["Meal Plan", "Activity Tracker", "Workout Routine"]
myDomain.extend(extended_list)
print("Extended: ", myDomain, "\n")



#SWAPPING

myList = [x for x in range(21) if x%2 == 0]
print("Original: ", myList)
myList[0], myList[len(myList)-1] = myList[len(myList)-1], myList[0]
print("Swapped: ", myList, "\n") 



#SUM OF DIGITS

myList = [x for x in range(21) if x%2 == 0]
sum = sum(myList)
print("Sum of list elements = ", sum,"\n")



#SMALLEST ELEMENT

anyList = [2,5,3,7,6,1,8,9,4,0,-1]
min = anyList[0]
for x in anyList:
    if(x<min): min = x
print("Minimum: ", x, '\n')



#SORT DICTIONARY BASED ON KEY

myDict = my_dict = {'b': 2, 'a': 1, 'd': 4, 'c': 3}
sorted_dict = dict(sorted(my_dict.items()))
print("Original: ", my_dict)
print("Sorted: ", sorted_dict, '\n')



#SUM OF VALUES

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
count = 0
for key in my_dict:
    count += my_dict[key]
print("Sum of values = ", count, '\n')



#LAMDA FUNCTION

my_dict = {'c': 8, 'a': 4, 'b': 10, 'd': 6}

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Original Dictionary:", my_dict)
print("Sorted Dictionary:", sorted_dict)