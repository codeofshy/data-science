# we can run the python file using terminal
# cd to the current folder >>> python {name-of-fil}

import matplotlib.pyplot as plt

# plot1 = plt.plot([1,2,3], [4,5,6])
# plot1.show()

# plt.plot([1,2,3], [4,5,6])
# plt.show()


# ================= Sachin runs
# years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
# runs =  [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]

# plt.plot(years, runs)
# plt.xlabel("Runs")
# plt.ylabel("Years")
# plt.title("Sachin's Runs vs Years")
# plt.show()

# ================ Kohli x sehwag
years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
kohli = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]
sehwag = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0]

plt.plot(years, kohli, label="Kohli's Score")
plt.plot(years, sehwag, label="Sehwag's Score")

plt.xlabel("Years")
plt.ylabel("Runs")
plt.title("Performance card")
plt.legend()
plt.show()