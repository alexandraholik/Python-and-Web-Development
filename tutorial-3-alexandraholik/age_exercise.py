class Person:
    def __init__(self, age):
        self.age = age

    def can_vote(self):
        return self.age >= 18

    def year_until_retirement(self):
        return max(65-self.age, 0)

    def pre_retirement(self):
        if self.age < 60:
            return str(60 - self.age)
        elif self.age < 65:
            return str((self.age - 60) * 8) + "%"
        else:
            return "100%"

    def legal_drinking_age(self, age_requirement=18):
        return self.age >= age_requirement


if __name__ == "__main__":
    person = Person(19)
    print(person.can_vote())

