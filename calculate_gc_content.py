#!/usr/bin/env python

# Command line script to calculate base frequency from a .fasta file

import sys


def gc_content(file_path):
	""" this method counts the occurance and prints them.
	"""

	a_count = 0
	c_count = 0
	g_count = 0
	t_count = 0
	total_count = 0
	
	with open(file_path, 'r') as fasta:
	    
	    for line in fasta:
	        if line.startswith(">"):
	            # Header line, skip it
	            continue

	        a_count = a_count + line.count("A")  # add the counts from previous lines as well
	        c_count = c_count + line.count("C")  # otherwise it would just keep the counts of last line.
	        g_count = g_count + line.count("G")
	        t_count = t_count + line.count("T")

	total_count = a_count + c_count + g_count + t_count

	print("Base counts for file %s:" % sys.argv[1])
	print("A: %d" % a_count)
	print("C: %d" % c_count)
	print("G: %d" % g_count)
	print("T: %d" % t_count)

	#now for percentages
	print("\nPercentages: ")
        print("A: %s %%" %"{0:.2f}".format(float(a_count * 100) / total_count))
	print("C: %s %%" %"{0:.2f}".format(float(c_count * 100) / total_count))
	print("G: %s %%" %"{0:.2f}".format(float(g_count * 100) / total_count))
	print("T: %s %%" %"{0:.2f}".format(float(t_count * 100) / total_count))
	print("CG: %s %%" %"{0:.2f}".format(float((g_count + c_count) * 100) / total_count))


if __name__ == "__main__":
	if len(sys.argv) > 1:
		file_path = sys.argv[1]
		gc_content(file_path)
	else:
		print("No input file given!!!")
