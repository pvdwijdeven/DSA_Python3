def get_pos(datex) -> list[tuple[int, str]]:
    pos = []
    date_s = datex.split("-")
    if int(date_s[1]) <= 12:
        pos.append((datex, ""))
    if int(date_s[2]) <= 12 and date_s[1] != date_s[2]:
        pos.append(("-".join([date_s[0], date_s[2], date_s[1]]), "inv"))
    pos = list([(int(p[0].replace("-", "")), p[1]) for p in pos])
    return pos


def check_date(record) -> int:
    correct = 0
    date1: list[tuple[int, str]] = get_pos(record[0])
    date2: list[tuple[int, str]] = get_pos(record[1])
    inverted = False
    for d1 in date1:
        for d2 in date2:
            if d1[0] < d2[0]:
                if d1[1] == "inv" or d2[1] == "inv":
                    inverted = True
                correct += 1
    if correct == 1:
        if inverted:
            return 1
        else:
            return 0

    return 2


def check_dates(records) -> list[int]:
    res: list[int] = [0, 0, 0]
    for record in records:
        res[check_date(record)] += 1
    return res


import codewars_test as test


@test.describe("Sample test")
def tests():

    records = [
        ["2015-04-04", "2015-05-13"],  # correct
        ["2013-06-18", "2013-08-05"],  # correct
        ["2001-02-07", "2001-03-01"],  # correct
        ["2011-10-08", "2011-08-14"],  # recoverable
        ["2009-08-21", "2009-04-12"],  # recoverable
        ["1996-01-24", "1996-03-09"],  # uncertain
        ["2000-10-09", "2000-11-20"],  # uncertain
        ["2002-02-07", "2002-12-10"],
    ]  # uncertain

    test.assert_equals(check_dates(records), [3, 2, 3])
