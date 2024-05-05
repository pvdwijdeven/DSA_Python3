LOVE_LANGUAGES = ["words", "acts", "gifts", "time", "touch"]


def love_language(partner, weeks):
    dict_word = {word: 0 for word in LOVE_LANGUAGES}
    for day in range(weeks * 7):
        language = LOVE_LANGUAGES[day % len(LOVE_LANGUAGES)]
        if partner.response(language) == "positive":
            dict_word[language] += 1
    max_word = max(dict_word, key=lambda x: dict_word[x])
    return max_word


import codewars_test as test


@test.it("Sample tests")
def tests():
    import random

    # example class
    class TestPartner:
        def __init__(self, main_lang, weeeks):
            self.main = main_lang
            self.count = weeks * 7

        def response(self, language):
            if self.count == 0:
                print("Too many tries!")
                exit()
            self.count -= 1

            r = random.random()
            if language == self.main:
                if r < 0.85:
                    return "positive"
                else:
                    return "neutral"
            else:  # language != self.main
                if r < 0.15:
                    return "positive"
                else:
                    return "neutral"

    weeks = 6
    partner = TestPartner("words", weeks)
    test.assert_equals(love_language(partner, weeks), "words")

    weeks = 7
    partner = TestPartner("gifts", weeks)
    test.assert_equals(love_language(partner, weeks), "gifts")
