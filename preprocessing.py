import pandas as pd


# Import dataset
data = pd.read_csv('water_potability.csv')
data = pd.DataFrame(data)


# PRE PROCESSING

# Check how many missing values
print("Missing values:\n", data.isnull().sum())

# Check skewness
skewness = data.skew()
print("\nph skewness: ", skewness['ph'])
print("Sulfate skewness: ", skewness['Sulfate'])
print("Trihalomethanes skewness: ", skewness['Trihalomethanes'])

# Since skewness was close to 0, we will replace missing values the mean value
columns_to_fill = ['Sulfate', 'ph', 'Trihalomethanes']

for column in columns_to_fill:
    data[column].fillna(data[column].mean(), inplace=True)


# Round values to three decimals
data = data.round(3)
# Round the 'ph' column to one decimal
data['ph'] = data['ph'].round(1)


# Save updated csv file
data.to_csv('updated_water_potability.csv', index=False)
