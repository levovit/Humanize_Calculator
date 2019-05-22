import getopt
import sys

from Number_dict import numbers


def convert(s: str) -> str:
    result = "number"
    tmp = int(s[-2::])
    if tmp <= 20:
        result = numbers[str(tmp)]
    elif 20 < tmp < 100:
        result = numbers[s[-2] + "0"] + " " + (numbers[s[-1]] if s[-1] != "0" else "")
    if (len(s) >= 3) and (s[-3] != "0"):
        result = numbers[s[-3]] + " hundred " + (result if result != "zero" else "")
    if (len(s) == 4) and (s[-4] != "0"):
        result = numbers[s[-4]] + " thousand " + (result if result != "zero" else "")
    if (len(s) >= 5) and (s[-5] != "0"):
        tmp = int(s[-5:-3])
        tmp2 = ""
        if tmp < 20:
            tmp2 = numbers[str(tmp)]
        elif 20 < tmp < 100:
            tmp2 = numbers[s[-5] + "0"] + " " + (numbers[s[-4]] if s[-4] != "0" else "")
        result = tmp2 + " thousand " + (result if result != "zero" else "")

    if (len(s) >= 6) and (s[-6] != "0"):
        result = numbers[s[-6]] + " hundred " + (result if result != "zero" else "thousand")

    if (len(s) >= 7) and (s[-7] != "0"):
        result = numbers[s[-7]] + " million " + (result if result != "zero" else "")

    return result.replace("  ", " ")


def fix(string: str) -> str:
    def fix2(s):
        s = s.replace(" ", "")

        if "*" in s:
            tmp = s.split("*", 1)
            return fix(tmp[0]) + " times " + fix(tmp[1])
        if "/" in s:
            tmp = s.split("/", 1)
            return fix(tmp[0]) + " divided " + fix(tmp[1])
        if "=" in s:
            tmp = s.split("=", 1)
            return fix(tmp[0]) + " equals " + fix(tmp[1])
        if "+" in s:
            tmp = s.split("+", 1)
            if tmp[0]:
                return fix(tmp[0]) + " plus " + fix(tmp[1])
            return fix(tmp[1])
        if "-" in s:
            tmp = s.split("-", 1)
            if tmp[0]:
                return fix(tmp[0]) + " minus " + fix(tmp[1])
            return " minus " + fix(tmp[1])

        if s.isdigit():
            return convert(s)
        return "invalid input"
        #  raise SyntaxError("invalid input")

    string = fix2(string)
    string = string.replace("  ", " ")
    if string[-1] == " ":
        string = string[:-1]
    if string[0] == " ":
        string = string[1:]

    if "invalid input" in string:
        return "invalid input"
    return string


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:")
    except getopt.GetoptError:
        print('humanize.py -s "string"')
        sys.exit()

    input_string = ""
    for opt, arg in opts:
        if opt == "-s":
            input_string = arg
        else:
            assert False, "Unknown option"

    print(fix(input_string))

