import re


def phone_numbers(my_text):
    """Retrieves all phone numbers from a string and returns them."""
    phone_list = re.findall(r"[\(][0-9]{3}[\)][\s][0-9]{3}-[0-9]{4}", my_text)
    return phone_list


def emails(my_text):
    """Retrieves all email addresses from a string and returns them."""
    email_list = \
        re.findall(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:"
                   r"[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", my_text)
    return email_list


if __name__ == '__main__':
    """Run from here if called directly."""
    print(emails("My email address is mav@cox.net and pea@sprouts.org"))
