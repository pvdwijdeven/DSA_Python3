# User function Template for python3


# Function to find matching decimal representation of a string as on the keypad.
def printNumber(s, n):
    def convertNumber(char):
        if char in "abc":
            return 2
        elif char in "def":
            return 3
        elif char in "ghi":
            return 4
        elif char in "jkl":
            return 5
        elif char in "mno":
            return 6
        elif char in "pqrs":
            return 7
        elif char in "tuv":
            return 8
        else:
            return 9

    res = ""
    for i in range(n):
        res += str(convertNumber(char=s[i]))
    # CODE HERE
