from multiprocessing import Process
from multiprocessing import Queue

from Queue import Empty as QueueEmptyException
from Queue import Full as QueueFullException

from math import sqrt
import argparse
import datetime
import time
import random


class Task(object):
    def __init__(self, task_desc):
        task_desc = task_desc.replace('\n', '')
        self._task_desc = task_desc

    def _repr_ans(self, answer):
        return str(answer) + '(' + self._task_desc + ')'

    def solve(self):
        raise NotImplementedError()


class IsPrimeTask(Task):
    def __init__(self, number, task_desc):
        self.number = int(number)
        super(IsPrimeTask, self).__init__(task_desc)

    def solve(self):
        num = self.number
        r = int(sqrt(self.number))
        ans = True
        for i in xrange(2, r + 1):
            if num % i == 0:
                ans = False
        return self._repr_ans(ans)


class EvenCountTask(Task):
    def __init__(self, args, task_desc):
        l, r = args.split(' ')
        self.l = int(l)
        self.r = int(r)
        super(EvenCountTask, self).__init__(task_desc)

    def solve(self):
        l = self.l if self.l % 2 == 0 else self.l + 1
        r = self.r
        if r < l:
            return self._repr_ans(0)
        return self._repr_ans((r - l + 1) / 2 + (1 - (r % 2)))


def get_task(task_desc):
    type_mapper = {
        'prime': IsPrimeTask,
        'even': EvenCountTask,
    }
    task_type, args = task_desc.split('?')
    task = type_mapper.get(task_type)
    if task is None:
        raise ValueError("Unknown task type.")
    return task(args, task_desc)


class Solver(Process):
    def __init__(self, filename=None, queue=None, *args, **kwargs):
        self._out_filename = filename
        self._out_file = None
        self._tasks = queue

        if 'target' in kwargs.keys():
            del kwargs['target']
        super(Solver, self).__init__(target=self._solve, *args, **kwargs)

    def run(self):
        with open(self._out_filename, 'w') as out_file:
            self._out_file = out_file
            while not self._tasks.empty():
                try:
                    task = self._tasks.get(False)
                except QueueEmptyException:
                    task = None
                self._solve(task)

    def _solve(self, task):
        # The first process can solve all tasks,
        # before the second process begins =\
        time.sleep(random.random())
        if self._out_file is not None and task is not None:
            self._out_file.write(task.solve() + '\n')


class SolverPool(object):
    def __init__(self, solvers_count):
        # The queue must be imported from multiprocessing
        self.queue = Queue()
        self.solvers = self._create_solvers(solvers_count)

    def _create_solvers(self, count):
        template = "task%d.out"
        return [Solver(filename=template % (num + 1), queue=self.queue)
                for num in xrange(count)]

    def add_task(self, task):
        if not isinstance(task, Task):
            return
        try:
            self.queue.put(task)
        except QueueFullException:
            pass

    def start(self):
        for solver in self.solvers:
            solver.start()
        for solver in self.solvers:
            solver.join()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-in', '--input', type=str, dest='input_file',
                        help='Input filename.', default='input.txt')
    parser.add_argument('-p', '--processes', type=int, dest='process_count',
                        help='Process count.', default=2)
    return parser.parse_args()


def main():
    args = parse_args()

    solver_pool = SolverPool(args.process_count)

    with open(args.input_file, 'r') as f:
        for line in f:
            solver_pool.add_task(get_task(line))

    start = datetime.datetime.today()
    solver_pool.start()
    finish = datetime.datetime.today()
    print finish - start


if '__main__' == __name__:
    main()
