print("hello")

class Hello:
    def __init__(self):
        self.hello = "hello"
    def __call__(self, *args, **kwargs):
        print(self.hello)
        print(self.new_hello())

    def new_hello(self):
        print("NEWHELLO")
        print("HELLO")
        print("HELLOOOO")
        print("HELLOOOOOO")
        print("a")
        print("b")
        print("c")

class Hello2:
    def __init__(self):
        self.hello = "hello"
    def __call__(self, *args, **kwargs):
        print(self.hello)
        print(self.new_hello())

    def new_hello(self):
        print("NEWHELLO")
        print("HELLO")
        print("HELLOOOO")
        print("HELLOOOOOO")
        print("a")
        print("b")
        print("c")
