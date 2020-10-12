# Challenge
# Your 1 coding problem.

# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


noOfEle = int(input('Enter the number of elements :'))
k = int(input('Enter the value of k:'))
elementList = []
conditionSatisfiedPairs = {}
i = 0
# read writes the element in the list
for x in range(noOfEle):
    elementList.append(int(input('Enter the element to add in list:')))

# check the condition and return true/false
def check(first, second):
    if(first + second == k) :
        print('your K value is :', first + second)
        return True
    else :
        return False

# sends the elements to check the condition
while i <= noOfEle :
    j = i + 1
    while j < noOfEle :
        if(check(elementList[i], elementList[j])) :
            print('Pair equal to your k value is', elementList[i], elementList[j])
            conditionSatisfiedPairs.update({elementList[x] : elementList[j]})
        j = j + 1
    i = i + 1

if(not bool(conditionSatisfiedPairs)) :
    print('No pairs in your list is equal to your K value', k)