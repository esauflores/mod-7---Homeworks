# gaussian.py

# gaussian elimination method


def gauss_elimination(equations, names, logs=False):
    eq = equations.copy()
    n = len(eq)

    if logs:
        print_equations(eq, names)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(eq[i][names[i]]) < abs(eq[j][names[i]]):
                eq[i], eq[j] = eq[j], eq[i]

        for j in range(i + 1, n):
            eq[j]["result"] -= eq[i]["result"] * eq[j][names[i]] / eq[i][names[i]]
            for k in range(n - 1, i - 1, -1):
                eq[j][names[k]] -= eq[i][names[k]] * eq[j][names[i]] / eq[i][names[i]]

        print("Step:", i + 1)
        if logs:
            print_equations(eq, names)

    ans = [0 for _ in range(n)]

    for i in range(n - 1, -1, -1):
        t = sum([eq[i][names[j]] * ans[j] for j in range(i + 1, n)])
        ans[i] = (eq[i]["result"] - t) / eq[i][names[i]]

    return ans


def check_ans(equations, ans, names, tol=1e-6):
    for eq in equations:
        res = 0
        for name in names:
            res += eq[name] * ans[names.index(name)]
        if abs(res - eq["result"]) > tol:
            return False
    return True


def test_gauss_elimination(equations):
    names = []
    for eq in equations:
        for name in eq.keys():
            if name not in names and name != "result":
                names.append(name)
    names.remove("result")

    print()

    ans = gauss_elimination(equations, names, logs=1)

    readable_ans = ""
    for name in names:
        readable_ans += name + " = " + str(ans[names.index(name)]) + ", "
    readable_ans = readable_ans[:-2]

    print("Answer: ", readable_ans)
    print("Works: ", check_ans(equations, ans, names))


def print_equations(equations, names):
    print()
    for eq in equations:
        eqstr = ""
        for name in names:
            eqstr += str(eq[name]) + name + (" + " if name != names[-1] else " = ")
        eqstr += str(eq["result"])
        print(eqstr)
    print()
