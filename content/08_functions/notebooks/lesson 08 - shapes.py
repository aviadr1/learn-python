def get_line(n):
    return 'X' * n


def get_square(n):
    result = ""
    for i in range(n):
        line = get_line(n)
        result += line + '\n'

    return result


def get_triang(n):
    result = ""
    for i in range(1, n + 1):
        line = get_line(i)
        result += line + '\n'

    return result


def reverse(lst):
    return lst[:: -1]


def shape(n):
    return '\n'.join([
        get_triang(n),
        get_square(n),
        reverse(get_triang(n))
    ])

