import sys, time

values = [2, 3, 4, -8, 5, 7, -9, 1, -7, 4, 2, -3, 5, 9]
n = len(values)  # Length of list
list1 = []  # List 1 for first mss
list2 = []  # List 2 for next mss
copied = values.copy()  # List holds copied list

index = []
indexes2 = []
left = 0
right = n-1
small_value = -999  # Small Value (Question 2)
counter = 0

#  Function to return sum (start, final)
def summation(listNum, s, f):
    if s == f:
        return listNum[s], (s, f)  # in case the selected index is only one value long

    middle = (s + f) // 2

    return max(summation(listNum, s, middle),
               summation(listNum, middle + 1, f),
               sumIt(listNum, s, middle, f), key=lambda x: x[0])


def sumIt(listNum, s, m, f):

    leftInd = None  # Index for left max range
    rightInd = None  # Index for right max range
    countr1 = 0  # Counter for 1st loop
    countr2 = 0  # Counter for 2nd loop
    r = 0
    l = 0

    for i in range(m + 1, f + 1):
        countr1 = countr1 + listNum[i]
        if countr1 > r:
            r = countr1
            rightInd = i

    for i in range(m, s - 1, -1):
        countr2 = countr2 + listNum[i]

        if countr2 > l:
            l = countr2
            leftInd = i

    return r + l, (leftInd, rightInd)

#  Max segment between left<right<=n as asked in Question 1
if left < right <= n:
    maxSum, index = summation(values, left, right)

    for i in range(index[0], index[1] + 1):

        copied[i] = small_value
        list1.append(values[i])

    print("The initial list is: ", values)
    print("The left and right positions are ", left, "and ", right, "respectively")
    print("the values are", list1)
    print("The sum is", maxSum)

else:
    sys.exit(0)

#  Positions left<right<=n
if left < right <= n:
    maxSum, indexes2 = summation(copied, left, right)
    for i in range(indexes2[0], indexes2[1] + 1):
        list2.append(values[i])

    print("the values of the next maximum subarray sum is", list2)
    print("The max sum is", maxSum)
else:
    sys.exit(0)