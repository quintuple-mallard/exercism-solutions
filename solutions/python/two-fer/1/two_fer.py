def two_fer(*name):
    if not name:
        return 'One for you, one for me.'
    return f'One for {name[0]}, one for me.'
