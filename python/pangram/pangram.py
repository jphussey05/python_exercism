def is_pangram(sentence):
    alphas = set('abcdefghijklmnopqrstuvwxyz')
    diff = alphas - set(sentence.lower())

    return True if len(diff) == 0 else False