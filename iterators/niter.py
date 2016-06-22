from collections import deque


def niter(iterable, n=2):
    iterable = iter(iterable)
    deques = [deque() for _ in xrange(n)]

    def gen(d):
        while True:
            if not d:
                item = next(iterable)
                for _d in deques:
                    _d.append(item)
            yield d.popleft()

    return tuple(gen(d) for d in deques)


if '__main__' == __name__:
    a = [1, 2, 3]
    b, c = niter(a, 2)

    for i in b:
        print i

    for i in c:
        print i
