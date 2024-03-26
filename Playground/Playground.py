def minimumPlatform(self, n, entrance, departure):

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

        return max_guests
