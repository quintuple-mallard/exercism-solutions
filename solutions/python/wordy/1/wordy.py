def operator_or_number(item):
    try:
        float(item)
    except:
        return "operator"
    else:
        return "int"


def valid_format(expression):
    expression_types = [operator_or_number(item) for item in expression]
    for i in range(len(expression_types) - 1):
        if expression_types[i] == expression_types[i + 1]:
            return False
    return expression_types[0] == 'int' and expression_types[-1] == 'int'

def get_operators(expression):
    operators = []
    for item in expression:
        try:
            float(item)
        except:
            operators.append(item)
    return operators

def valid_operators(expression):
    operators = get_operators(expression)
    return all(
        item in ("plus", "minus", "multiplied", "divided") for item in operators
    )

def evaluate_expression(operand1, operator, operand2):
    operand1, operand2 = float(operand1), float(operand2)
    if operator == "plus":
        return operand1 + operand2
    elif operator == "minus":
        return operand1 - operand2
    elif operator == "multiplied":
        return operand1 * operand2
    else:
        return operand1 / operand2
def answer(question):
    expression = question.removeprefix("What is").removesuffix("?").replace("by", "").split()
    if not expression:
        raise ValueError("syntax error")
    if not valid_operators(expression):
        raise ValueError("unknown operation")
    if not valid_format(expression):
        raise ValueError("syntax error")
    while len(expression) > 1:
        operand1, operator, operand2, *rest = expression
        result = evaluate_expression(operand1, operator, operand2)
        expression = [str(result), *rest]
    return float(expression[0])