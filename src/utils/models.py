from typing import List


class Child:
    def __init__(self, mark, cookies):
        self.mark = mark
        self.cookies = cookies

    def __repr__(self):
        return f"Child with m:{self.mark} and c:{self.cookies}"

    def give_cookie(self):
        self.cookies = self.cookies + 1

    def take_cookie(self):
        self.cookies = self.cookies - 1

    def set_cookies(self, cookies):
        self.cookies = cookies


Children = List[Child]
