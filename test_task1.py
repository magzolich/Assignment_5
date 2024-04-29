from Task1 import can_create_triangle


def test():
    assert can_create_triangle((1, 2, 3)) == False
    assert can_create_triangle((2, 2, 2)) == True
    assert can_create_triangle((0, 1, 2)) == False
    assert can_create_triangle((10, 10, 20)) == False
    assert can_create_triangle((3, 4, 5)) == True
    assert can_create_triangle((5, 4, 3)) == True
    assert can_create_triangle((4, 5, 3)) == True
