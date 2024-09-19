def sumN(n: int)-> int:
    sum1 = 0
    for i in range(1, n+1):
        sum1+=i

    return sum1

def sumNCubes(n: int)->int:
    sum1 = 0
    for i in range(1, n+1):
        sum1+= i**3

    return sum1


def main():
    
    print("Let's compute the sum of the cubes for the first N natural numbers!")
    
    n = int(input("Enter a value for N: "))
    
    n_sum = sumN(n)
    n_sum_cube = sumNCubes(n)

    print(f"The sum from 1 to {n} is {n_sum}.")
    print(f"The sum of the cubes of those numbers is {n_sum_cube}.")

if __name__ == "__main__":
    
    choice = "yes"
    
    while choice.lower() == "yes" or choice.lower() ==  "y":
        main()
        choice = input("Try again? (y/n): ")
        print("=========================")

    print("Bye!")