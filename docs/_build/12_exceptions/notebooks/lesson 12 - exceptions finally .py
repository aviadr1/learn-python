import sys

def A(x):
    print(f"starting A({x})", file=sys.stderr)
    y = B(x)
    print(f"A({x}) --> {y}", file=sys.stderr)
    return y

def B(x):
    print(f"starting B({x})", file=sys.stderr)
    try:
        y = C(x)
    finally:
        print("B has finished calling C", file=sys.stderr)

    print(f"B({x}) --> {y}", file=sys.stderr)
    return y

def C(x):
    print(f"starting C({x})", file=sys.stderr)
    return D(x)
    print(f"C({x}) --> {y}", file=sys.stderr)
    return y

def D(x):
    print(f"starting D({x})", file=sys.stderr)
    y =  10 / x
    if x > 0:
        open("1")

    print(f"D({x}) --> {y}", file=sys.stderr)
    return y



print("starting the program", file=sys.stderr)
#print(A(10))
x = 0
for x in [-1, 0, 1]:
    y = None
    try:
        y = A(x)
        print(f"A({x}) --> {y}", file=sys.stderr)
    except ZeroDivisionError as ex:
        print("you're a bad mathematician", ex, file=sys.stderr)
    except Exception as ex:
        print("oops! I made an oppsie: error", type(ex), ex, file=sys.stderr)
    except OSError as ex:
        print("do you really need this file???", type(ex), x, file=sys.stderr)
    finally:
        print(f"y={y}", file=sys.stderr)

print("the end")