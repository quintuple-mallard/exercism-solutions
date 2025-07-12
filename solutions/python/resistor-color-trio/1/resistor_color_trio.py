COLOR_VALUES={
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9,
}
def label(colors):
    resistance=(COLOR_VALUES[colors[0]]*10+COLOR_VALUES[colors[1]])*10**COLOR_VALUES[colors[2]]
    if resistance>=1000000000:
        return f'{int(resistance/1000000000)} gigaohms'
    elif resistance>=1000000:
        return f'{int(resistance/1000000)} megaohms'
    elif resistance>=1000:
        return f'{int(resistance/1000)} kiloohms'
    return f'{resistance} ohms'