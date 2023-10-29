from mylib.lib import plot_count, plot_scatter, plot_histogram

# from mylib.lib import read_dataset

import matplotlib.pyplot as plt


def save_plot_count(cardio_data):
    plot_count(cardio_data)
    plt.savefig("./results/count.png")


def save_plot_histogram(cardio_data):
    plot_histogram(cardio_data)
    plt.savefig("./results/histogram.png")


def save_plot_scatter(cardio_data):
    plot_scatter(cardio_data)
    plt.savefig("./results/scatter.png")


# if __name__ == "__main__":
#     import os,sys
#     print(sys.path)
#     print(os.getcwd())
#     os.chdir('/workspaces/IDS706_Individual_Proj1_ZH')
#     sys.path.append("/workspaces/IDS706_w3_Individual_Project1")
#     PATH = "./CardioGoodFitness.csv"
#     save_plot_count(read_dataset(PATH))
