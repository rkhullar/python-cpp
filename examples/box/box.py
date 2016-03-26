class box:
    def __init__(self, w, h, l):
        self.width = w
        self.height = h
        self.length = l

    def __str__(self):
        return "this is a box"

    def volume(self):
        return self.width * self.height * self.length


if __name__ == '__main__':
    b = box(1,2,3)
    print b
    print b.volume()
