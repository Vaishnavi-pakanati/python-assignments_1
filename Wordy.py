# import re

# def answer(question):
#     # Iteration 0 - Numbers
#     if re.match(r"What is (-?\d+)\?", question):
#         return int(re.match(r"What is (-?\d+)\?", question).group(1))

#     # Iteration 1 - Addition
#     match = re.match(r"What is (-?\d+) plus (-?\d+)\?", question)
#     if match:
#         return int(match.group(1)) + int(match.group(2))

#     # Iteration 2 - Subtraction, Multiplication, and Division
#     match = re.match(r"What is (-?\d+) (plus|minus|multiplied by|divided by) (-?\d+)\?", question)
#     if match:
#         num1 = int(match.group(1))
#         num2 = int(match.group(3))
#         operation = match.group(2)
#         if operation == 'plus':
#             return num1 + num2
#         elif operation == 'minus':
#             return num1 - num2
#         elif operation == 'multiplied by':
#             return num1 * num2
#         elif operation == 'divided by':
#             if num2 == 0:
#                 raise ValueError("division by zero")
#             return num1 // num2  # using floor division to ensure an integer result

#     # Iteration 3 - Multiple Operations
#     match = re.match(r"What is (.+)\?", question)
#     if match:
#         operations = re.findall(r"(-?\d+) (plus|minus|multiplied by|divided by)", match.group(1))
#         if not operations:
#             raise ValueError("syntax error")
#         result = int(operations[0][0])
#         for i in range(1, len(operations)):
#             num = int(operations[i][0])
#             op = operations[i - 1][1]
#             if op == 'plus':
#                 result += num
#             elif op == 'minus':
#                 result -= num
#             elif op == 'multiplied by':
#                 result *= num
#             elif op == 'divided by':
#                 if num == 0:
#                     raise ValueError("division by zero")
#                 result //= num  # using floor division to ensure an integer result
#         return result

#     # Iteration 4 - Errors
#     raise ValueError("syntax error")


# # Example usage:
# try:
#     print(answer("What is 5 plus 13?"))  # 18
#     print(answer("What is 6 multiplied by 4?"))  # 24
#     print(answer("What is 3 plus 2 multiplied by 3?"))  # 15
#     print(answer("What is 5 plus 13 plus 6?"))  # 24
#     print(answer("What is 25 divided by 5?"))  # 5
#     print(answer("What is 52 cubed?"))  # Raises a ValueError
# except ValueError as e:
#     print(e)



import re
OPS = {
    "plus": "__add__", "minus": "__sub__",
    "multiplied": "__mul__", "divided": "__truediv__"
}
def answer(question):
    question = question.removeprefix("What is").removesuffix("?").strip()
    # question = question.strip("What is").strip("?").strip()
    if not question: raise ValueError("syntax error")   
    # if only a digit, return it
    if question.isdigit(): return int(question)
    # process one or more operations        
    ret = ret = re.split(' by | ', question)
    if len(ret) == 2:
        if ret[1] not in OPS.keys(): raise ValueError("unknown operation")
        raise ValueError("syntax error")
    while len(ret) > 1:
        try:
            x, op, y, *tail = ret
            if op not in OPS.keys() and not op.isnumeric():
                raise ValueError("unknown operation")
            op = OPS[op]
            # put result as first element and append what remains
            ret = [int(x).__getattribute__(op)(int(y)), *tail]
        except Exception as e: 
            if repr(e) == "ValueError('unknown operation')": raise e
            else: raise ValueError("syntax error")
    return ret[0]
