
class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def __str__(self):
        return "{v} {s}".format(v=self.value, s=self.suite)
