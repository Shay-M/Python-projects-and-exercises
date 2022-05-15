# Given an array A[] and a number x, check for pair in A[] with sum as x (aka Two Sum)

A = [2, 1, 5, 3]
n = 4  # 3+1


def printPairs(arr, arr_size, sum):

    # Create an empty hash map, using an hashmap allows us to store the indices
    # Time Complexity: O(n)

    hashmap = {}

    for i in range(0, arr_size):
        temp = sum - arr[i]
        if (temp in hashmap):
            print(
                f'Pair with given sum {sum} is ({temp},{arr[i]}) at indices ({hashmap[temp]},{i})')
        hashmap[arr[i]] = i

    print(hashmap)


printPairs(A, len(A), n)


# ----------------------------------------------------------------
#  The idea is to count the elements with remainders when divided by x,
#  i.e 0 to x-1, each remainder separately. Suppose we have x as 6,
#  then the numbers which are less than 6 and have remainders which add up to 6
#  gives sum as 6 when added. For example, we have elements,
#  2,4 in the array and 2%6 = 2 and 4%6 =4, and these remainders add up to give 6.
#  Like that we have to check for pairs with remainders (1,5),(2,4),(3,3).
#  if we have one or more elements with remainder 1 and one or more elements with remainder 5,
#  then surely we get a sum as 6. Here we do not consider (0,6) as the elements
#  for the resultant pair should be less than 6. when it comes to (3,3)
#  we have to check if we have two elements with remainder 3,
#  then we can say that “There exists a pair whose sum is x”.

# Function to print pairs | Time Complexity: O(n+sum)
def printPairs2(arr, arr_size, sum):

    rem = []

    for i in range(sum):

        # Initializing the rem values with 0's.
        rem.append(0)

    for i in range(arr_size):
        if (arr[i] < sum):

            # Perform the remainder operation only if the element is x, as
            # numbers greater than x can't be used to get a sum x.Updating
            # the count of remainders.
            rem[arr[i] % sum] += 1

    # Traversing the remainder list from start to middle to find pairs
    for i in range(1, sum // 2):
        if (rem[i] > 0 and rem[sum - i] > 0):

            # The elements with remainders
            # i and x-i will result to a
            # sum of x. Once we get two
            # elements which add up to x,
            # we print x and break.
            print("Yes")
            break

    # Once we reach middle of remainder array, we have to do operations based on x.
    if (i >= sum // 2):
        if (sum % 2 == 0):
            if (rem[sum // 2] > 1):

                # If x is even and we have more
                # than 1 elements with remainder
                # x/2, then we will have two
                # distinct elements which add up
                # to x. if we dont have than 1
                # element, print "No".
                print("Yes")
            else:
                print("No")
        else:

            # When x is odd we continue the same process which we did in previous loop.
            if (rem[sum // 2] > 0 and
                    rem[sum - sum // 2] > 0):
                print("Yes")
            else:
                print("No")


A = [2, 1, 5, 3]
n = 4

printPairs2(A, len(A), n)
