import matplotlib.pyplot as plt
import numpy as np


def main(input_filename, output_filename):
    plt.figure()
    data = np.loadtxt(input_filename)
    plt.hist(data)
    plt.savefig(output_filename)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Takes a file containing numbers and plots a hist.")
    parser.add_argument("input", help="a numpy .txt file containing the data.")
    parser.add_argument("output", help="a png file containing the plot")
    args = parser.parse_args()

    main(input_filename=args.input, output_filename=args.output)