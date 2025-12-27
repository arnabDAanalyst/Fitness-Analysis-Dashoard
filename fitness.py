import numpy as np
import pandas as pd    

import matplotlib.pyplot as plt  

import seaborn as sns  

df=pd.read_csv("fitness_data.csv")

df.head(10)
df.info()

# 1.Count of members by Gender

plt.figure(figsize=(10,7))
sns.countplot(df,x='Gender') 
plt.title("Members by Gender") 
plt.show()


# 2. Membership Status distribution

plt.figure(figsize=(10,7))

df['Status'].value_counts().plot.pie(autopct='%1.1f%%', startangle=45) 

plt.title("Membership Status Distribution") 

plt.show()



# 3.BMI by Goal 

plt.figure(figsize=(10,7))

sns.barplot(df,x='Goal', y='BMI',order=['Muscle Gain','Maintenance','Weight Loss']) 

plt.title("BMI by Goal Type") 

plt.show()


# 4.Average BMI by Gender 

df.groupby('Gender')['BMI'].mean().reset_index() 
sns.barplot(df,x='Gender', y='BMI',order=['Male','Female']) 
plt.title("Average BMI by Gender") 
plt.show() 


# 5. Membership duration (start to end)

df['MembershipStart'] = pd.to_datetime(df['MembershipStart']) 

df['MembershipEnd'] = pd.to_datetime(df['MembershipEnd']) 

df['Duration_Days'] = (df['MembershipEnd'] - df['MembershipStart']).dt.days 

plt.figure(figsize=(10,7))

sns.scatterplot(df,x='UserName', y='Duration_Days') 

plt.title("Membership Duration per User") 

plt.show()


# 6.  Members by Trainer Name
 
df['Trainer_Name'].value_counts().index 

plt.figure(figsize=(10,7))

sns.countplot(df,y='Trainer_Name')

plt.title("Members Trained by Each Trainer") 
plt.show()


# 7.Weight vs Height 

plt.figure(figsize=(10,7))

sns.scatterplot(df,x='Height_cm',y='StartingWeight', 
hue='Gender') 

plt.title("Height vs Starting Weight") 
plt.show() 