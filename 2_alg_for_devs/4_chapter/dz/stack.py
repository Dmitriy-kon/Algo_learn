"""Stack implemented using dynamic array inside."""


class Stack:
    def __init__(self):
        # Array where we store the data
        self.a = [None] * 10
        # Number of elements that we actually store in the array. <= a.length
        self.size = 0

    def get_size(self) -> int:
        return self.size

    def reallocate(self) -> None:
        """
        This function is called when it's not enough memory to fit new elements.
        It creates new long array and copies all the elements there.
        """
        size = len(self.a)
        new_a = [None] * (size * 2)

        for i in range(size):
            new_a[i] = self.a[i]
        self.a = new_a

    def push_back(self, x: int) -> None:
        """Adds element to the end of the stack."""
        self.a[self.size] = x
        self.size += 1

        if self.size == len(self.a):
            self.reallocate()

    def pop_back(self) -> int:
        """Removes last element from the stack and returns its value."""
        res = self.a[self.size - 1]
        self.a[self.size - 1] = None
        self.size -= 1
        return res

    def top(self) -> int:
        """Returns value of the last element in the stack."""
        #  IMPLEMENT THIS
        return self.a[self.size - 1]


def calc_polish(s: str) -> int:
    """
    Calculates the result of reversed polish notation. https://en.wikipedia.org/wiki/Reverse_Polish_notation
    This one is simplified. Every number and character are separated by exactly one space.
    Only + - * should be supported.

    >>> calcPolish("1 2 3 * -")
    -5
    # because (1 - (2 * 3))
    """
  # splitting expression at whitespaces 
    expression = s.split() 
        
    # stack 
    stack = [] 
        
    # iterating expression 
    for ele in expression: 
        
        # ele is a number 
        if ele not in '/*+-': 
            stack.append(int(ele)) 
        
        # ele is an operator 
        else: 
        # getting operands 
            right = stack.pop() 
            left = stack.pop() 
            
        # performing operation according to operator 
        if ele == '+': 
            stack.append(left + right) 
            
        elif ele == '-': 
            stack.append(left - right) 
            
        elif ele == '*': 
            stack.append(left * right) 
            
        elif ele == '/': 
            stack.append(int(left / right)) 
        
    # return final answer. 
    return stack.pop()


stack = Stack()
stack.push_back(1)
stack.push_back(1)
stack.push_back(1)

print(stack.a)
print(stack.pop_back())
print(stack.a)
print(stack.top())

print(calc_polish("1 2 3 * -"))