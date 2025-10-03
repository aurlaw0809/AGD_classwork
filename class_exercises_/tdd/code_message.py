import pytest


def code_mssg(p_message, p_shift):
    p_message = p_message.lower()
    p_coded = ""

    if not isinstance(p_shift, int):
        pytest.raises(TypeError)

    for letter in p_message:
        
        if letter.isalpha():
            num = ord(letter)
            num += p_shift
            if num > ord("z"):
                num -= 26

            if num < ord("a"):
                num += 26

            character = chr(num)
            p_coded += character



        else:
            p_coded += letter

    return p_coded
            