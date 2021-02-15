import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection

dataset = pandas.read_csv('iris.csv')
dataset.head() #to check the first 10 rows of the data set
dataset.tail() #to check out last 10 row of the data set
dataset.describe() #to give a statistical summary about the dataset

# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

# histograms
dataset.hist()
plt.show()


# scatter plot matrix
scatter_matrix(dataset)
plt.show()


# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
