import os                                                         # Using functions
from pathlib import Path                                          # Object-oriented approach

# os module is more syntax intensive
# first method
os.path.dirname(os.path.dirname(os.path.abspath(__file__)))       #################### (Home dir is two levels up)

# second method (long but intuitive)
absolute_path = os.path.abspath(__file__)


def find_parent(abs_path):
    return os.path.dirname(abs_path)


HOME_1 = find_parent(find_parent(absolute_path))                  ##################### (Home dir is two levels up)


# pathlib tries to address that by introducing simpler and more intuitive syntax
HOME_2 = Path(__file__).resolve().parent.parent                   ###################### (Home dir is two levels up)

