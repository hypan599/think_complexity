from Cdf import Cdf
import matplotlib.pyplot as plt


def plot_ccdf():
    pass

cdf = Cdf()
cdf.from_list(1, 2, 2, 4, 5)
print(cdf.values)
print(cdf.probabilities)
print(cdf.render())