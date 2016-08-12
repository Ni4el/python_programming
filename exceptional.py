'''A module for demonstrating exceptions.'''

def convert(s):
    '''Convert to an integer.'''
    try:
        x = int(s)
        return x
    except ValueError:
        print("Conversion failed!")
        x = -1
    return x