def fileparser(filename, parser):

    def decorator(func):

        def wrapper():

            res = []

            with open(filename, 'r') as f:
                for line in f:
                    args, kwargs = parser(line)
                    res.append(func(*args, **kwargs))
            res = tuple(res)

            def returned_function():
                return res

            return returned_function

        return wrapper

    return decorator


def some_parser(line):
    args = map(int, line.split(' '))
    kwargs = {}
    return args, kwargs


@fileparser('input.txt', some_parser)
def some_func(*args):
    return sum(args)


if '__main__' == __name__:
    iter_func = some_func()
    for item in iter_func():
        print item
