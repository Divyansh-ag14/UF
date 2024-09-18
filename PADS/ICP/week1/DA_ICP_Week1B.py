# ICP_Week1B: Submission by Divyansh Agarwal

from math import sqrt

def getNumbers():
    nums = []     # start with an empty list

    # loop to get numbers
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = float(xStr)
        nums.append(x)   # add this value to the list
        xStr = input("Enter a number (<Enter> to quit) >> ")
    return nums
    
def mean(nums):
    total = 0.0
    for num in nums:
        total = total + num
    return total / len(nums)
    
def stdDev(nums): # one input
    xbar = mean(nums)
    sumDevSq = 0.0
    for num in nums:
        dev = num - xbar
        sumDevSq = sumDevSq + dev * dev
    return sqrt(sumDevSq/(len(nums)-1))
    
def median(nums):
    nums_copy = nums.copy()
    nums_copy.sort()
    size = len(nums_copy)
    midPos = size // 2
    if size % 2 == 0:
        med = (nums_copy[midPos] + nums_copy[midPos-1]) / 2.0
    else:
        med = nums_copy[midPos]
    return med

def meanStdDev(nums): #new function calls mean() and stdDev()
    return mean(nums), stdDev(nums)
    
def main():
    print("\nThis program computes mean, median and standard deviation.")

    data = getNumbers()
    xbar, std = meanStdDev(data) # call to new function
    med = median(data)

    # formatted output
    print(f"\nThe mean of {data} is {xbar:.3f}!")
    print(f"The standard deviation of {data} is {std:.3f}!")
    print(f"The median of {data} is {med:.3f}!")

if __name__ == '__main__':
    
    # infinite choice loop
    choice = "yes"
    while choice.lower()=="yes":
        main()
        choice = input("\nDo you want to repeat? (yes or no)? ")
    print("\nThank you! Goodbye!")
