from geometric_lib.circle import (
    area as circle_area,
    perimeter as circle_perimeter,
)
from geometric_lib.square import (
    area as square_area,
    perimeter as square_perimeter,
)


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {
    'perimeter-circle': 1,
    'area-circle': 1,
    'perimeter-square': 1,
    'area-square': 1
}


def calc(fig, func, size):
    assert fig in figs, f"Invalid figure: {fig}. Available: {figs}"
    assert func in funcs, f"Invalid function: {func}. Available: {funcs}"

    if fig == "circle":
        if func == "area":
            result = circle_area(*size)
        elif func == "perimeter":
            result = circle_perimeter(*size)
    elif fig == "square":
        if func == "area":
            result = square_area(*size)
        elif func == "perimeter":
            result = square_perimeter(*size)

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
            size = list(
                map(
                    float,
                    input(
                        "Input figure sizes separated by space "
                        "(e.g., radius for circle or side for square):\n"
                    ).split()
                )
            )

        except ValueError:
            print("Invalid input. Please enter numeric values.")

    calc(fig, func, size)
