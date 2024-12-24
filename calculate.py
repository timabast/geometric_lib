from geometric_lib import circle, square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {
    'perimeter-circle': 1,
    'area-circle': 1,
    'perimeter-square': 1,
    'area-square': 1,
}


def calc(fig, func, size):
    """Calculate area or perimeter for a given figure and size."""
    assert fig in figs, f"Invalid figure: {fig}. Available: {figs}"
    assert func in funcs, f"Invalid function: {func}. Available: {funcs}"

    if fig == "circle":
        if func == "area":
            result = circle.area(*size)
        elif func == "perimeter":
            result = circle.perimeter(*size)
    elif fig == "square":
        if func == "area":
            result = square.area(*size)
        elif func == "perimeter":
            result = square.perimeter(*size)

    print(f'{func} of {fig} is {result}')
    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = []

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}: \n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}: \n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        try:
            size = list(map(float, input(
                "Input figure sizes separated by space, "
                "1 for circle and square:\n"
            ).split()))
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    calc(fig, func, size)
