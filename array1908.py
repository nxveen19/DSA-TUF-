#Optimal soln to find second largest integer in an array 
arr = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9 ]
def main():
    largest =0
    slargest = -1
    for i in arr:
        if i > largest:
            slargest = largest
            largest = i
        elif i > slargest and i < largest:
            slargest = i
    print(slargest)
            
#check if array is sorted
def isSorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

#remove duplicates from sorted array and give no of unique elements
arr1 = [1,1,2,2,3,3,3]
new_arr = []
# for i in range(len(arr1)-1):
#     if arr1[i] != arr1[i-1]:
#         arr1.append(arr1[i], i)
# print(new_arr)
#OR to modify same array
i=0
for j in range(1, len(arr1)):
    if arr1[j] != arr1[i]:
        i+= 1
        arr1[i] = arr1[j]
arr1 = arr1[0:i+1]
# print(arr1)

#left rotate the array by d plane(commmit)
larr = [1,2,3,4,5,6]
n = len(larr)
D = int(input("Tell about the number of rotations: "))
d = int(D % n)
print(d)
# start1 = larr[1]
while d>0:
    start0 = larr[0]
    for i in range(0, len(larr) - 1):
        larr[i] = larr[i+1]
        i+= 1
    larr[n-1] = int(start0)

    d-=1

print(larr)

