#! /usr/bin/env python

import sys

def count(str):
  def ins(hm, char):
    if char in hm:
      hm[char] += 1
    else:
      hm[char] = 1
    return hm
  return reduce(ins, str, {})


def check_argv():
  l = len(sys.argv) - 1
  if l != 1:
    print "wrong number of arguments: expected 1, found {}".format(l)
    sys.exit(1)


check_argv()
for (k, v) in sorted(count(sys.argv[1]).items(), key= lambda tup: tup[0]):
  print "{} : {}".format(k,v)
