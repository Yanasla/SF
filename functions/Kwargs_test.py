def show_keys(**kwargs):
    print(' '.join(kwargs.keys()))

print(show_keys(verbose=True, mode='constant'))