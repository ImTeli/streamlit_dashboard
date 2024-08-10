def format_number(value, prefix = ''):
    if value < 1000:
        return f'{prefix} {value:.2f}'
    elif value < 1000000:
        value /= 1000
        return f'{prefix} {value:.2f} mil'
    elif value < 1000000000:
        value /= 1000000
        return f'{prefix} {value:.2f} milhões'
    elif value < 1000000000000:
        value /= 1000000000
        return f'{prefix} {value:.2f} bilhões'
    elif value < 1000000000000000:
        value /= 1000000000000
        return f'{prefix} {value:.2f} trilhões'