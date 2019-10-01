import pandas as pd

# Question1#######################################################
data = pd.read_csv('Automobile_data.csv')
print(data.head(5))
print(data.tail(5))

# Question2#######################################################
data = data.replace('', 'NaN', regex=True)
data.to_csv('updated_automobile_data.csv', na_rep='NaN')

# Question3#######################################################
ind = data['price'].idxmax()
print(data['company'][ind], data['price'].max())

# Question4#######################################################
print(data[data['company'] == 'toyota'])

# Question5#######################################################
print(data['company'].value_counts())

# Question6#######################################################
print(data.groupby(['company'])['price'].max())

# Question7#######################################################
print(data.groupby(['company'])['average-mileage'].mean())

# Question8#######################################################
data.sort_values(by='price', inplace=True, ascending=False)
print(data)

# Question9#######################################################
german_cars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925, 71400]}
japanese_cars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'], 'Price': [29995, 23600, 61500, 58900]}
german_cars_df = pd.DataFrame.from_dict(german_cars)
german_cars_df['Country'] = 'Germany'
japanese_cars_df = pd.DataFrame.from_dict(japanese_cars)
japanese_cars_df['Country'] = 'Japan'
german_japanese_df = pd.concat([german_cars_df, japanese_cars_df])
print(german_japanese_df)

# Question10#######################################################
car_price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
car_horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Horsepower': [141, 80, 182, 160]}
car_price_df = pd.DataFrame.from_dict(car_price)
car_horsepower_df = pd.DataFrame.from_dict(car_horsepower)
car_total_df = pd.merge(car_price_df, car_horsepower_df)
print(car_total_df)
