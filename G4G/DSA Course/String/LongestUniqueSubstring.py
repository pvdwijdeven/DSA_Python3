# Here, we are planning to implement a simple sliding window methodology
def longest_unique_substring(string):

    # Creating a set to store the last positions of occurrence
    seen = {}
    maximum_length = 0
    max_word = ""

    # starting the initial point of window to index 0
    start = 0
    for end in range(len(string)):

        # Checking if we have already seen the element or not
        if string[end] in seen:

            # If we have seen the number, move the start pointer
            # to position after the last occurrence
            start = max(start, seen[string[end]] + 1)

        # Updating the last seen value of the character
        seen[string[end]] = end
        if maximum_length < end - start + 1:
            max_word = string[start:end]
            maximum_length = end - start + 1
    return maximum_length, max_word


if __name__ == "__main__":
    string = "geeksforgeeks"
    print("The input string is", string)
    length, max_word = longest_unique_substring(string)
    print("The length of the longest non-repeating character substring is", length)
    print("The longest non-repeating character substring is", max_word)
