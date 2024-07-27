# This function performs basic arithmetic operations and raises an error if an invalid operation is provided or if dividing by zero.
def calculator(a, b, operation):
    """
    Peforms basic arithmetic operations.

    Arguments:
    a (float type): The first number.
    b (float type): The second number.
    operation (str type): The operation to perform. Can be 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
    float type: The result of the operation.

    Raises:
    ValueError: If an invalid operation is provided or if dividing by zero.
    """
    if operation:
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        elif operation == 'multiply':
            return a * b
        elif operation == 'divide':
            if b == 0:
                raise ValueError('Cannot divide by zero.')
            return a / b
        else:
            raise ValueError(f"Invalid operation: {operation}")
        
# Example
if __name__ == "__main__":
    print(calculator(10, 5, 'add'))  # Should print 15
    print(calculator(10, 5, 'subtract'))  # Should print 5
    print(calculator(10, 5, 'multiply'))  # Should print 50
    print(calculator(10, 5, 'divide'))  # Should print 2.0

    # Uncomment to test error handling
    # print(calculator(10, 0, 'divide'))  # Should raise ValueError
    # print(calculator(10 ,5, 'invalid'))  # Should raise ValueError
    