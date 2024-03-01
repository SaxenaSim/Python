numbers = list(range(1,1001))
divisors = list(range(2,10))

ans = [n for n in numbers if any([ n % d == 0 for d in divisors])]
print(ans)