#Functions with outputs


def format_name():
    """Take a first and last name and format it to return the title case version of the name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         """
    f_name = input("First name: ")
    l_name = input("Last name: ")
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
    
formatted_name = format_name()
print(formatted_name)