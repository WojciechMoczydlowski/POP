from typing import List


class Child:
    def __init__(self, mark, cookies):
        self.mark = mark
        self.cookies = cookies

    def give_cookie(self):
        self.cookies = self.cookies + 1

    def take_cookie(self):
        self.cookies = self.cookies - 1

    def __repr__(self):
        return f"Child with m:{self.mark} and c:{self.cookies}"

    def __eq__(self, other):
        return self.mark == other.mark and self.cookies == other.mark


Children = List[Child]
