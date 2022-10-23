import numpy as np
import matplotlib.pyplot as plt


def main(data_filename, fig_filename):
    data = np.loadtxt(data_filename)
    plt.figure()
    plt.hist(data.flatten(), bins=args.bins)
    plt.gcf().savefig(fig_filename)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="asfda")
    parser.add_argument("input", help="a txt file containing the data")
    parser.add_argument("output", help="the output image filename")
    parser.add_argument("--bins", default=7, type=int, help="number of bins in the histogram")
    args = parser.parse_args()

    main(data_filename=args.input, fig_filename=args.output)