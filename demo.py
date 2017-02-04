"""
this program is meant to demonstrate the use of git as a version control
system. The methods below are trivial by nature and may be blank for the
purpose of said demonstration.

author: elias garcia
veresion: 3.2.17
"""

import arrow


def print_list():
    """
    * DEVELOPMENT FEATURE, MAY NOT WORK *
    creates and prints a list of integers using the range() std function and
    list comprehension
    """
    list = [x for x in range(POTATO)]

    print(list)


def print_date_today():

    """
    This doesn't print right...
    """
    print("The date today is ".format(arrow.now().format("YYYY-MM-DD")))

    # what about the format? don't we typically put year last?


def print_names():
    """
    this prints names
    """
    print("Will, Austin, Isaac, and Elias.")


def main():
    """
    main method
    """

    print("Hello, world! Here's a list of the names of our group!")
    print_names()
    print_date_today()


if __name__ == "__main__":
    main()
