import algorithms.gauss_elimination as gauss


# eq = [
#     {"x1": 1, "x2": 1, "x3": 1, "result": 3},
#     {"x1": 2, "x2": -1, "x3": -1, "result": 0},
#     {"x1": 6, "x2": -4, "x3": 2, "result": 4},
# ]


# Test 1

ans = gauss.gauss_elimination([[1, 1, 1, 3], [2, -1, -1, 0], [6, -4, 2, 4]], True)
print(f"Ok = {gauss.check_ans([[1, 1, 1, 3], [2, -1, -1, 0], [6, -4, 2, 4]], ans)}")

# Test 2 - random all sum 1

ans = gauss.gauss_elimination([[0.2, 0.3, 0.5, 1], [0.1, 0.2, 0.7, 1], [0.3, 0.4, 0.3, 1]], True)
print(f"Ok = {gauss.check_ans([[0.2, 0.3, 0.5, 1], [0.1, 0.2, 0.7, 1], [0.3, 0.4, 0.3, 1]], ans)}")