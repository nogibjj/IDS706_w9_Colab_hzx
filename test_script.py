from main import *
import os
import pandas as pd

cardio_data = pd.read_csv("CardioGoodFitness.csv")


def test_save_plot_count():
    save_plot_count(cardio_data)
    assert os.path.exists("./results/count.png")


def test_save_plot_histogram():
    save_plot_histogram(cardio_data)
    assert os.path.exists("./results/histogram.png")


def test_save_plot_scatter():
    save_plot_scatter(cardio_data)
    assert os.path.exists("./results/scatter.png")


if __name__ == "__main__":
    pass
