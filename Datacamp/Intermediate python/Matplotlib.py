import matplotlib.pyplot as plt

# A very simple plot
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.062, 3.265, 6.972]
plt.plot(year, pop)
plt.show()

plt.clf

#A simple histogram
values = [0,0.6,1.4,4.6,2.2,2.5,2.6,3.2,3.9,4.2,2.6]
plt.hist(values, bins=3)
plt.show()