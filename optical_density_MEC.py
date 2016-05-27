# optical_density_MEC.py v1.0

# by William H. Grover, Department of Bioengineering
# University of California, Riverside
# wgrover@engr.ucr.edu
# http://groverlab.org

# Copyright (c) 2016 Regents of the University of California.  Permission is
# hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions: The above copyright notice and this
# permission notice shall be included in all copies or substantial portions of
# the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO
# EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES
# OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

# Usage:  This program expects to be run in the same directory as the folder
# named "yeast data from optical density MEC" containing binary data from the
# optical density Multifluidic Evolutionary Component (MEC).  When this program
# is run, it reads in this raw data, filters it using a median filter, and shows
# a plot of voltage vs. time.

# Dependencies:
#   Python 2.X (http://www.python.org)
#   Numpy (http://www.numpy.org)
#   Scipy (http://www.scipy.org)
#   Matplotlib (http://matplotlib.org)

# The latest version of this program is available at
# https://github.com/groverlab/optical_density_MEC

import numpy, pylab, os.path, scipy.signal

# read raw data from files containing paired measurements of voltage and time
dir = "yeast data from optical density MEC"
voltages = numpy.array([])  # empty array to store voltage data
times = numpy.array([])  # empty array to store time data
for candidate in os.listdir(dir):
	if candidate.endswith("V"):  # if file contains voltage data
		file = os.path.join(dir, candidate)
		voltages = numpy.append(voltages, numpy.fromfile(file, dtype='>f8'))
	elif candidate.endswith("T"): # if file contains time data
		file = os.path.join(dir, candidate)
		times = numpy.append(times, numpy.fromfile(file, dtype='>f8'))

# median filter of voltage data to reduce noise
voltages = scipy.signal.medfilt(voltages, kernel_size=101)

# plot a subset of the data centered on growth period
voltages = voltages[100000:700000]
times = times[100000:700000]

# create and customize the plot of voltage vs. time
pylab.figure(figsize=(5,4)) # good size for paper
pylab.plot(times/(60*60), voltages, "k-", linewidth=2)
pylab.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.15)
pylab.xlabel("Time (hours)", fontweight='bold')
pylab.ylabel("""Optical absorbance MEC voltage (V)
    (proportional to optical density)""", 
    fontweight='bold', multialignment='center')
pylab.xlim(3,24)
pylab.yticks(numpy.arange(1.2, 1.6, 0.1))
pylab.gca().invert_yaxis()
pylab.show()


