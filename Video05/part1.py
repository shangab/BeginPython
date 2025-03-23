
person = "Person"


def sayHelloWorld():
    print("Hello World!")
    print(f"Hello {person}!")


def capsAndReverse(text: str):
    def sayHello():
        print(f"Hello {text}")
    sayHello()
    caps = text.upper()
    rev = []
    for c in text:
        rev.insert(0, c)
    rev = ''.join(rev)
    return caps, rev


def greet(name=None):
    if name is None:
        print(f"Hello {person}")
    else:
        print(f"Hello {name}")


def capsAndReverse2(text: str, func):
    func(text)
    caps = text.upper()
    rev = []
    for c in text:
        rev.insert(0, c)
    rev = ''.join(rev)
    return caps, rev


c, r = capsAndReverse2("osman", greet)
print(c)
print(r)
# sayHelloWorld()
# greet("Sami")

# greet()
