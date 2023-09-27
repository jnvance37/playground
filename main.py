from seval import safe_eval

# Dictionary to store variables
variables = {}


def main():
    while True:
        expression = input(
            "Enter a mathematical expression or assignment (e.g., 'x = 5'): ")
        if not expression:
            break
        try:
            result = evaluate_expression(expression)
            print(f"Result: {result}")
        except (ValueError, SyntaxError, NameError):
            raise


def evaluate_expression(expression):
    try:

        # Check if it's an assignment
        if "=" in expression:
            parts = expression.split("=")
            if len(parts) != 2:
                raise SyntaxError("Invalid assignment")
            variable_name = parts[0].strip()
            variable_value = parts[1]
            # Store the variable in the dictionary
            variables[variable_name] = safe_eval(variable_value)
            return f"Assigned {variable_name} = {variables[variable_name]}"

        result = safe_eval(expression)
        return result
    except (ValueError, SyntaxError, NameError):
        raise


if __name__ == "__main__":
    main()
