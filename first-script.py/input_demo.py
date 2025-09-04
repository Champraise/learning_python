"""A simple script to demonstrate user input in Python.
It prompts the user to enter their name and then greets them."""
name = input("Enter your name: ")
print(f"Hello, {name}!")

import ast
import operator

def safe_eval(expr):
	# Supported operators
	allowed_operators = {
		ast.Add: operator.add,
		ast.Sub: operator.sub,
		ast.Mult: operator.mul,
		ast.Div: operator.truediv,
		ast.Pow: operator.pow,
		ast.USub: operator.neg,
	}

	def eval_node(node):
		if isinstance(node, ast.Num):  # <number>
			return node.n
		elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
			op_type = type(node.op)
			if op_type in allowed_operators:
				return allowed_operators[op_type](eval_node(node.left), eval_node(node.right))
			else:
				raise ValueError("Unsupported operator")
		elif isinstance(node, ast.UnaryOp):  # - <operand> e.g., -1
			op_type = type(node.op)
			if op_type in allowed_operators:
				return allowed_operators[op_type](eval_node(node.operand))
			else:
				raise ValueError("Unsupported unary operator")
		else:
			raise ValueError("Unsupported expression")

	try:
		node = ast.parse(expr, mode='eval').body
		return eval_node(node)
	except Exception as e:
		return f"Error: {e}"

expr = input("Enter an expression to evaluate (e.g., 2 + 3 * 4): ")
x = safe_eval(expr)
print(f"The result of the expression is: {x}")

# End of script
