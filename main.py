import chem_parser as cp


if __name__ == '__main__':
    print("Welcome to the chemical equation balancer")
    print("Please enter the chemical equation you want to balance")
    equation = input("Enter the equation: ")
    balanced_equation = cp.balance_equation(equation)
    print("Balanced equation: ", balanced_equation)