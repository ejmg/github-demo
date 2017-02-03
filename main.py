"""
this program is meant to demonstrate the use of git as a version control
system. The methods below are trivial by nature and may be blank for the
purpose of said demonstration.

author: elias garcia
veresion: 3.2.17
"""

import arrow


def print_date_today():

    """
    This doesn't print right...
    """
    print("The date today is".format(arrow.now().format("YYYY-MM-DD")))

    # this could be made better...doesn't year come last normally?

def print_names():

    print("Will, Austin, Isaac, and Elias.")


def main():

    print("Hello, world! Here's a list of the names of our group!")
    print_names()
    print_date_today()


if __name__ == "__main__":
    main()
