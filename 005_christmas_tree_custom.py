#! /usr/bin/env python

import os
import sys

def print_top(height):
  for i in xrange(0, height):
    format_spaces = '{0: ^' + str(height - i - 1) + '}'
    format_stars  = '{0:*^' + str(i * 2 + 1) + '}'
    print (format_spaces + format_stars).format('')


def print_trunk(height):
  width = (height / 5) * 2 + 1
  format_spaces = '{0: ^' + str((max_width(height) - width) / 2) + '}'
  format_stars  = '{0:*^' + str(width) + '}'
  level = (format_spaces + format_stars).format('')
  for i in xrange(0, height / 2 + 1):
    print level


def max_width(height):
  return (height - 1) * 2 + 1


def check_argv():
  l = len(sys.argv) - 1
  if l != 1:
    print "wrong number of arguments: expected 1, found {}".format(l)
    sys.exit(1)


def check_height(height):
  _, columns = map(int, os.popen('stty size', 'r').read().split())
  if (height < 2) or (max_width(height) > columns) :
    max_height = str((columns - 1) / 2 + 1)
    err_str = "{} is outside acceptable range (2-{}) and would look bad"
    print err_str.format(height, max_height)
    sys.exit(1)


check_argv()
height = int(sys.argv[1])
check_height(height)
print_top(height)
print_trunk(height)
