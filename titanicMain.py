import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
titanic_df = pd.read_csv('train.csv')


titanic_df.drop(['Parch','PassengerId','Name','Ticket'], axis=1, inplace=True)


titanic_df["Embarked"] = titanic_df["Embarked"].fillna("S")
print("======Data Headers After Filling with default value for Embarked Column =======")
print(titanic_df.head(5))


print("Visualization #1 : Survival Rate Based on Passenger Sitting Class")
ax = sns.countplot(x = 'Pclass', hue = 'Survived', palette = 'Set1',data = titanic_df)
ax.set(title = 'Passenger status (Survived/Died) against Passenger Class',
       xlabel = 'Passenger Class', ylabel = 'Total')
plt.show() 


print("Visualization #2 : Survival Rate Based on Gender")
ax = sns.countplot(x = 'Sex', hue = 'Survived', palette = 'Set2', data = titanic_df)
ax.set(title = 'Total Survivors According to Sex', xlabel = 'Sex', ylabel='Total')
plt.show()


print("Visualization #3 : Survival Rate Based on Passenger Age Group")
interval = (0,18,35,60,120)
categories = ['Children','Teens','Adult', 'Old']
titanic_df['Age_cats'] = pd.cut(titanic_df.Age, interval, labels = categories)
ax = sns.countplot(x = 'Age_cats',  data = titanic_df, hue = 'Survived', palette = 'Set3')
ax.set(xlabel='Age Categorical', ylabel='Total',
       title="Age Categorical Survival Distribution")
plt.show()