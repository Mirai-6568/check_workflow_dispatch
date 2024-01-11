print("hello")

class Hello:
    def __init__(self):
        self.hello = "hello"
    def __call__(self, *args, **kwargs):
        print(self.hello)
        print("HELLOLOLO")
