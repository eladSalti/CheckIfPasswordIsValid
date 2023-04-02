special_characters = ['!', '@', '#', '%', '^', '&', '*', '(', ')', '_']
def test_check_if_spaces_is_valid(stringinput):
    "In this test we will check if there are any spaces in the password"
    value_bool = True
    if any(char.isspace() for char in stringinput):
        value_bool = False
    assert value_bool == True, "The Password shouldn't contains spaces"

def test_check_if_there_is_less_than_6_characters(stringinput):
    "In this test we will check if the password len is less than 6 characters"
    value_bool = True
    if len(stringinput) < 6:
        value_bool = False
    assert value_bool == True ,"the length should be at least 6 characters"

def test_if_password_contains_at_least_one_number(stringinput):
    "In this test we will check if there is at least one number in the password"
    value_bool = True
    if not any(char.isdigit() for char in stringinput):
        value_bool = False
    assert value_bool == True, 'The Password should have at least one number'

def test_if_password_contains_at_least_one_lower_case(stringinput):
    "In this test we will check if there is at least one lower case in the password"
    value_bool = True
    if not any(char.islower() for char in stringinput):
        value_bool = False
    assert value_bool == True, 'The Password should have at least one lowercase letter'

def test_if_password_contains_at_least_one_upper_case(stringinput):
    "In this test we will check if there is at least one upper case in the password"
    value_bool = True
    if not any(char.isupper() for char in stringinput):
        value_bool = False
    assert value_bool == True, 'The Password should have at least one uppercase letter'

def test_if_password_contains_at_least_one_special_character(stringinput):
    "In this test we will check if there is at least one special character in the password"
    value_bool = True
    if not any(char in special_characters for char in stringinput):
        value_bool = False
    assert value_bool == True, 'The Password should have at least one of the symbols !@#$%^&*()_'
