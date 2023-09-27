import ast

def main():
    expression = input("Enter a mathematical expression: ")
    try:
        result = evaluate_expression(expression)
        print(f"Result: {result}")
    except (ValueError, SyntaxError):
        print("Invalid expression")

def evaluate_expression(expression):
    try:
        # Use ast.literal_eval to evaluate the expression safely
        parsed_expression = ast.literal_eval(expression)
        return parsed_expression
    except (ValueError, SyntaxError):
        raise

if __name__ == "__main__":
    main()