# define rabbitRecursion
def rabbit_recursion(n, k):
    if n < 2:  # base case
        return n
    else:  # recursive call
        return rabbit_recursion((n - 1), k) + rabbit_recursion((n - 2), k) * k


# define main
def main():
    f = open('input.txt')  # file stream
    read_in_array = f.readlines()  # read in data
    rabbits = read_in_array[0].split()  # separate data into unique items
    n = int(rabbits[0])  # months
    k = int(rabbits[1])  # generations
    print(rabbit_recursion(n, k))  # display recursive function


# enter program here
if __name__ == "__main__":
    main()
