from nose.tools import *

def avg_line(line):
    values = line.split(',')
    count = 0
    total = 0
    for value in values:
        total += int(value)
        count += 1
    return total / count

def min_avg(file_name,*args):
    if len(*args)>0:
            
    contents = open(file_name)
    averages = []
    for (i, line) in enumerate(contents):
        averages.append((avg_line(line), i))
    contents.close()
    averages.sort()
    min_avg, experiment_number = averages[0]
    return experiment_number
