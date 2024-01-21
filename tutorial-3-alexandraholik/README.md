# EBS2070 - Python and Web Design - Tutorial 2

# OOP Python Programming Exercises

## General information

This set of exercises is to solved individually or in a group, before
the tutorial. The subjects of the exercises are meant to help you gain
proficiency in programming with Python.

You are strongly encouraged to [prepare the material]{.underline}
individually or in study groups, in the form of slides or other forms
that can be used to discuss your results with your colleagues.

Research subjects (e.g. list comprehension) but try to not search for
the solution of the exercises. If you use any code from the internet,
please acknowledge it correctly and pay attention to the license.

The tutorial will start with a pre-discussion of which material and
exercises are discussed. If you have any questions about exercises that
were not discussed in the tutorial, please use the discussion board.

The goal of this tutorial is to discuss problems and solutions
encountered while solving the preparation material and the exercises,
but also any tips and tricks or additional resources on Python
programming. You are encouraged to first discuss the issues with your
colleagues (via discussion board) and then with the tutor.

#### Suggested material

-   [UML diagrams](https://tallyfy.com/uml-diagram/)

-   [Chapter 17 of Beyond the Basic Stuff with
    Python](http://inventwithpython.com/beyond/chapter17.html)

#### Tools

-   UML diagrams tools such as [draw.io](https://app.diagrams.net/),
    [lucidchart](https://www.lucidchart.com/pages/) (requires
    registration) or
    [creately](https://creately.com/lp/uml-diagram-tool/) (requires
    registration).

-   Python 3.6+ [Download and install Python
    vanilla](https://www.python.org/downloads/)

-   PyCharm [Download and install
    PyCharm](https://www.jetbrains.com/pycharm/)

-   [pytest](https://docs.pytest.org/en/latest/)

-   GitHub

#### Concepts in exercises

-   Test-Driven-Development

-   Unit-tests

-   Separation of concerns

-   UML diagrams

-   Classes, inheritance, interface, composition

-   Pythonic OOP

Concepts in programming
=======================

1.  Research how to document your python code using `Docstrings` and
    what are the different formats for Doctstrings. Choose one and stick
    with it. *Hint:* : <https://devguide.python.org/documenting/>

2.  Research how python deals with multiple inheritance and why it is
    not a great idea to use it.

3.  Research the concept of composition vs inheritance.

Development and object-oriented programming in Python
=====================================================

#### Concepts in OOP in Python

1.  Research what is `__init__`, `__self__` and `__str__` in OOP in
    Python.

#### Example

-   Write a program, using object oriented programming, that asks the user for the names of two football teams, and the 
score of one team followed by the score of the other team. Your program should output how many points each team gets (3 
for a win,1 for a draw, 0 if they lose). Write down unit tests, make use of functions and use the concept of separation 
of concerns. Use GitHub. Use the procedural programming (PP) version (i.e. Session 2 solution) as a starting point.

Solutions: files [tests/test_football_exercise.py](./tests/test_football_exercise.py) and [football_exercise.py](football_exercise.py).



#### Exercises

For all exercises, use unit tests (using `pytest`) make use of
functions, and separation of concerns. You are encouraged to use GitHub,
make one commit per test, and another for the code that passes that
test. Make a push every time you stop working. Use the pythonic way of
coding and follow the [PEP8 naming
conventions](https://www.python.org/dev/peps/pep-0008/). Furthermore,
include documentation in the form of `Docstrings`.

1.  Write a program, using object oriented programming, that asks the
    users how old they are and returns an answer indicating if the users
    are old enough to vote and how many years are there until they can
    retire (assume at age 65).

2.  Continue the previous program. Write an extension of the program
    from the previous question to include the possibility to indicate
    also the amount of years to the age of pre-retirement (assumed at
    60), and if already illegible to display the percentage of full
    retirement (assumed at 60% at 60 and growing linearly with each
    year).

3.  Continue the previous program. Write an extension of the program
    from the previous question to include the possibility to indicate
    also if they are legal drinking age.

4.  This exercise is another example of working incrementally. Create a
    program that calculates area and perimeters of different geometric
    shapes, following:

    -   Create a general shape class that only have methods to print
        area and perimeter on the screen.

    -   Add further (sub) classes to shape: `Triangle`, `Square`,
        `Rectangle`, `Circle`.

    -   Create a `Cylinder` class as subclass of `Circle` that you
        created in question 1.

5.  Research the concept of abstract class.

    -   How would you solve the previous exercise using an abstract
        class?

    -   Which implementation makes the most sense for this problem?
        *Hint:* : Would you need to instantiate an object of the class
        shape?

6.  Research the concept of composition. From the 'shapes' exercises,
    how would you use composition to create a class `Square`, and
    `Rectangle` from the class `Triangle`?

7.  Create a `Point` class, with a method `distance_to_origin` to
    calculate the distance from the origin. The class should instantiate
    objects by default in the origin.

8.  Create a `Line` class based on the `Point` class. The `Line` class
    should have a method to calculate the length of the line. Does it
    make more sense to use composition or inheritance and why?

9.  With your group, develop a UML diagram of a game of cards, with the
    following specifications:

    -   Create a *Cards* class that holds multiple cards (not single
        card). Standard playing cards have a rank (ace, two through ten,
        jack, queen and king) and suit (clubs, diamonds, hearts,
        spades). This class should output (print) the cards contained in
        this object. The class should have a method to rank the cards
        (by rank) and (another method) to sort by suit.

    -   Create a *Deck* class. Like in real life, *Cards* are dealt from
        a *Deck*. A *Deck* is a collection of *Cards* that includes some
        methods for shuffling and dealing. Dealing should allow to deal
        several cards or one card at a time.

    -   Create a *Hand* class. A *Hand* is a collection of *Cards* and
        some addition methods to score the hand in way that's
        appropriate to the given game.

        1.  Create methods to score blackjack hands. The objective of
            Blackjack is to accumulate a *Hand* with a total point value
            that is less than or equal to 21. Note that an ace can count
            as 1 or 11, so only one of the aces in a hand can have a
            value of 11, and any other aces must have a value of 1.
            *Hint:* : If there is an ace, consider both separate cases
            until your value goes over 21. This is an obvious test.

    -   Create a game combining *Cards*, *Deck* and *Hand* by creating a
        class to play blackjack. This program will create a *Deck* and a
        *Hand*; it will deal two *Cards* into the *Hand*. While the
        *Hand's* total is soft 16 or less, it will add *Cards*. Finally,
        it will print the resulting *Hand*.
