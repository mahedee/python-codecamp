import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age




person = Person(
    "Md. Mahedee Hasan",
    "Jewel",
      datetime.date(1984, 4, 07), # year, month, day
      "Jatrabari, Dhaka",
      "01919191879",
      "mahedee@gmail.com"
)

print(person.name)
print(person.email)
print(person.age())