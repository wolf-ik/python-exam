def merge(*args, **kwargs):
    fill = kwargs.get('fillvalue')
    args = map(iter, args)

    def get_next():
        cnt = 0
        res = []
        for arg in args:
            try:
                val = next(arg)
            except StopIteration:
                cnt += 1
                val = fill
            res.append(val)
        if cnt == len(args):
            raise StopIteration()
        return res

    while True:
        yield tuple(get_next())


if '__main__' == __name__:
    a = merge([1, 2, 3], ['a', 'b'], [False], fillvalue='fucker')
    for i in a:
        print i
