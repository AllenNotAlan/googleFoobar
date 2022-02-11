

from os import remove
from numpy import size


def solution(xs):
    panel = cleanPanel(xs)

    result = 1
    for x in panel:
        result *= x

    if result < 1:
        result = result * -1

    return str(result)


def cleanPanel(panel: list):
    newPanel = []
    for x in panel:
        if x != 0 and x != 1:
            newPanel.append(x)
    return(newPanel)

test = [4, -1, 5, 0, 1, 0, 4]
print(solution(test))
