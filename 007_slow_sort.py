#! /usr/bin/env python

import datetime
import random
import sys

def slow_sort(l):
  if len(l) < 2:
    return
  for i in xrange(0, len(l) - 1):
    iom = index_of_min(l, i + 1)
    if l[iom] < l[i]:
      tmp = l[i]
      l[i] = l[iom]
      l[iom] = tmp
  return

def index_of_min(l, start):
  iom = start
  for i in xrange(start + 1, len(l)):
    if l[i] < l[iom]:
      iom = i
  return iom

def time_delta_to_secs(td):
  return td.microseconds / float(1000000) + td.seconds

def test(size):
  list1 = [0] * size
  for i in xrange(0,size):
    list1[i] = random.randint(-1000000, 1000000)

  list2 = list(list1)

  end = (10 if len(list1) > 10 else len(list1))
  print('testing {} elements'.format(size))
  print('='* 50)
  print('list1 and list2 equal: {}'.format(list1 == list2))
  print('Slow Sort:')
  print('first elements of list1 before sorting: {}'.format(list1[0:end]))

  t1 = datetime.datetime.now()
  slow_sort(list1)
  t2 = datetime.datetime.now()
  slow_sort_time = time_delta_to_secs(t2 - t1)

  print('first elements of list1 after sorting: {}'.format(list1[0:end]))
  print('lists1 and list2 equal: {}'.format(list1 == list2))
  print('time to sort (slow_sort): {}\n'.format(slow_sort_time))

  print('Builtin Sort:')
  print('first elements of list2 before sorting: {}'.format(list2[0:end]))

  t1 = datetime.datetime.now()
  list2.sort()
  t2 = datetime.datetime.now()
  builtin_sort_time = time_delta_to_secs(t2 - t1)

  print('first elements of list2 after sorting: {}'.format(list2[0:end]))
  print('time to sort (builtin sort): {}\n'.format(builtin_sort_time))
  print('lists1 and list2 equal: {}'.format(list1 == list2))
  print('ratio of slow sort to builtin sort : {}\n'.format(slow_sort_time / builtin_sort_time))

test(0)
test(1)
test(10)
test(100)
test(1000)
test(10000)
