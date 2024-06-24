class Rect:
    def __init__(self, boyi, eni):
        self.length = boyi
        self.width = eni

    def area(self):
        return self.length * self.width

r = Rect(5, 10)

print("To'rtburchak yuzasi:", r.area())
