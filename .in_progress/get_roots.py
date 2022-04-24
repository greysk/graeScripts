"""
Obtain real zeros of a polynomial function.

Author: Graeson Thomas
Date Created: 2022-04-23
Last Updated: 2022-04-24
"""
from fractions import Fraction
from math import sqrt


def get_factors(n: int) -> list:
    """Returns the factors of a given integer.
    """
    return [i for i in range(1, n+1) if n % i == 0]


def obtain_coefficients(coefficients: list = None) -> list:
    """Prompt user to provide coefficients for a polynomial."""
    if coefficients:
        if [a for a in coefficients if not isinstance(a, int)]:
            # Raise error of coefficients are not all integers.
            raise TypeError('Coefficients must be integers.')
        return coefficients
    # If no coefficient passed to function, obtain from terminal input.
    coefficients = []
    # Get polynomial's degree for number of coefficients to request
    polynomialdegree = int(input('Enter the degree of the polynomial: '))
    # Ask user to provide coefficients by power of x to ensure all
    # provided and provided in order.
    for i in range(polynomialdegree, -1, -1):
        coefficient = input(f'Enter coefficient for x^{i}: ').strip()
        if coefficient.startswith('-'):
            coefficient = coefficient.replace('-', '')
            sign = -1
        else:
            sign = 1
        # Convert string coefficient to int, Fraction, or Complex
        if coefficient.isnumeric():
            coefficients.append(int(coefficient) * sign)
        else:
            raise TypeError('Coefficients must be integers.')
    return coefficients


def get_possible_zeros(coefficients: list) -> list:
    """Rational Zeros Theorem possible zeros of a polynomial function.

    Args:
        coefficients (list): The coefficients of a polynomial function,
        in order of degree including all from a_n to a_0.

    Returns:
        list: A list containing all possible zeros, negative and positive.
    """
    possible_zeros = []
    # Obtain factors of a_n and a_0
    factors_an = get_factors(coefficients[0])
    factors_a0 = get_factors(coefficients[-1])
    # Generate all possible zeros, skipping duplicates.
    for i in factors_a0:
        possible_zeros.extend([i, -i])
        for j in factors_an:
            frac = Fraction(i, j)
            if frac not in possible_zeros:
                possible_zeros.extend([frac, -frac])
    # Sort the possible zeros in absolute value order.
    possible_zeros.sort(key=abs)
    return possible_zeros


def convert_to_int(n: float | Fraction):
    """Convert float of fraction to int when value represent an int."""
    if n == 0:
        n = 0
    elif isinstance(n, Fraction) and n.denominator == 1:
        n = n.numerator
    elif isinstance(n, float) and n - int(n) == 0:
        n = int(n)
    return n


def mod_by_x_minus(coefficients: list, x_minus: Fraction | int
                   ) -> int | Fraction:
    """Obtain the remainder of dividing a polynomial by x - {x_minus}"""
    result = 0
    # Obtain the remainder using synthetic division.
    for i in coefficients:
        result = (result + i) * x_minus
    # Convert int floats and Fractions to int.
    if isinstance(result, (float, Fraction)):
        result = convert_to_int(result)
    return result


def floor_by_minus(coefficients: list, x_minus: Fraction | int
                   ) -> tuple:
    last_coefficient_index = len(coefficients) - 1
    result = 0
    quotient_coefficients = []
    # Obtain the remainder and quotient using synthetic division.
    for i, a in enumerate(coefficients):
        if i != last_coefficient_index:
            # Obtain quotient, convert int floats and Fractions to int.
            quotient_coefficient = (result + a)
            if isinstance(quotient_coefficient, (float, Fraction)):
                quotient_coefficient = convert_to_int(quotient_coefficient)
            quotient_coefficients.append(quotient_coefficient)
        # Calculate remainder
        result = (result + a) * x_minus
    return quotient_coefficients


def get_real_zeros(coefficients: list) -> dict:
    """Return zero(s) of a polynomial function with coefficients."""
    # Obtain all possible zeros using the rational zeros theorem.
    possiblezeros = get_possible_zeros(coefficients)
    # Test all possible zeros, saving any whose remainder is zero.

    return [possiblezero for possiblezero in possiblezeros
            if mod_by_x_minus(coefficients, possiblezero) == 0]


def make_polynomial(coefficients: list) -> str:
    """Make a string polynomial from coefficients."""
    polynomial = []
    power = len(coefficients) - 1
    # Create the polynomial
    for i, a in enumerate(coefficients):
        # If a is negative, add a minus sign between terms.
        if i != 0:
            if a > 0:
                polynomial.append('+')
            elif a < 0:
                polynomial.append('-')
                a = abs(a)
            else:
                power -= 1
                continue
        # A coefficient of one is not shown before the x.
        if a == 1:
            a = ''
        # Add the terms with x to the appropriate power.
        if power > 1:
            polynomial.append(f'{a}x^{power}')
        elif power == 1:
            polynomial.append(f'{a}x')
        elif power == 0:
            polynomial.append(f'{a}')
        else:
            break
        power -= 1
    return ' '.join(polynomial)


def quadratic_formula(coefficients: list) -> tuple:
    """Obtain parts of resulting quadratic formula.

    Returns:
        (tuple): (str) value before determinate over 2(a),
                 (str) determinate over 2(a)
    """
    if len(coefficients) != 3:
        raise ValueError(
            'The quadratic formula can only be used on a 3-degree polynomial.')
    A = coefficients[0]
    B = coefficients[1]
    C = coefficients[2]

    determinate = pow(B, 2) - (4 * A * C)
    denominator = 2 * A
    k = Fraction(-B, denominator)
    print(sqrt(abs(determinate)))
    # Handle imaginary numbers
    if determinate < 0:
        i = 'i'
    else:
        i = ''
    # If square root has a integer result, return it.
    # Otherwise, return pre-sqrt root value.
    sqrt_determinate = sqrt(abs(determinate))
    if sqrt_determinate - int(sqrt_determinate) == 0:
        m = f'{Fraction(int(sqrt_determinate), denominator)}{i}'
    else:
        m = f'{i}√({sqrt_determinate})/{denominator}'
    return k, m, denominator


if __name__ == '__main__':
    coefficients = obtain_coefficients()
    # Print starting polynomial based on coefficients provided.
    starting_polynomial = make_polynomial(coefficients)
    print(f'The real zeros for {starting_polynomial} are:')
    # Print out real zeros
    real_zeros = get_real_zeros(coefficients)
    print('\treal zeros =', real_zeros)
    # Factor out real zeros and print out quotient
    quotient = coefficients
    print('The quotient after factoring out the real zeros is:')
    for real_zero in real_zeros:
        quotient = floor_by_minus(quotient, real_zero)
    print('\tquotient =', make_polynomial(quotient))
    # If quotient is a quadratic formula, return remaining zeros (if any).
    print('The remaining non-real zeros:')
    if len(quotient) == 3:
        quadratic_formula_parts = quadratic_formula(quotient)
        print('\tx =', f'{quadratic_formula_parts[0]}',
              f'± {quadratic_formula_parts[1]}')
    else:
        print('Cannot be determined - Quotient is not a quadratic formula.')
