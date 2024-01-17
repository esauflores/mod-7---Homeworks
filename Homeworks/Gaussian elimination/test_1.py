# test_1.py

import gaussian as gaus


def test_1():
    eq = [
        {"x1": 1, "x2": 1, "x3": 1, "result": 3},
        {"x1": 2, "x2": -1, "x3": -1, "result": 0},
        {"x1": 6, "x2": -4, "x3": 2, "result": 4},
    ]

    ans = gaus.gauss_elimination(eq, ["x1", "x2", "x3"], logs=True)
    print("Answer:", [round(x, 6) for x in ans])

    assert gaus.check_ans(eq, ans, ["x1", "x2", "x3"]), "Wrong answer"
