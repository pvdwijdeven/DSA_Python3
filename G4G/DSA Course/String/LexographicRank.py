# A O(n) solution for finding rank of string
MAX_CHAR = 256

# all elements of count[] are initialized with 0
count = [0] * (MAX_CHAR + 1)


# A utility function to find factorial of n
def fact(n):
    return 1 if (n <= 1) else (n * fact(n - 1))


# Construct a count array where value at every index
# contains count of smaller characters in whole string
def populate_and_increase_count(str):
    for i in range(len(str)):
        count[ord(str[i])] += 1

    for i in range(1, MAX_CHAR):
        count[i] += count[i - 1]


# Removes a character ch from count[] array
# constructed by populateAndIncreaseCount()
def update_count(ch):

    for i in range(ord(ch), MAX_CHAR):
        count[i] -= 1


# A function to find rank of a string in all permutations
# of characters
def find_lexographic_rank(str):
    len1 = len(str)
    mul = fact(len1)
    rank = 1

    # Populate the count array such that count[i]
    # contains count of characters which are present
    # in str and are smaller than i
    populate_and_increase_count(str)

    for i in range(len1):
        mul = mul // (len1 - i)

        # count number of chars smaller than str[i]
        # from str[i+1] to str[len-1]
        rank += count[ord(str[i]) - 1] * mul

        # Reduce count of characters greater than str[i]
        update_count(str[i])

    return rank


if __name__ == "__main__":
    # Driver code
    str = "string"
    print(find_lexographic_rank(str))
