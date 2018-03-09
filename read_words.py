"""count words from a text file and count them"""
import argparse
import string
import math
import matplotlib.pyplot as plt
from collections import defaultdict

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input text file")
    args = parser.parse_args()

    trans = str.maketrans(string.ascii_uppercase, string.ascii_lowercase, string.punctuation + string.digits)
    words = defaultdict(int)
    with open(args.input, "r") as f:
        for line in f:
            line = line.translate(trans).strip().split()
            for word in line:
                words[word] += 1

    plot_x = []
    plot_y = []
    rank = 1
    for w, f in sorted(words.items(), key=lambda x: x[1], reverse=True):
        plot_x.append(math.log(rank))
        plot_y.append(math.log(f))
        rank += 1

    plt.plot(plot_x, plot_y)
    # plt.xlim(0, 1)
    # plt.ylim(0, 4)
    plt.show()
