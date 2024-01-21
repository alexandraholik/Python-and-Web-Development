"""
Research how to document your python code using Docstrings and what are the different formats for Doctstrings.
Choose one and stick with it. Hint: : https://devguide.python.org/documenting/
    - Plaintext Docstrings
    - reStructuredText Docstrings
    - Google Style Docstrings
    - NumPy Style Docstrings

Research how python deals with multiple inheritance and why it is not a great idea to use it.
    - Python allows multiple inheritance. A class can inherit from multiple parent classes.
    - Comes with potential issues
        1. MRO(Method resolution order)
            - Nor sure which method to call when a method with the same name exists
        2. Complex code
            - Hurts readability
        3. Hard to maintain

Research the concept of composition vs inheritance.

"""

"""
Exercises
For all exercises, use unit tests (using pytest) make use of functions, and separation of concerns. 
You are encouraged to use GitHub, make one commit per test, and another for the code that passes that test. 
Make a push every time you stop working. Use the pythonic way of coding and follow the PEP8 naming conventions. 
Furthermore, include documentation in the form of Docstrings.
"""

"""
Write a program, using object oriented programming, that asks the users how old they are and returns an answer 
indicating if the users are old enough to vote and how many years are there until they can retire (assume at age 65).
"""
class Person:
    def __init__(self, age):
        self.age = age

#    def can_vote(self):
#        return self.age >= 18

    def can_vote(self, age_requirement = 18):
        """Returns True if older than voting age."""
        return self.age >= age_requirement = 18

    def year_until_retirement(self):
        """Returns the remaining years left until retirement age, 65."""
        return max(65 - self.age, 0)

    def pre_retirement(self):
        """Returns the remaining years left until preretirement age, 60."""
        if self.age < 60:
            return str(60 - self.age)
        elif self.age < 65:
            return str((self.age - 60) * 8) + "%"
        else:
            return "100%"

    def legal_drinking_age(self, age_requirement = 18):
        """Returns True if older than drinking age."""
        return self.age >= age_requirement


if __name__ == "__main__":
    person = Person(19)
    print(person.can_vote())

