from collections import deque

def is_polindrome(text: str) -> bool:
    text = text.replace(" ", "").lower()
    d = deque(text)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

print(is_polindrome("Racecar"))
print(is_polindrome("Hello world"))
print(is_polindrome("Was it a car or a cat I saw"))
print(is_polindrome("Bag"))
