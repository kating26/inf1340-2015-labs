#!/usr/bin/env python3

""" Graded Lab #1 for Inf1340, Fall 2015 """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def vowel_or_consonant():
    """
    Exercise: Vowel or Consonant
    Reads a letter of the alphabet from the user. (You can assume that it's
    lowercase.) If the user enters a, e, i, o or u then your program should
    display "vowel". If the user enters y then your program should display
    "sometimes a vowel, sometimes a consonant". Otherwise your program should
    display a message indicating that the letter is a "consonant".
    """

# Katherine Ing's Code
# Student Number: 993128671

letter = raw_input ("Enter a letter ")
vowel_1 = "a"
vowel_2 = "e"
vowel_3 = "i"
vowel_4 = "o"
vowel_5 = "u"
sometimes_vowel = "y"

if letter == sometimes_vowel:
    print ("sometimes a vowel, sometimes a consonant")
elif letter == vowel_1:
    print ("vowel")
elif letter == vowel_2:
    print ("vowel")
elif letter == vowel_3:
    print ("vowel")
elif letter == vowel_4:
    print ("vowel")
elif letter == vowel_5:
    print ("vowel")
else:
    print ("consonant")