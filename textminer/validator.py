import re


def binary(my_text):
    """Checks to see if text is binary and returns True if it is and False otherwise."""
    pattern = r"(^[0-1]+$)"
    result = re.search(pattern, my_text)
    if result:
        return True
    else:
        return False


def binary_even(my_text):
    """Checks to see if binary input is even and returns True if it is and False otherwise."""
    pattern = r"(^[0-1]+[0]$)"
    result = re.search(pattern, my_text)
    if result:
        to_return = True
    else:
        to_return = False
    return to_return


def hex(my_text):
    """Checks to see if the text is hex and returns True if is is and False otherwise."""
    pattern = r"(^[0-9A-Fa-f]+$)"
    result = re.search(pattern, my_text)
    if result:
        return True
    else:
        return False


def word(my_text):
    """Checks to see if the text is a string and returns True if it is and False otherwise."""
    pattern = r"(^[A-z0-9\-]+[A-z]+$)"
    result = re.findall(pattern, my_text)
    if len(result) > 0:
        return True
    else:
        return False


def words(my_text, count=0):
    """Checks to see if the text is a string and returns True if is is and False
    otherwise with optional word count."""
    pattern = r"(^[A-z0-9\-]+[A-z]+$)"
    result = re.findall(pattern, my_text)
    if len(result) > 0:
        if count == len(result):
            to_return = True
        else:
            to_return = False
    else:
        to_return = False
    return to_return


def phone_number(my_text):
    """Checks if a proper phone number is in the text and returns True and False otherwise."""
    pattern = r"(?:\(?(\d{3})\)?[\-\.]?\s*)?(\d{3})[\-\.]?(\d{4})"
    result = re.search(pattern, my_text)
    if result:
        return True
    else:
        return False


def money(my_text):
    """Checks if proper money pattern is in the text and returns True and False otherwise."""
    pattern = r"(^\${1}\d+(?:\,\d{3})?(?:\,\d{3})?(?:\.\d{2})?$)"
    result = re.search(pattern, my_text)
    if result:
        return True
    else:
        return False


def zipcode(my_text):
    """Checks if proper formatted zipcode is in the text and returns True and False otherwise."""
    pattern = r"(^\d{5}(?:\-\d{4})?$)"
    result = re.search(pattern, my_text)
    if result:
        return True
    else:
        return False


def date(my_text):
    """Checks if proper date format is given in the text and returns True and False otherwise."""
    pattern = r"(^\d{1,4}[\-/]{1}\d{1,2}[\-/]{1}\d{2,4}$)"
    result = re.search(pattern, my_text)
    if result:
        return True
    else:
        return False


if __name__ == '__main__':
    """Run from here if file run directly."""
    print(date("2015"))
