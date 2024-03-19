from typing import Any


class Node:

	def __init__(self, value) -> None:
		self.value = value
		self.next = None


class Stack:
	# Initializing a stack.
	# Use a dummy node, which is
	# easier for handling edge cases.
	def __init__(self) -> None:
		self.stack = []

	# String representation of the stack
	def __str__(self) -> str:
		return "".join([str(x) for x in self.stack])

	# Get the current size of the stack
	def get_size(self) -> int:
		return len(self.stack)

	# Check if the stack is empty
	def is_empty(self) -> bool:
		return self.stack == []

	# Get the top item of the stack
	def top(self) -> Any:
		# Sanitary check to see if we
		# are peeking an empty stack.
		if self.is_empty():
			raise Exception("Peeking from an empty stack")
		return self.stack[-1]

	# Push a value into the stack.
	def push(self, value) -> None:
		self.stack.append(value)

	# Remove a value from the stack and return.
	def pop(self) -> Any:
		if self.is_empty():
			raise Exception("Popping from an empty stack")
		return self.stack.pop()
