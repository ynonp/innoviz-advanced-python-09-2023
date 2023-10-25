class LightBulb:

    def __init__(self):
        self.is_on = False

    def turn_on(self):
        if self.is_on: return

        print("Lights On")
        self.is_on = True

    def turn_off(self):
        if not self.is_on: return

        print("Lights Off")
        self.is_on = False


class Book:
    ISBN: str
    title: str
    pages: int = 0

    def __init__(self, ISBN, title):
        self.ISBN = ISBN
        self.title = title

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"[{self.ISBN} {self.title} ({self.pages} pages)"



with open('file') as f:
    pass

