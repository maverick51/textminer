import re


def words(my_text):
    """Splits a string up into separate words and returns each word as a list."""
    my_list = re.split(r"\s", my_text)
    return my_list


def phone_number(my_text):
    """Return a dictionary of area code and number from a given phone number."""
    my_dict = {"area_code": "", "number": ""}
    temp_list_with_string = [my_text]

    if len(my_text) < 8:
        my_dict = None
        return my_dict
    else:
        phone_num_with_possible_area_code = r"(?:\(?(\d{3})\)?[\-\.]?\s*)?(\d{3})[\-\.]?(\d{4})"
        for num in temp_list_with_string:
            match = re.search(phone_num_with_possible_area_code, num)
            match_groups = match.groups()
        temp_area_code = match_groups[0]
        temp_number = match_groups[1] + '-' + match_groups[2]
        my_dict["area_code"] = temp_area_code
        my_dict["number"] = temp_number
        return my_dict


def money(my_text):
    """Return a dictionary of currency and amount from a given dollar amount."""
    my_dict = {"currency": "$", "amount": 0.00}
    my_string = ""
    temp_dollar = re.findall(r"\A[$]", my_text)
    temp_amount = re.findall(r"[^$]", my_text)
    print(temp_dollar)
    print(temp_amount)
    if ',' not in temp_amount:
        my_string = my_string.join(temp_amount)
        my_string_into_float = float(my_string)
        my_dict["amount"] = my_string_into_float
        print(my_dict["amount"])
    else:
        new_string_list = []
        for i in temp_amount:
            if i != ',':
                new_string_list.append(i)
        my_string = my_string.join(new_string_list)
        my_string_into_float = float(my_string)
        my_dict["amount"] = my_string_into_float
        print(my_dict["amount"])
    return my_dict


def zipcode(my_text):
    """Return a dictionary of zipcode and plus4 from a given zip code."""
    my_dict = {"zip": "", "plus4": ""}
    if len(my_text) == 5:
        my_dict["zip"] = my_text
        my_dict["plus4"] = None
    else:
        temp_zip = re.split('-', my_text)
        my_dict["zip"] = temp_zip[0]
        my_dict["plus4"] = temp_zip[1]
    print(my_dict["zip"])
    print(my_dict["plus4"])
    return my_dict


if __name__ == '__main__':
    """Run from here if file run directly."""
    print(zipcode("50583"))
