def slices(series, length):
    num_digits = len(series)

    if length > num_digits or length < 1:
        raise ValueError('You silly goose')
    
    backstop = num_digits - length + 1

    return [series[idx:idx+length] for idx in range(backstop)]