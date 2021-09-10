#!/usr/bin/env python3
import sys

expression = sys.argv[1]

def evaluate_expression(expression):
    if expression_contains_equal_parentheses(expression):
        sub_expression_count = expression.count("(")
        while sub_expression_count != 0:
            expression_index = 0
            index_at_sub_expr = 0
            sub_expression_length = 0
            sub_expression = ''
            for char in expression:
                if char == "(":
                    sub_expression = ''
                    index_at_sub_expr = expression_index
                elif char == ")":
                    sub_expression_length += 1
                    break
                else:
                    sub_expression += char
                sub_expression_length += 1
                expression_index += 1
            result = calculate_sub_expression(sub_expression)
            expression = build_new_expression(expression, index_at_sub_expr, result, sub_expression_length)
            sub_expression_count -= 1
        return expression
    else:
        print("This expression contains unbalanced parentheses.")

def expression_contains_equal_parentheses(expression):
    return expression.count("(") == expression.count(")")

def calculate_sub_expression(sub_expression):
    sub_expression_as_array = sub_expression.split()
    FUNCTION = sub_expression_as_array[0]
    INTEGERS = sub_expression_as_array[1:]
    if integers_are_valid(INTEGERS):
        if FUNCTION == "add":
            return add(INTEGERS)
        elif FUNCTION == "multiply":
            return multiply(INTEGERS)
        elif FUNCTION.isnumeric():
            return int(FUNCTION)

def integers_are_valid(INTEGERS):
    for INTEGER in INTEGERS:
        if not INTEGER.isnumeric():
            return False
    return True

def add(INTEGERS):
    result = 0
    for INTEGER in INTEGERS:
        result += int(INTEGER)
    return result

def multiply(INTEGERS):
    result = int(INTEGERS[0])
    for INTEGER in INTEGERS[1:]:
        result = result * int(INTEGER)
    return result

def build_new_expression(expression, index_at_sub_expr, result, sub_expression_length):
    if result is not None:
        new_expression = expression[0:index_at_sub_expr] + str(result) + expression[sub_expression_length:]
        return new_expression

try:
    print(evaluate_expression(expression))
except:
    print("This expression is invalid, please review.")

