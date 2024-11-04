import csv
from src.data_preprocessing import create_normalized_data
from src.gradient_descent import gradient_descent

housing_txt = "data/housing.txt"
output_file = "data/normalized.txt"

feature_mean_std_dev = create_normalized_data(housing_txt, output_file)

try:
    with open(output_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        areas, bedrooms, prices = [], [], []
        for row in csv_reader:
            areas.append(float(row[0]))
            bedrooms.append(float(row[1]))
            prices.append(float(row[2]))
except FileNotFoundError:
    print(f"The file {output_file} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
    
print("Gradient Descent to Find Weights:")
alphas = [0.01, 0.1, 0.2]
data = (areas, bedrooms, prices)

for i, alpha in enumerate(alphas):
    w0, w1, w2, J_history = gradient_descent(alpha, 100, data)
    print(f"Learning rate = {alpha}, Final Cost = {J_history[-1]}, Weights: w0 = {w0}, w1 = {w1}, w2 = {w2}")

# Predicting housing prices
test_area = 2650
test_bedrooms = 4
test_area = (test_area - feature_mean_std_dev['area']['mean']) / feature_mean_std_dev['area']['std_dev']
test_bedrooms = (test_bedrooms - feature_mean_std_dev['bedrooms']['mean']) / feature_mean_std_dev['bedrooms']['std_dev']
predicted_price = w0 + w1 * test_area + w2 * test_bedrooms
predicted_price = (predicted_price * feature_mean_std_dev['price']['std_dev']) + feature_mean_std_dev['price']['mean']
print(f"Predicted Price: {predicted_price}")
