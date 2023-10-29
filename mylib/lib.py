import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_dataset(path):
    cardio_data = pd.read_csv(path)
    return cardio_data

def general_summary(cardio_data):
    print("The first five lines of the dataset\n")
    print(cardio_data.head())
    print("The descriptive statistics of the CardioGoodFitness dataset\n")
    print(cardio_data.describe().T)
    print("The info of the CardioGoodFitness dataset\n")
    print(cardio_data.info())
    print("The shape of the CardioGoodFitness dataset\n")
    print(cardio_data.shape)
    return True

def plot_boxplot(cardio_data):
    plt.figure()
    sns.boxenplot(x='Gender',y='Age',data=cardio_data)

# flag means whether in the python script or not
def plot_histogram(cardio_data):
    cardio_data.hist(figsize=(15,15))

def plot_count(cardio_data):
    plt.figure()
    sns.countplot(x="Product", hue="Gender", data=cardio_data)        


def plot_scatter(cardio_data):
    _, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10,10))
    sns.scatterplot(x='Age', y='Income', data=cardio_data, hue='Product', ax=ax1)
    sns.scatterplot(x='Age', y='Fitness', data=cardio_data, hue='Product', ax=ax2)
    sns.scatterplot(x='Age', y='Usage', data=cardio_data, hue='Product', ax=ax3)
    sns.scatterplot(x='Age', y='Miles', data=cardio_data, hue='Product', ax=ax4)
    ax1.set_title('Plot 1')
    ax2.set_title('Plot 2')
    ax3.set_title('Plot 3')
    ax4.set_title('Plot 4')
    plt.tight_layout()
        