import numpy
import pylab

mu, sigma = 2, 0.5
v = numpy.random.normal(mu, sigma, 10000)

pylab.hist(v, bins=50, normed=1)
pylab.show()

(n, bins) = numpy.histogram(v, bins=50, normed=True)

pylab.plot(.5*(bins[1:]+bins[:-1]), n)
pylab.show()