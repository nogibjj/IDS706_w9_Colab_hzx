from mylib.lib import (
    read_dataset,
    general_summary,
    plot_histogram,
    plot_boxplot,
    plot_count,
    plot_scatter,
)

import matplotlib.pyplot as plt


def test_plot_boxplot():
    path = "CardioGoodFitness.csv"
    dfm = read_dataset(path)
    plot_boxplot(dfm)
    assert plt.gcf() is not None


def test_plot_histogram():
    path = "CardioGoodFitness.csv"
    dfm = read_dataset(path)
    plot_histogram(dfm)
    assert plt.gcf() is not None


def test_plot_count():
    path = "CardioGoodFitness.csv"
    dfm = read_dataset(path)
    plot_count(dfm)
    assert plt.gcf() is not None


def test_plot_scatter():
    path = "CardioGoodFitness.csv"
    dfm = read_dataset(path)
    plot_scatter(dfm)
    assert plt.gcf() is not None


def test_general_summary():
    path = "CardioGoodFitness.csv"
    dfm = read_dataset(path)
    flag = general_summary(dfm)
    assert flag is True


def test_read_dataset():
    path = "CardioGoodFitness.csv"
    dfm = read_dataset(path)
    assert len(dfm) > 0


# @pytest.fixture
# def test_mock():
#     data = {
#         'Product': ['TM195', 'TM195', 'TM195', 'TM498', 'TM498', 'TM798', 'TM798', 'TM798'],
#         'Age': [18, 19, 19, 19, 20, 20, 21, 21],
#         'Gender': ['Male', 'Male', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male'],
#         'Education': [14, 15, 14, 12, 13, 14, 14, 13],
#         'MaritalStatus': ['Single', 'Single', 'Partnered', 'Single', 'Partnered', 'Partnered', 'Partnered', 'Single'],
#         'Usage': [3, 2, 4, 3, 4, 3, 3, 3],
#         'Fitness': [4, 3, 3, 3, 2, 3, 3, 3],
#         'Income': [29562, 31836, 30699, 32973, 35247, 32973, 35247, 32973],
#         'Miles': [112, 75, 66, 85, 47, 66, 75, 85]
#     }
#     df = pd.DataFrame(data)
#     return df


# def test_general_summary(test_mock, mocker):
#     mock_print = mocker.patch("test_lib.general_summary")
#     general_summary(test_mock)
#     mock_print.assert_called_once_with(test_mock)
#     assert plt.gcf() is not None

# def test_plot_histogram(test_mock, mocker):
#     mock_hist = mocker.patch("test_lib.plot_histogram")
#     plot_histogram(test_mock)
#     # assert mock_hist.call_count == 1
#     mock_hist.assert_called_once_with(test_mock)
#     assert plt.gcf() is not None


# def test_plot_boxplot(test_mock, mocker):
#     mock_boxplot = mocker.patch("test_lib.plot_boxplot")
#     plot_boxplot(test_mock)
#     # assert mock_boxplot.call_count == 1
#     mock_boxplot.assert_called_once_with(test_mock)
#     assert plt.gcf() is not None


# def test_plot_count(test_mock, mocker):
#     mock_count = mocker.patch("test_lib.plot_count")
#     plot_count(test_mock)
#     # assert mock_count.call_count == 1
#     mock_count.assert_called_once_with(test_mock)
#     assert plt.gcf() is not None

# def test_plot_scatter(test_mock, mocker):
#     mock_scatter = mocker.patch("test_lib.plot_scatter")
#     plot_scatter(test_mock)
#     mock_scatter.assert_called_once_with(test_mock)
#     assert plt.gcf() is not None


# if __name__ == "__main__":
#     path = "/workspaces/IDS706_w3_Individual_Project1/data/CardioGoodFitness.csv"
#     test_read_dataset(path)
#     print("Everything passed")
