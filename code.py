import pandas as pd
df=pd.read_csv("LS_2.0.csv")
df.head()



#TO RENAME COLUMN NAMES
import numpy as np
import pandas as  pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("LS_2.0.csv")
df=df.rename(columns={"CRIMINAL\nCASES": "Criminal", "GENERAL\nVOTES": "Genral_votes","POSTAL\nVOTES":"Postal_votes","TOTAL\nVOTES":"Total_votes"})
df
df.head()



#TO MENTION ONLY THE COLUMNS
list(df.columns)


#TO DROP NONE ENTRIES
df=df.dropna()
df

#TO LIST THE EDUCATION OF CANDIDATES

df["EDUCATION"].value_counts()


#TO PLOT THE EDUCATION OF DIFFERENT CANDIDATES FOR BETTER ANALYSIS OF THEIR COMPETANCY


L3=list(df["EDUCATION"].value_counts().keys())
L4=list(df["EDUCATION"].value_counts())
sns.barplot(data=df,x=L4,y=L3)
plt.xlabel("count")
plt.ylabel("Education")
plt.title("Education Level of the Candidates")

#TO DISPLAY THE EDUCATIONAL DEGREE OF ONLY THE WINNING CANDIDATES

winner = df[df['WINNER']==1]
L5=list(winner["EDUCATION"].value_counts().keys())
L6=list(winner["EDUCATION"].value_counts())
sns.barplot(data=df,x=L6,y=L5)
plt.xlabel("WINNERS")
plt.ylabel("EDUCATION")
plt.title("Winning Candidates Educational Degree")


#TO DISPLAY THE DATA OF YOUNG WINNING CANDIDATES


youth=winner[winner["AGE"]<=30]
youth.head()


#to plot the age of winning candidates

sns.histplot(data=df,x="AGE")


#plotting party vs criminal cases
criminal_cases = df.groupby('PARTY')['Criminal'].sum().reset_index().sort_values('Criminal',ascending=False).head(30)
plt.title("PARTY Vs. Criminal cases")
sns.barplot(data=criminal_cases,x="Criminal",y="PARTY")
plt.xlabel("Criminal cases")
plt.ylabel("PARTY")


#no. of female winners
winner = df[df['WINNER']==1]
Female_winner=winner[winner["GENDER"]=="FEMALE"]
sns.histplot(data=Female_winner,y="PARTY")
plt.title("Female Winners from different Party")



#female winners state wise
sns.histplot(data=Female_winner,y="STATE")
plt.title("Female Winners from different States")



#to check which party has most senior leaders
senior=df[df["AGE"]>=60].PARTY.value_counts()
senior.head()


#plotting most senior leaders party wise
sns.barplot(x=senior["PARTY"][0:30],y=senior["index"][0:30])
plt.xlabel("count")
plt.ylabel("PARTY")
plt.title('Top 30 Political Parties having most Senior leaders')
plt.show()


#to check which party has youth leaders
youth=df[df["AGE"]<=30].PARTY.value_counts()
youth.head()


#to plot numbers of male winners
winner = df[df['WINNER']==1]
Male_winner=winner[winner["GENDER"]=="MALE"]
sns.histplot(data=Male_winner,y="PARTY",palette="ch:s=.25,rot=-.25")
plt.title("Male Winners from different Party")


#to plot male winners from different parties
sns.histplot(data=Male_winner,y="PARTY",palette="ch:s=.25,rot=-.25")
plt.title("Male Winners from different Party")

#total votes state statewise
votes=df.groupby("STATE")["Total_votes"]
votes.head()


caste=df["CATEGORY"].value_counts()
caste


bjp=df[df["PARTY"]=="BJP"].STATE.value_counts().reset_index()
inc=df[df["PARTY"]=="INC"].STATE.value_counts().reset_index()
ind=df[df["PARTY"]=="IND"].STATE.value_counts().reset_index()
bsp=df[df["PARTY"]=="BSP"].STATE.value_counts().reset_index()
cpi=df[df["PARTY"]=="CPI(M)"].STATE.value_counts().reset_index()
vba=df[df["PARTY"]=="VBA"].STATE.value_counts().reset_index()
aitc=df[df["PARTY"]=="AITC"].STATE.value_counts().reset_index()
sp=df[df["PARTY"]=="SP"].STATE.value_counts().reset_index()
mnm=df[df["PARTY"]=="MNM"].STATE.value_counts().reset_index()
ntk=df[df["PARTY"]=="NTK"].STATE.value_counts().reset_index()
sns.barplot(x=bjp["STATE"],y=bjp["index"])
plt.xlabel("count")
plt.ylabel("STATE")
plt.title('Spread of BJP party in states of India')
plt.show()



#to check spread of top indian parties from india
df['PARTY'].value_counts()[0:10]






