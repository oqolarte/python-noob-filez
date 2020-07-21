#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prime_factorization.py
#  

def primes(n): #returns a list of prime factors
	primfac = []
	d = 2
	while d*d <= n:
		while (n % d) == 0:
			primfac.append(d)  # supposing you want multiple factors repeated
			n //= d
		d += 1
	if n > 1:
		primfac.append(n)
	return primfac

print(primes(int(input('Type an integer to get its prime factors: '))))
