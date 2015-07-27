import re


def words(my_text):
    """Splits a string up into separate words and returns each word as a list."""
    to_return = False
    pattern = r"(^[A-z0-9\-]+[A-z]+$)"
    result = re.findall(pattern, my_text)
    if len(result) > 1:
        to_return = result
    else:
        to_return = None
    return to_return


def phone_number(my_text):
    """Return a dictionary of area code and number from a given phone number."""
    pattern = r"(?:\(?(\d{3})\)?[\-\.]?\s*)?(\d{3})[\-\.]?(\d{4})"
    result = re.findall(pattern, my_text)
    my_dict = {"area_code": "", "number": ""}
    if len(result) < 3:
        my_dict = None
    else:
        my_dict["area_code"] = result[0][0]
        temp_number = result[0][1] + '-' + result[0][2]
        my_dict["number"] = temp_number
    return my_dict


def money(my_text):
    """Returns a dictionary of the $ and currency portion."""
    the_amount = ""
    my_dict = {"currency": "$", "amount": ""}
    pattern = r"(^\${1}\d+(?:\,\d{3})?(?:\,\d{3})?(?:\.\d{2})?$)"
    result = re.findall(pattern, my_text)
    if result:
        result_no_dollar = re.findall(r"[^$]", result[0])
        the_amount = the_amount.join(result_no_dollar)
        my_dict["amount"] = the_amount
        return my_dict
    else:
        return None


def zipcode(my_text):
    """Return a dictionary of zipcode and plus4 from a given zip code."""
    my_dict = {"zip": "", "plus4": ""}
    pattern = r"(^\d{5}(?:\-\d{4})?$)"
    result = re.findall(pattern, my_text)
    if len(result[0]) > 0:
        if len(result[0]) < 6:
            my_dict["zip"] = my_text
            my_dict["plus4"] = None
        else:
            temp_zip = re.split('-', result[0])
            my_dict["zip"] = temp_zip[0]
            my_dict["plus4"] = temp_zip[1]
        return my_dict
    else:
        return None


if __name__ == '__main__':
    """Run from here if file run directly."""
    print(zipcode("26433-3235"))
