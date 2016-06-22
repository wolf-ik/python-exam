import cPickle


def cache(func):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        hash_code = cPickle.dumps((args, sorted(kwargs.items())))
        from_cache = True
        if hash_code not in cache_dict.keys():
            from_cache = False
            cache_dict[hash_code] = func(*args, **kwargs)
        return from_cache, cache_dict[hash_code]

    return wrapper


@cache
def some_func(a=1, b=2):
    return a + b


if '__main__' == __name__:
    assert (False, 3) == some_func()
    assert (False, 3) == some_func(1, 2)
    assert (False, 3) == some_func(a=1, b=2)
    assert (True, 3) == some_func(a=1, b=2)
    print '42'
