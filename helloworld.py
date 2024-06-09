class shoppinglist:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
    def show(self):
        print(self.items)

ove = shoppinglist()
ove.add("apple")
ove.add("banana")
ove.add("cherry")
ove.show()
