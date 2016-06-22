# Итераторы.

* функция niter(iterable, n=2)

возвращает кортеж из "копий"-итераторов по переданному итератору, каждый итератор должен предоставлять то же, что и итератор-источник. Новые итераторы независимы в смысле их текущих позиций (в первом может вычитаться значение, а в последующих они неизменны, возвращают первое значение)

* функция merge_longer_iter(iterables*, fill)

возвращает итератор из кортежей элементов передаваемых iterable-объектов, объединенных по позиции (сначала первые из первых, вторые из вторых и тд). Итератор выдает кортежи, пока не закончится самый длинный iterable. Если один из них заканчивается, то вместо его элементов вставляется fill

## Realisations:

**Python 2.7**

* https://docs.python.org/2.7/library/itertools.html#itertools.tee
* https://docs.python.org/2.7/library/itertools.html#itertools.izip_longest

**Python 3.5**

* https://docs.python.org/3.5/library/itertools.html#itertools.tee
* https://docs.python.org/3.5/library/itertools.html#itertools.zip_longest
