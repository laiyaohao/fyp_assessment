# This is to answer the first question in the assessment

def englishify(number):

    # Since the number is in integer form, there is no way of "counting" how many digits
    # Thus, we need to convert it to a string first.
    num_in_str = str(number)
    len_of_num = len(num_in_str)
    
    #create a dictionary of english equivalent from 1 to 9
    zero_to_nine = {"0": "", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", \
        "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}
    ten_to_nineteen = {"10": "Ten", "11": "Eleven", "12": "Twelve", "13": "Thirteen", "14": "Fourteen", "15": "Fifteen", \
        "16": "Sixteen", "17": "Seventeen", "18": "Eightteen", "19": "Nineteen"}
    twe_to_nint = {"2": "Twenty", "3": "Thirty", "4": "Fourty", "5": "Fifty", \
        "6": "Sixty", "7": "Seventy", "8": "Eighty", "9": "Ninety"}
    english = ""
    def twoorless(numbe):
        engl = ""
        if len(numbe) < 2:
            # if numbe == '0':
            #     engl += "Zero"
            # else:
            engl += zero_to_nine[numbe]
        elif numbe[0] == '0':
            engl += zero_to_nine[numbe[1]]
        elif numbe[0] == '1':
            engl += ten_to_nineteen[numbe]
        else:
            engl += twe_to_nint[numbe[0]]
            engl += zero_to_nine[numbe[1]]
        return engl
    def threedigit(numb):
        eng = ""
        # if numb[0] == '0':
        eng += zero_to_nine[numb[0]]
        if eng:
            eng += " Hundred "
        else:
            pass
        lasttwodigits = twoorless(numb[1:])
        if lasttwodigits:
            eng += "And "
        else:
            pass
        # if numb[1] == '1':
        #     eng += ten_to_nineteen[numb]
        # elif numb[1] != '0':
        #     eng += twe_to_nint[numb[1]]
        #     eng += zero_to_nine[numb[2]]
        # else:
            
        #     eng += zero_to_nine[numb[2]]
        eng += lasttwodigits
        return eng
    
    def threeorless(numberr):
        englis = ""
        if len(numberr) <= 2:
            englis += twoorless(numberr)
        elif len(numberr) == 3:
            englis += threedigit(numberr)
        return englis
    
    if num_in_str == '0':
        english += "Zero"
    # elif len_of_num <= 2:
    #     english += twoorless(num_in_str)
    # elif len_of_num == 3:
    #     english += threedigit(num_in_str)
    elif len_of_num <= 3:
        english += threeorless(num_in_str)
    else:
        lastthree = num_in_str[-3:]
        firstn = num_in_str[-len_of_num:-3]
        english += threeorless(firstn)
        english += " Thousand "
        lastthreedigits = threeorless(lastthree)
        if lastthreedigits:
            english += ","
        else:
            pass
        english += lastthreedigits
        

    
    return english       
    # elif len_of_num == 2:


print(englishify(333333))