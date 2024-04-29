from Task2 import validate_pin


def test():
    assert validate_pin('1234', '1234')[0] == True
    assert validate_pin('1234', '12345')[0] == False
    assert validate_pin('987654', '987654')[0] == True
    assert validate_pin('0000', '0000')[0] == False
    assert validate_pin('1145', '1145')[0] == False
    assert validate_pin('12345', '12345')[0] == False
    assert validate_pin('12ab', '12ab')[0] == False
