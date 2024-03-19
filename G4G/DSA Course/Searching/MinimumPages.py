# Python3 program for optimal allocation of pages


# Utility function to check if
# current minimum value is feasible or not.
def is_possible(arr, n, m, curr_min) -> bool:
    students_required = 1
    curr_sum = 0
    # iterate over all books
    for i in range(n):
        # check if current number of pages are
        # greater than curr_min that means
        # we will get the result after
        # mid no. of pages
        if arr[i] > curr_min:
            return False
        # count how many students are required
        # to distribute curr_min pages
        if curr_sum + arr[i] > curr_min:
            # increment student count
            students_required += 1
            # update curr_sum
            curr_sum = arr[i]
            # if students required becomes greater
            # than given no. of students, return False
            if students_required > m:
                return False
        # else update curr_sum
        else:
            curr_sum += arr[i]
    return True


# function to find minimum pages
def find_minimum_pages(arr, m) -> int | float:
    n = len(arr)
    end = 0
    # return -1 if no. of books is
    # less than no. of students
    if n < m:
        return -1
    end = sum(arr)
    start = max(arr)
    res = float("inf")
    # traverse until start <= end
    while start <= end:
        # check if it is possible to distribute
        # books by using mid as current minimum
        mid = (start + end) // 2
        if is_possible(arr=arr, n=n, m=m, curr_min=mid):
            # update result to current distribution
            # as it's the best we have found till now.
            res = mid
            # as we are finding minimum and books
            # are sorted so reduce end = mid -1
            # that means
            end = mid - 1
        else:
            # if not possible means pages should be
            # increased so update start = mid + 1
            start = mid + 1
    # at-last return minimum no. of pages
    return res


if __name__ == "__main__":
    # Number of pages in books
    arr = [12, 34, 67, 90]
    m = 2  # No. of students
    print("Minimum number of pages = ", find_minimum_pages(arr=arr, m=m))
