def is_pangram(sentence):
    alphas = list('abcdefghijklmnopqrstuvwxyz')

    for char in sentence:
        char = char.lower()
        if char in alphas:
            alphas.remove(char)

            if len(alphas) == 0:
                return True
        
    return False