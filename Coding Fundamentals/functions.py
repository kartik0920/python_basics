"""
syntx: def func_name(parameters):
            code....
            return if needed

Dont use capital letter at start
"""


def greet(last_name, first_name="lokesh"):
    print(f"Hello {first_name} {last_name}")

    return first_name + " " + last_name, 21


def main():
    print("This is main function")
    hello = greet(last_name="Gile", first_name="Kartik")
    print(hello[1])
    print(hello[0])


if __name__ == "__main__":
    main()
