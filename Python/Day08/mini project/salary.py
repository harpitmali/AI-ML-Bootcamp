def calculate_salary(hours, rate):
    return hours * rate

def calculate_bonus(salary):
    bonus_rate = 0.10 if salary >= 50000 else 0.05
    return salary * bonus_rate

def calculate_tax(salary):
    tax = 0.15 if salary >= 60000 else 0.10
    return salary * tax


def net_salary(hours, rate):
    gross_salary = calculate_salary(hours, rate)
    bonus = calculate_bonus(gross_salary)
    tax = calculate_tax(gross_salary)
    final_salary = gross_salary + bonus - tax

    return gross_salary, bonus, tax, final_salary