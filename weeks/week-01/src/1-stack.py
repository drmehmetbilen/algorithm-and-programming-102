class Stack:
    """Array-based Stack implementation"""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add an item to the top of the stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return the top item without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)
    
    def __str__(self):
        return f"Stack({self.items})"


# Example usage of Stack

def is_balanced_parentheses(expression):
    """
    Check if parentheses in an expression are balanced
    Example: "(()())" -> True, "(()" -> False
    """
    stack = Stack()
    opening = "({["
    closing = ")}]"
    matches = {"(": ")", "{": "}", "[": "]"}
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            if matches[stack.pop()] != char:
                return False
    
    return stack.is_empty()

def reverse_string(text):
    """Reverse a string using a stack"""
    stack = Stack()
    
    for char in text:
        stack.push(char)
    
    reversed_text = ""
    while not stack.is_empty():
        reversed_text += stack.pop()
    
    return reversed_text

if __name__ == "__main__":
    # Test balanced parentheses
    print(is_balanced_parentheses("(()())"))  # True
    print(is_balanced_parentheses("(()"))     # False
    
    # Test string reversal
    print(reverse_string("Hello, World!"))  # !dlroW ,olleH