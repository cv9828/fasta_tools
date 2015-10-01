#!/usr/bin/env python

# Command line script to calculate base frequency from a .fasta file

import sys

a_count = 0
c_count = 0
g_count = 0
t_count = 0
total_count = 0

with open(sys.argv[1], 'r') as fasta:

    for line in fasta:
        if line.startswith(">"):
            # Header line, skip it
            continue
        a_count = line.count("A")
        c_count = line.count("C")
        g_count = line.count("G")
        t_count = line.count("T")

total_count = a_count + c_count + g_count + t_count
#here is where the word count looks weird


#        for base in line.strip():
#            if base == "A":
#                a_count += 1
#            elif base == "C":
#                c_count += 1
#            elif base == "G":
#                g_count += 1
#            elif base == "T":
#                t_count += 1

print("Base counts for file %s:" % sys.argv[1])
print("A: %d" % a_count)
print("C: %d" % c_count)
print("G: %d" % g_count)
print("T: %d" % t_count)
#now for percentages
print("Percentages: ")
print("A: %d" % a_count / total_count)
print("C: %d" % c_count / total_count)
print("G: %d" % g_count / total_count)
print("T: %d" % t_count / total_count)
print("CG: %d" % (c_count + g_count) / total_count)
