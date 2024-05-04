def decode(s):
    circle = (
        "bdhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIcflxVC5WE94UA1OoD70MkvRuPqHa"
    )
    dict_decode = {
        33: " ",
        6: ",",
        35: ".",
        57: "0",
        52: "1",
        8: "2",
        26: "3",
        49: "4",
        45: "5",
        36: "6",
        56: "7",
        7: "8",
        48: "9",
        34: "?",
        51: "A",
        25: "B",
        44: "C",
        55: "D",
        47: "E",
        5: "F",
        32: "G",
        65: "H",
        38: "I",
        14: "J",
        22: "K",
        11: "L",
        58: "M",
        18: "N",
        53: "O",
        63: "P",
        9: "Q",
        61: "R",
        27: "S",
        29: "T",
        50: "U",
        43: "V",
        46: "W",
        31: "X",
        37: "Y",
        21: "Z",
        0: "a",
        1: "b",
        39: "c",
        2: "d",
        15: "e",
        40: "f",
        23: "g",
        3: "h",
        12: "i",
        16: "j",
        59: "k",
        41: "l",
        19: "m",
        24: "n",
        54: "o",
        4: "p",
        64: "q",
        13: "r",
        10: "s",
        17: "t",
        62: "u",
        60: "v",
        28: "w",
        42: "x",
        30: "y",
        20: "z",
    }
    res = ""
    for char in s:
        if char not in circle:
            res += char
        else:
            res += dict_decode[circle.find(char)]
        circle = circle[1:] + circle[0]
    return res


import codewars_test as test


@test.describe("Sample Test")
def test_group():
    @test.it("Should crack encoded message")
    def test_case2():
        test.assert_equals(decode("atC5kcOuKAr!"), "Hello World!")
