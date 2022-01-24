from typing import List


class Child:
    def __init__(self, mark, cookies):
        self.mark = mark
        self.cookies = cookies

    def give_cookie(self):
        self.cookies = self.cookies + 1

    def take_cookie_immutable(self):
        if self.cookies > 1:
            return Child(self.mark, self.cookies - 1)
        return self

    def take_cookies_immutable(self, n):
        if self.cookies - n >= 1:
            return Child(self.mark, self.cookies - n)
        return self

    def __repr__(self):
        return f"m:{self.mark} c:{self.cookies}"

    def __eq__(self, other):
        return self.mark == other.mark and self.cookies == other.mark


Children = List[Child]
