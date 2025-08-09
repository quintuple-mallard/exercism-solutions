import re
from operator import add, sub, mul, floordiv
OPERATORS = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": floordiv
}
class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message

class Stack:
    def __init__(self):
        self._stack = []
    
    def push(self, val): # Add value to stack
        self._stack.append(val)
        
    def drop(self): # DROP stack operator
        if len(self._stack) == 0:
            raise StackUnderflowError("Insufficient number of items in stack")
            
        self._stack.pop(-1)

    def dup(self): # DUP stack operator
        if len(self._stack) == 0:
            raise StackUnderflowError("Insufficient number of items in stack")
            
        self._stack.append(self._stack[-1])

    def swap(self): # SWAP stack operator
        if len(self._stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack")
            
        *rest, second, top = self._stack
        self._stack = [*rest, top, second]
        
    def over(self): # OVER stack operator
        if len(self._stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack")
            
        *rest, second, top = self._stack
        self._stack = [*rest, second, top, second]

    def call(self, f): # Call a function on the stack
        if len(self._stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack")
        arg1, arg2, *rest = reversed(self._stack)
        self.drop()
        self.drop()
        if f == floordiv and arg1 == 0:
            raise ZeroDivisionError("divide by zero")
            
        self._stack.append(f(arg2, arg1))

    @property
    def stack(self):
        return self._stack

def expand_custom_words(input):
    replacements = {}
    expanded = []
    for item in input:
        if re.fullmatch(": .+? .+? ;", item):
            name, definition = re.match(": (.+?) (.+?) ;", item).groups()
            definition = definition.split()
            for i, word in enumerate(definition):
                if word in replacements:
                    definition[i] = replacements[word]
            definition = " ".join(definition)
            if re.fullmatch(r"[a-z-]+|[+\-*\/]", name):
                replacements.update({name: definition})
            else:
                return ValueError("illegal operation")
        else:
            item = item.split()
            for i, word in enumerate(item):
                if word in replacements:
                    item[i] = replacements[word]
            item = " ".join(item)
            expanded.append(item)
    return expanded[0]
            
  
                
def evaluate(input):
    input = [item.lower() for item in input] # Normalize case
    processable_input = expand_custom_words(input)
    if isinstance(processable_input, ValueError):
        raise processable_input
    stack = Stack()
    for item in processable_input.split():
        try:
            item = int(item)
            stack.push(item)
        except:
            if re.fullmatch("[a-z]+", item):
                try:
                    getattr(stack, item)()
                except AttributeError:
                    raise ValueError("undefined operation")
            else:
                stack.call(OPERATORS[item])
    return stack.stack
