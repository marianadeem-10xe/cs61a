# Exam Prep
# Q1. Phone Validator

import re
def phone_number(string):
    """
    >>> phone_number("Song by Logic: 1-800-273-8255")
    True
    >>> phone_number("123 456 7890")
    True
    >>> phone_number("1" * 11) and phone_number("1" * 10) and phone_number("1" * 7)
    True
    >>> phone_number("The secret numbers are 4, 8, 15, 16, 23 and 42 (from the TV show Lost)")
    False
    >>> phone_number("Belphegor's Prime is 1000000000000066600000000000001")
    False
    >>> phone_number(" 1122334455 ")
    True
    >>> phone_number(" 11 22 33 44 55 ")
    False
    >>> phone_number("Tommy Tutone's '80s hit 867-5309 /Jenny")
    True
    >>> phone_number("11111111") # 8 digits isn't valid, has to be 11, 10, or 7
    False
    """
    return bool(re.search("[0-9]{3}+[0-9]{4}|[0-9]{3}+[0-9]{3}+[0-9]{4}|[0-9]{1}+[0-9]{3}+[0-9]{3}+[0-9]{4}",
                            string))

# Q2: Email Domain Validator

import re
def email_validator(email, domains):
    """
    >>> email_validator("oski@berkeley.edu", ["berkeley.edu", "gmail.com"])
    True
    >>> email_validator("oski@gmail.com", ["berkeley.edu", "gmail.com"])
    True
    >>> email_validator("oski@berkeley.com", ["berkeley.edu", "gmail.com"])
    False
    >>> email_validator("oski@berkeley.edu", ["yahoo.com"])
    False
    >>> email_validator("xX123_iii_OSKI_iii_123Xx@berkeley.edu", ["berkeley.edu", "gmail.com"])
    True
    >>> email_validator("oski@oski@berkeley.edu", ["berkeley.edu", "gmail.com"])
    False
    >>> email_validator("oski@berkeleysedu", ["berkeley.edu", "gmail.com"])
    False
    """
    pattern = "\w+@"
    for domain in domains:
        pattern = pattern + domain + "|"
    return bool(re.search(pattern, email))

# Q3: Reg Extreme
import re
def all_patterns(n):
    """
    >>> "12" in all_patterns(2)
    True
    >>> r"\d\d" in all_patterns(2)
    True
    >>> "1." in all_patterns(2)
    True
    >>> "1." in all_patterns(1)
    False
    >>> "a" in all_patterns(1)
    False
    >>> ".*" in all_patterns(3)
    True
    """
    numbers = list("0123456789")
    special = list(r"\()[]{}+*?|$^.")
    rest = 
    everything = [""] + numbers + special + rest
    if _________________________:
        _________________________
    else:
        'Use as many lines as necessary'

def reg_extreme(matches, no_matches, n=3):
    """
    >>> pattern = reg_extreme(["11", "12", "13"], ["1", "a"])
    >>> bool(re.search(pattern, "11"))
    True
    >>> bool(re.search(pattern, "12"))
    True
    >>> bool(re.search(pattern, "a"))
    False
    """
    for _____________________:
        'Use as many lines as necessary'

