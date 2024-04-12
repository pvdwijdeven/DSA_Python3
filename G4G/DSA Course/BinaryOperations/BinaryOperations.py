# Function to find the first bit from the right that differs between m and n
def pos_of_right_most_diff_bit(m, n) -> int:
    if m == n:
        return -1
    xor_diff = m ^ n
    return get_right_most_set_bit(n=xor_diff)


# Function to get the position of the first bit from the right that is set
def get_right_most_set_bit(n) -> int:
    if n == 0:
        return 0
    bit = 1
    while not n & 1:
        bit += 1
        n = n >> 1
    return bit


# Function to get the value of the first bit from the right that is set
def get_right_most_set_bit_no(n) -> int:
    return n & -(n - 1)


# Function to retreive the kth bit of n
def check_Kth_bit(n, k) -> int:
    return n & (1 << (k - 1)) != 0


# Function to return the count of set bits in n
# Brian Kernighan's algorithm
def count_set_bits(n) -> int:
    res = 0
    while n:
        n = n & (n - 1)
        res += 1
    return res


# Function to return the count
# of set bits in n (32 bit)
def count_set_bits_preprocess(n) -> int:
    bit_set_table_256 = [0] * 256

    def initialize() -> None:
        bit_set_table_256[0] = 0
        for i in range(256):
            bit_set_table_256[i] = (i & 1) + bit_set_table_256[i // 2]

    initialize()
    return (
        bit_set_table_256[n & 0xFF]
        + bit_set_table_256[(n >> 8) & 0xFF]
        + bit_set_table_256[(n >> 16) & 0xFF]
        + bit_set_table_256[n >> 24]
    )


# Function to return sum of count of set bits in the integers from 1 to n.
# See https://www.geeksforgeeks.org/count-total-set-bits-in-all-numbers-from-1-to-n-set-2/
def count_set_bits_1ton(n) -> int:
    total_setbit = 0
    i = 1
    while i <= n:
        total_setbit += ((n + 1) // (2 * i)) * i
        if (n + 1) % (2 * i) > i:
            total_setbit += ((n + 1) % (2 * i)) - i
        i <<= 1
    return total_setbit


# Function to find number of bits needed to be flipped to convert A to B
def count_bits_flip(a, b) -> int:
    n = a ^ b
    res = 0
    while n:
        n = n & (n - 1)
        res += 1
    return res


# Function to find the max number of consecutive ones in bin number
def max_consecutive_ones(n) -> int:
    max_cons_bits = 0
    set_bits = 0
    while n:
        if n & 1:
            set_bits += 1
        else:
            set_bits = 0
        max_cons_bits = max(max_cons_bits, set_bits)
        n = n >> 1
    return max_cons_bits


# Function to find the only number in an array that occurs an odd number of time
def find_only_odd(arr) -> int:
    res = arr[0]
    for element in arr[1:]:
        res ^= element
    return res


# Function to find the only 2 numbers in an array that occurs an odd number of time
def find_two_odds(arr) -> tuple[int, int]:
    xor2 = arr[0]
    set_bit_no = 0
    size = len(arr)
    n = size - 2
    x, y = 0, 0
    # Get the xor of all elements in arr[].
    # The xor will basically be xor of two
    # odd occurring elements
    for i in range(1, size):
        xor2 = xor2 ^ arr[i]
    # Get one set bit in the xor2. We get
    # rightmost set bit in the following
    # line as it is easy to get
    set_bit_no = xor2 & ~(xor2 - 1)
    # Now divide elements in two sets:
    # 1) The elements having the corresponding bit as 1.
    # 2) The elements having the corresponding bit as 0.
    for i in range(size):
        # XOR of first set is finally going to
        # hold one odd occurring number x
        if arr[i] & set_bit_no:
            x = x ^ arr[i]
        # XOR of second set is finally going
        # to hold the other odd occurring number y
        else:
            y = y ^ arr[i]
    return x, y


def is_power_of_two(n) -> bool:
    if n:
        if n & (n - 1) == 0:
            return True
    return False


# Power Set: Power set P(S) of a set S is the set of all subsets of S.
# For example S = {a, b, c} then P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}.
# The following function gives the power set of a string
def get_power_set(inp_str: str) -> list[str]:
    str_len = len(inp_str)
    res = []
    bit_size = 1 << str_len
    for i in range(bit_size):
        sub_str = ""
        for j in range(str_len):
            if (i & (1 << j)) != 0:
                sub_str += inp_str[j]
        res.append(sub_str)
    return res


def swap_bits(n) -> int:
    ev = n & 0xAAAAAAAA
    od = n & 0x55555555
    ev >>= 1
    od <<= 1
    return ev | od


# Function for finding maximum AND value pair
def max_AND(arr) -> int:
    def check_bit(pattern, arr, arr_len) -> int:
        count = 0
        for i in range(0, arr_len):
            if (pattern & arr[i]) == pattern:
                count = count + 1
        return count

    arr_len = len(arr)
    res = 0
    for bit in range(31, -1, -1):
        count = check_bit(pattern=res | (1 << bit), arr=arr, arr_len=arr_len)
        if count >= 2:
            res = res | (1 << bit)
    return res


# This function shows if a number is sparse,
# meaning that is has no consecutive set bits
def is_sparse(n) -> bool:
    set_bits = 0
    while n:
        if n & 1:
            set_bits += 1
            print(set_bits)
        else:
            set_bits = 0
        if set_bits >= 2:
            return False
        n >>= 1
    return True


# This function converts from binary to grey code
def binary_to_grey(n) -> int:
    return n ^ (n >> 1)


def grey_to_binary(n) -> int:
    res = n
    while n > 0:
        n >>= 1
        res ^= n
    return res


if __name__ == "__main__":
    print(get_right_most_set_bit(n=16))
    print(get_right_most_set_bit_no(n=16))
    print(pos_of_right_most_diff_bit(m=8, n=4))
    print(check_Kth_bit(n=5, k=1))
    print(count_set_bits(n=15))
    print(count_set_bits_preprocess(n=15))
    print(count_bits_flip(a=10, b=20))
    print(count_set_bits_1ton(n=17))
    print(max_consecutive_ones(n=222))
    print(find_only_odd(arr=[10, 40, 40, 20, 20, 30, 30, 40, 10, 10, 10]))
    print(is_power_of_two(n=256))
    print(find_two_odds(arr=[10, 10, 20, 30, 30, 40, 50, 50]))
    print(get_power_set(inp_str="abc"))
    print(swap_bits(n=23))
    print(max_AND(arr=[4, 8, 16, 12]))
    print(binary_to_grey(n=10))
    print(grey_to_binary(n=15))
