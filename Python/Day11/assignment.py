# Assignment 1 — Employee Management ⭐

class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def display_info(self):
        print("\n===== Employee Details =====\n")
        print(f"Name: {self.name}")
        print(f"Id: {self.emp_id}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary}\n")

    def increase_salary(self, amount):
        self.salary += amount
        print(f"{self.name}'s Salary Increased!")
        print(f"New Salary: ${self.salary}")

employee1 = Employee("Harpit", "EMP01", "AI", 45000)
employee2 = Employee("Luffy", "EMP02", "Data Science", 50000)

employee1.display_info()
employee2.display_info()

employee1.increase_salary(5000)

employee1.display_info()


# Assignment 2 — Book Class ⭐⭐

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_book(self):
        print("\n===== Book Details =====\n")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}\n")

    def apply_discount(self, percent):
        discount_price = (self.price * percent)/100
        self.price -= discount_price
        print(f"{self.title}'s New Price: ${self.price}\n")

book1 = Book("To Kill a Mockingbird", "Harper Lee", 500)
book2 = Book("1984", "George Orwell", 399)
book3 = Book("Pride and Prejudice", "Jane Austen", 450)

book1.display_book()
book2.display_book()
book3.display_book()

book1.apply_discount(10)
book2.apply_discount(20)
book3.apply_discount(30)


# Assignment 3 — Mobile Phone ⭐⭐

class MobilePhone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def use_phone(self, hours):
        self.battery -= hours * 10
        if self.battery < 0:
            self.battery = 0
            print(f"Battery: {self.battery}")
            return
        print(f"{self.brand} {self.model}'s remaining battery: {self.battery}%")

    def charge(self):
        self.battery = 100
        print(f"{self.brand} {self.model}'s Battery Fully charged {self.battery}%")

mobile1 = MobilePhone("Oppo", "Reno 7", 100)

mobile1.use_phone(7)
mobile1.charge()


# Assignment 4 — Movie Rating System ⭐⭐⭐

class Movie:
    def __init__(self, movie_name, genre):
        self.movie_name = movie_name
        self.genre = genre
        self.rating = 0

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.rating = rating
        else:
            print("Invalid Rating")

    def display_movie(self):
        print(f"\nMovie: {self.movie_name}")
        print(f"Genre: {self.genre}")
        print(f"Rating: {self.rating}\n")

movie1 = Movie("Interstellar", "Sci-Fi")

movie1.add_rating(5)
movie1.display_movie()



# Assignment 5 — Student Result System ⭐⭐⭐

class Student:
    def __init__(self, name, maths, science, english):
        self.name = name
        self.maths = maths
        self.science = science
        self.english = english
    
    def total_marks(self):
        total = self.maths + self.science + self.english
        return total
    
    def average_marks(self):
        average = self.total_marks()/3
        return average
    
    def grade(self):
        average = self.average_marks()
        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"

        return grade

    def display_result(self):
        print(f"\nName: {self.name}")
        print(f"Total: {self.total_marks()}")
        print(f"Average: {self.average_marks():.2f}")
        print(f"Grade: {self.grade()}\n")

student1 = Student("Harpit", 90, 94, 97)
student1.display_result()