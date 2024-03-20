# Function to find maximum number of consecutive steps
# to gain an increase in altitude with each step.
def max_climbing_steps(arr) -> int:
    steps = 0
    max_steps = 0
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            steps += 1
        else:
            max_steps = max(steps, max_steps)
            steps = 0
    return max(max_steps, steps)


if __name__ == "__main__":
    arr = [1, 2, 3, 1, 2, 3, 4, 5, 6]
    print(max_climbing_steps(arr=arr))
