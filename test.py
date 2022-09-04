"""
This is a module document, aka docstring.
Module is a '.py' file.
"""


'''
This is also a comment
'''


# this is a line comment


# integer
this_is_a_int_variable = 0
# string
this_is_a_str_variable = '0'
# boolen
this_is_a_bool_variable = True
# list
this_is_a_list = [1, 2, 3, True, False, [1, 2, 3], this_is_a_int_variable]
# tuple
this_is_a_tuple = 1, 2, 3
this_is_a_tuple_too = (1, 2, 3)
this_is_a_tuple_too_2 = (1,)
this_is_a_tuple_too_3 = 1,
# set
this_is_a_set = {1, 2, 3}
# dictionary
this_is_a_dict_variable = {'a': 1111, 'b': 2222, 'c': 3333}


# define a function with 'function_1' name
#  - it has no argument
def function_1():
    """
    this is a function documentation string.
    """
    
    # 'pass' do nothing
    pass


# define a function with 'function_2' name
#  - it has argument 'name' and 'surname'
def function_2(name, surname):
    """
    this is a function documentation string.
    """
    
    # 'pass' do nothing
    print(name)
    print(surname)


# define a function with 'function_3' name
#  - it has default argumen
def function_3(name='Gago'):
    """
    this is a function documentation string.
    """
    
    print(f'{__name__ = }')
    print(name)


# call function_1
function_1()
function_2('Miqo', 'Ghambaryan')
function_3()
function_3('Mikkkkko')

