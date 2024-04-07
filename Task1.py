# Write a python code to verify if three side (line) lengths provided by user can make a triangle:

def provide_triangle_lenghts():
    a = int(input("Provide 1st triangle length: "))
    b = int(input("Provide 2nd triangle length: "))
    c = int(input("Provide 3rd triangle length: "))
    return (a, b, c)


def can_create_triangle(sides: tuple[int, int, int]):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a+b > c or a+c > b or b+c > a


def main():
    triangle_lenghts = provide_triangle_lenghts()
    triangle_results = can_create_triangle(triangle_lenghts)
    if triangle_results:
        print("You can create a triangle")
    else:
        print("You can't create a triangle")


if __name__ == "__main__":
    main()
