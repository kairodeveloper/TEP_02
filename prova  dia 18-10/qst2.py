import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

df = pd.read_csv('train.csv')


"""

#a
survived = (df[df['Survived'] == 1]['Name'])
print(survived)


#b
survived_count = len(survived)
all_count = len(df)
rate_survived = (100 / all_count) * survived_count
print(round(rate_survived,2))


#d
new_df = df.drop(df[df['Embarked'].isnull()].index)
print(new_df['Embarked'].isnull().sum())

"""

df = df.replace(['male', 'female'], [0,1])
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['isAlone'] = np.where(df['FamilySize'] > 1, 1,0)

df_x = df[['Sex','isAlone','Embarked','Pclass']]
df_x = pd.get_dummies(df_x)

df_y = df[['Survived']]



x_treino, x_teste, y_treino, y_teste = train_test_split(df_x, df_y, test_size=0.20, random_state=0)

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(x_treino, y_treino)

print(modelo.score(x_teste, y_teste))


