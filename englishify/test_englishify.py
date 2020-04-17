from englishify import englishify


def test_case():
    print("This is the test case for question 1")
    print("######################################################")
    # Test the limits of input
    print(englishify(0) == "Zero")
    print(englishify(999999) ==
          "Nine Hundred And Ninety Nine Thousand, Nine Hundred And Ninety Nine")

    # Testing a number that has zeroes behind
    print(englishify(9000) == "Nine Thousand")
    print(englishify(900) == "Nine Hundred")

    # Testing a number that has thousand and hundred at the back
    print(englishify(31447) == "Thirty One Thousand, Four Hundred And Forty Seven")
    print(englishify(55667) == "Fifty Five Thousand, Six Hundred And Sixty Seven")

    # Testing a number that has thousand but no hundred at the back
    print(englishify(909018) == "Nine Hundred And Nine Thousand And Eighteen")
    print(englishify(190004) == "One Hundred And Ninety Thousand And Four")

    # Testing a number that has zeros in between
    print(englishify(5050) == "Five Thousand And Fifty")
    print(englishify(4003) == "Four Thousand And Three")


test_case()
