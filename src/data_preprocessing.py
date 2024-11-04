import csv
import math

def get_mean_stddev(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    avg_dist_sqr = sum((n - mean) ** 2 for n in numbers)
    std_dev = math.sqrt(avg_dist_sqr / count)
    return mean, std_dev

def calculate_normalized_data(numbers):
    mean, std_dev = get_mean_stddev(numbers)
    normalized_data = [(n - mean) / std_dev for n in numbers]
    return normalized_data, mean, std_dev

def create_normalized_data(housing_txt, output_file):
    try:
        with open(housing_txt, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            areas, bedrooms, prices = [], [], []
            for row in csv_reader:
                areas.append(float(row[0]))
                bedrooms.append(float(row[1]))
                prices.append(float(row[2]))

        areas_normalized, area_mean, area_std_dev = calculate_normalized_data(areas)
        bedrooms_normalized, bedrooms_mean, bedrooms_std_dev = calculate_normalized_data(bedrooms)
        prices_normalized, prices_mean, prices_std_dev = calculate_normalized_data(prices)

        with open(output_file, 'w', newline='') as file1:
            csv_writer = csv.writer(file1)
            csv_writer.writerow(["area", "bedrooms", "price"])
            for area, bedroom, price in zip(areas_normalized, bedrooms_normalized, prices_normalized):
                csv_writer.writerow([area, bedroom, price])

        feature_mean_std_dev = {
            'area': {'mean': area_mean, 'std_dev': area_std_dev},
            'bedrooms': {'mean': bedrooms_mean, 'std_dev': bedrooms_std_dev},
            'price': {'mean': prices_mean, 'std_dev': prices_std_dev},
        }

        return feature_mean_std_dev

    except FileNotFoundError:
        print(f"The file {housing_txt} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
