def saver(func):
    def wrapped(*args,**kwargs):
        with open(f'{func.__name__}.txt','w') as file:
            file.write(str(func(*args,**kwargs)))
        return func(*args, *kwargs)
    return wrapped
