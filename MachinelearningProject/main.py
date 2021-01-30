import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as plt

data = pd.read_csv("Dataset.csv", sep=",")

data = data[["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"]]

predict = "Insulin"

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

maximum = 0
for x in range(20):

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print(acc)
    if acc > maximum:
        maximum = acc
print('Maximum accuracy is: ', maximum)

print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)

predictions = linear.predict(x_test)
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()