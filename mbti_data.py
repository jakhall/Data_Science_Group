import pandas as pd
#setting variable for loop
x=0

#reading in csv
new_data = pd.read_csv('mbti_1.csv')

#selecting the type column
newtype = new_data['type']

#adding new columns for each type
new_data['type1'] = listtype[0]
new_data['type2'] = listtype[1]
new_data['type3'] = listtype[2]
new_data['type4'] = listtype[3]

#assinging new columns to variables
Type1 = new_data['type1'] 
Type2 = new_data['type2'] 
Type3 = new_data['type3'] 
Type4 = new_data['type4'] 

#splitting the type column into new columns
for x in range(len(newtype)):
	listtype = list(newtype[x])
	Type1.iloc[x] = listtype[0]
	Type2.iloc[x] = listtype[1]
	Type3.iloc[x] = listtype[2]
	Type4.iloc[x] = listtype[3]
	x=x+1

print(new_data)
