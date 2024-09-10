from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

import requests

N = 21

def main():
    rectangle = Rectangle(N, N, "blue")
    circle = Circle(N, "green")
    square = Square(N, "red")

    print('{}\n{}\n{}\n'.format(rectangle,circle,square))

    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

    print(f"Status code: {response.status_code}")
    print(f"Response body: {response.json()}")


if __name__ == "__main__":
    main()
