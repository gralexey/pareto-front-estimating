# -*- coding: utf8 -*-

from os import sys
from math import sqrt

if len(sys.argv) < 3:
	print "Too less arguments, give filename as first arg, problemname as second. You can also give step of search as 3rd arg and e of error as 4rd arg"
	exit()

step = 0.00001
if len(sys.argv) > 3:
	step = float(sys.argv[3])

e = 0.1
if len(sys.argv) == 5:
	step = float(sys.argv[4])

file_with_archive = sys.argv[1]
problem = sys.argv[2]

if (problem == 'zdt1'):									# В зависимости от тестовой задачи загружаем функцию определения расстояния точки до фронта (dist), 
	from zdt1 import dist, get_F_from_X, f2, x2			# функцию трансформирования входных данных в виде множества Парето в данные, представляющие фронт Парето (get_F_from_X),
if (problem == 'zdt2'):									# функцию точного фронта Парето (f2), функцию точного множества Парето (x2) 
	from zdt2 import dist, get_F_from_X, f2, x2
if (problem == 'zdt3'):
	from zdt3 import dist, get_F_from_X, f2, x2
if (problem == 'zdt4'):
	from zdt4 import dist, get_F_from_X, f2, x2
if (problem == 'zdt6'):
	from zdt6 import dist, get_F_from_X, f2, x2

from read_from_file	import *								# Следующая функция read_from_file определена в файле read_from_file.py

x_vectors = read_from_file(file_with_archive)				# Вектора X, представляющие собой множество Парето
f_vectors = get_F_from_X(x_vectors)							# Вектора F, представляющие собой множество Парето
archive_potency = len(f_vectors)

def min_dist_to_dot(f1s, f2s, step):	
	f1 = 0.0001
	min_residual = 100;
	while f1 <= 1:
		residual = dist(f1, f1s, f2s)
		if (residual < min_residual):
			min_dist = residual
			min_residual = residual
		f1 += step
	return min_dist

# Error Ratio indicator
summ = 0
for f_vector in f_vectors:
	d = min_dist_to_dot(f_vector[0], f_vector[1], step)		# minimum distance to front
	if d > e:
		summ += 1
result = summ / float(archive_potency)
print "Problem: ", problem, " I_ER = %f" % result	