from src import decorators


@decorators.log()
def sum(x, y):
    return x + y


def test_sum(capsys):
    sum(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "sum start - 00:00:00\nsum work\nsum stop - 00:00:00\nmy_function ok\n"


def test_sum_1(capsys):
    sum(1, "2")
    captured = capsys.readouterr()
    assert captured.out == "sum error: unsupported operand type(s) for +: 'int' and 'str'. inputs: (1, '2'), {}\n"
