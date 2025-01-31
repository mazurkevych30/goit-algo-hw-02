class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Додавання елемента до стеку"""
        self.stack.append(item)

    def pop(self):
        """Видалення елемента зі стеку"""
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def is_empty(self):
        """Перевірка, чи стек порожній"""
        return len(self.stack) == 0

    def peek(self):
        """Перегляд верхнього елемента стеку без його видалення"""
        if not self.is_empty():
            return self.stack[-1]


def checkBrackets(text: str) -> str:
    s = Stack()
    brackets = {
        "(" : ")",
        "{" : "}",
        "[" : "]"
    }

    for char in text:
        if char in "({[":
            s.push(char)
        elif char in ")}]":
            if s.is_empty() or brackets[s.pop()] != char:
                return "Asymmetrical"

    if not s.is_empty():
        return "Asymmetrical"

    return "Symmetrical"

print(checkBrackets("}( 23 ( 2 - 3);:)"))
print(checkBrackets("( 23 ( 2 - 3);:"))
print(checkBrackets("( ){[ 1 ]( 1 + 3 )( ){ }}"))
print(checkBrackets("( 11 }:"))
