def greet_multiple(*names):
    for name in names:
        print("Hello, " + name)
greet_multiple("Alice", "Bob", "Charlie")
