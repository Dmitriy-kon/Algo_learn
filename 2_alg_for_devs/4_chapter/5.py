def chech(s: str):
    pass


class StackBracket:
    brackets_mapper = {")": "(", "]": "[", "}": "{"}

    def __init__(self) -> None:
        self.brackets: list[str] = []

    def check(self, bracket: str):
        return bracket in {"(", "[", "{"}

    def push(self, bracket: str):
        if self.check(bracket):
            self.brackets.append(bracket)

    def pop(self):
        return self.brackets.pop()

    def clean(self):
        self.brackets = []


stack_bracket = StackBracket()
brackets = r"[({][]})"
brackets2 = r"[({[]})]"
print(brackets)


def check_brackets(brackets: str) -> bool:
    for bracket in brackets:
        if bracket in {")", "]", "}"}:
            if stack_bracket.brackets[-1] == StackBracket.brackets_mapper[bracket]:
                stack_bracket.pop()
        stack_bracket.push(bracket)


check_brackets(brackets)
print(stack_bracket.brackets)
stack_bracket.clean()
check_brackets(brackets2)
print(stack_bracket.brackets)
