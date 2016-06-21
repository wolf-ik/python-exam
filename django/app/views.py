import json

from django.shortcuts import render
from .models import GcdModel
from .models import PrimeModel


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def solve_gcd(left, right):
    results = []
    for x in xrange(left, right + 1):
        for y in xrange(left, right + 1):
            results.append({
                'x': x,
                'y': y,
                'gcd': gcd(x, y),
            })
    return {'results': results}


def gcd_view(request, left, right):
    left = int(left)
    right = int(right)
    try:
        cached = GcdModel.objects.get(left=left, right=right)
    except GcdModel.DoesNotExist:
        cached = None
    if cached:
        return render(request, 'gcd.html', context=json.loads(cached.ans))
    ans = solve_gcd(left, right)
    GcdModel.objects.create(left=left, right=right, ans=json.dumps(ans))
    return render(request, 'gcd.html', context=ans)


def solve_prime(n):
    results = []
    used = [False for i in xrange(n + 2)]
    for i in xrange(2, n + 1):
        if not used[i]:
            results.append(i)
            j = i * i
            while j <= n:
                used[j] = True
                j += i
    return {'results': results}


def prime_view(request, n):
    n = int(n)
    try:
        cached = PrimeModel.objects.get(n=n)
    except PrimeModel.DoesNotExist:
        cached = None
    if cached:
        return render(request, 'prime.html', json.loads(cached.ans))
    ans = solve_prime(n)
    PrimeModel.objects.create(n=n, ans=json.dumps(ans))
    return render(request, 'prime.html', ans)
