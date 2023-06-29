import chemparse

def parse_equation(equation):
    # Split the equation into left and right sides
    left, right = equation.split("->")
    
    # Further split each side into its compounds
    left_compounds = []
    right_compounds = []
    for compound in left.split("+"):
        left_compounds.append(compound.strip())
    for compound in right.split("+"):
        right_compounds.append(compound.strip())
  
    # Parse the compounds to get the elements and their counts
    left_elements = []
    right_elements = []
    for compound in left_compounds:
        left_elements.append(chemparse.parse_formula(compound))
    for compound in right_compounds:
        right_elements.append(chemparse.parse_formula(compound))

    # Return the parsed elements
    return left_elements, right_elements

def get_matrix(left_elements, right_elements):
    elements_set = set()

    # Go through each compound in the list of left_elements and right_elements
    for compound in left_elements + right_elements:
        # Add each element of the compound to the set
        for element in compound.keys():
            elements_set.add(element)

    # Convert the set to a list and sort it
    elements = sorted(list(elements_set))
    
    matrix = []
    for element in elements:
        row = []
        # For each compound on the left (reactants), get the count of the current element
        for compound in left_elements:
            row.append(-1 * compound.get(element, 0)) # Use a negative sign for reactants
        # For each compound on the right (products), get the count of the current element
        for compound in right_elements:
            row.append(compound.get(element, 0))
        matrix.append(row)
    return elements, matrix