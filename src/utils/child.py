class Child:
    def __init__(self, mark, cookies):
        self.mark = mark
        self.cookies = cookies

    def give_cookie(self):
        self.cookies = self.cookies + 1

    def take_cookie(self):
        self.cookies = self.cookies - 1
