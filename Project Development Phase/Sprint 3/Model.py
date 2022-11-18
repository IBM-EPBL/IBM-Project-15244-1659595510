# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import pickle

import warnings
warnings.filterwarnings('ignore')


data = pd.read_csv("./Data/autos_preprocessed.csv")

data.head()
data.shape

data.info()


def multiple_plot(feature):
    plt.figure(figsize=(10, 5))
    # plt.subplot(1,2,1)
    sns.countplot(x=feature)
    plt.title(f'{feature.name} count plot')

    plt.show()

for i in data.columns:
    multiple_plot(data[i])

for i in data.columns:
    print(data[i].value_counts())

data['brand'].value_counts()

from sklearn.preprocessing import LabelEncoder

label=LabelEncoder()

data['vehicleType']=label.fit_transform(data['vehicleType'])
data['gearbox']=label.fit_transform(data['gearbox'])

data['model']=label.fit_transform(data['model'])
data['fuelType']=label.fit_transform(data['fuelType'])

data['brand']=label.fit_transform(data['brand'])
data['notRepairedDamage']=label.fit_transform(data['notRepairedDamage'])




print(data)
data.head()

X=data.drop('price',axis=1)
Y=data['price']


from sklearn.model_selection import train_test_split


X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
X_train.shape,X_test.shape,y_train.shape,y_test.shape




from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor (n_estimators =1000, max_depth = 10, random_state = 34)


regressor.fit (X_train, np.ravel(y_train, order = 'C'))




# Creating a pickle file for the classifier
filename = 'Model/prediction-rfc-model.pkl'
pickle.dump(regressor, open(filename, 'wb'))


filename = 'Model/prediction-rfc-model.pkl'
classifier = pickle.load(open(filename, 'rb'))


'''data = np.array([[1,69,1,2,2,1,1,2,1,2,2,2,2,2,2]])
my_prediction = classifier.predict(data)

warnings.filterwarnings("ignore", category=DeprecationWarning)
print(my_prediction[0])

if my_prediction == 1:
    Answer = 'LUNGCANCER'


    print('Hello:According to our Calculations, You have LUNGCANCER')

else:
    Answer = 'No-LUNGCANCER'

    print('Congratulations!! You DON T have LUNG CANCER ')
    Prescription = 'Nill'''''