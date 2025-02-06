# How many ways to run phyton
#1 IDLE OR CMD
#2 Notepad
#3 development platform (like Vs code or PyCharm 0r........)



# DATA type 
#numeric-int,float,complex number ,boolen
#sequence-list , tuple,string,range
#set
#dictionary
#none


#complex numbers

cmp1 = 5 + 3j
cmp2 = 6 - 3j
print(cmp1 + cmp2)

print(cmp1 - cmp2)

print(cmp1 * cmp2)

print(cmp1 / cmp2)

print(cmp1 ** cmp2)
#print(cmp1 // cmp2) #float division doesn't work on complex
#print(cmp1 % cmp2)  # modules doesn't work on complex numbers


bool1 = True

print(bool1)

print(type(bool1))

print(int(bool1))

print(int(False))

#Sequences
#list
list1 = [1,2,3,4,5-4,54 ,'Vineeth','a',[7,9,8]]

print(list1)

print(list1[0])

print(list1[len(list1)-1])

print(list1[-1])

print("Printing......")
print(list1[-1][2])

print("Slicing")

print(list1[0 :5])

print(list1[0 : -1 :2])

print(list1[-4:-8 :-1])


#printing elements one by one
for i in list1:
    print(i)

#tuple
tuple1= (4,5,6,7,2,'vineeth',(5,6,7))

for i in tuple1:
    print(i)

print("Tuble example")

print(tuple1[0])

print(tuple1[0 :5])

print(tuple1[-2:-5:-1])

#range

print("Range")
print(list(range(0,100)))

print(list(range(100 ,0 ,-1)))

print(list(range(100 ,0 ,-3)))

 
 
