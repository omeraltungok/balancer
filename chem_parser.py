import gaussian as gp
import chem as ch
from fractions import Fraction


def find_least_common_multiple(numbers):
    # find denominators
    denominators = []
    for number in numbers:
        fraction = Fraction(number)
        denominators.append(fraction.denominator)
    lcm = 1

    # Iterate over the numbers
    for number in denominators:
        # Find the greatest common divisor of the current number and the least common multiple
        gcd = find_greatest_common_divisor(number, lcm)

        lcm = (lcm // gcd) * number

    # Return the least common multiple
    return lcm

# recieves two numbers and returns their greatest common divisor
def find_greatest_common_divisor(number1, number2):
    gcd = 1
    min = number1
    if number2 < number1:
        min = number2
    
    for i in range(1, min + 1):
        if number1 % i == 0 and number2 % i == 0:
            gcd = i

    # Return the greatest common divisor
    return gcd

def format_solution(solution_matrix):
    # Initialize an empty list to hold the coefficients
    solution = []

    # Iterate over the solution matrix
    for i in range(len(solution_matrix)):
        # Add the coefficient to the solution list
        solution.append(solution_matrix[i][len(solution_matrix[i]) - 1])

    # Return the solution list
    return solution

def balance_equation(equation):
    # Parse the equation and get the matrix
    left_elements, right_elements = ch.parse_equation(equation)
    elements, matrix = ch.get_matrix(left_elements, right_elements)

    # Apply the Gaussian elimination
    solution_matrix = gp.gauss_eliminate_algorithm(matrix)
    solution = format_solution(solution_matrix)

    lcm = find_least_common_multiple(solution)

    # Multiply each number in the solutions last colomn by the lcm
    col_num = len(solution_matrix[0])
    row_num = len(solution_matrix)
    for i in range(row_num):
        solution_matrix[i][col_num - 1] *= lcm * -1

    coefficients = []
    for i in range(row_num):
        coefficients.append(int(solution_matrix[i][col_num - 1]))
    coefficients.append(lcm)

    # Split the original equation into parts
    left_compounds, right_compounds = equation.replace(" ", "").split("->")
    left_compounds = left_compounds.split("+")
    right_compounds = right_compounds.split("+")

    balanced_equation = ""

    # left side
    for i in range(len(left_compounds)):
        # Add a "+" between compounds
        if i != 0:
            balanced_equation += " + "
        balanced_equation += str(coefficients[i]) + left_compounds[i]

    balanced_equation += " -> "

    # right side
    for i in range(len(right_compounds)):
        # Add a "+" between compounds
        if i != 0:
            balanced_equation += " + "
        balanced_equation += str(coefficients[i - len(left_compounds)]) + right_compounds[i]

    # Return the balanced equation
    return balanced_equation

