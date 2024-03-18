# Function to find the first non-repeating character in a string.
def find_first_non_repeating_char(s) -> str:
    dict = {}
    for char in s:
        dict[char] = 0

    for char in s:
        dict[char] += 1

    for char in s:
        if dict[char] == 1:
            return char
    return "$"


if __name__ == "__main__":
    print(find_first_non_repeating_char(s="abcdabcddeefgha"))
