# Program to find maximum guest
# at any time in a party
def find_max_guests(entrance, departure) -> None:
    n = len(entrance)
    # Sort arrival and exit arrays
    entrance.sort()
    departure.sort()

    # guests_in indicates number of
    # guests at a time
    guests_in = 1
    max_guests = 1
    time = entrance[0]
    i = 1
    j = 0
    # Similar to merge in merge sort to
    # process all events in sorted order
    while i < n and j < n:
        # If next event in sorted order is
        # arrival, increment count of guests
        if entrance[i] <= departure[j]:
            guests_in += 1
            # Update max_guests if needed
            if guests_in > max_guests:
                max_guests = guests_in
                time = entrance[i]
            # increment index of arrival array
            i += 1
        else:
            guests_in = guests_in - 1
            j += 1

    print("Maximum Number of Guests =", max_guests, "at time", time)


if __name__ == "__main__":
    arrl = [1, 2, 10, 5, 5]
    exit = [4, 5, 12, 9, 12]
    n = len(arrl)
    find_max_guests(entrance=arrl, departure=exit)
