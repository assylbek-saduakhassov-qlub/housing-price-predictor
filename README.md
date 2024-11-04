# housing-price-predictor

# Housing Price Prediction

## Project Overview

This project aims to predict housing prices based on features like area and the number of bedrooms using gradient descent. The dataset is normalized, and then the gradient descent algorithm is used to find the optimal weights that minimize the cost function. The primary goal of this project is to explore the use of linear regression with gradient descent to create a simple prediction model.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries listed in `requirements.txt`

To install the dependencies, run:

```bash
pip install -r requirements.txt
```

### Directory Structure

The project directory is organized as follows:

```
housing-price-prediction/
├── data/
│   ├── housing.txt
│   └── normalized.txt
├── src/
│   ├── data_preprocessing.py
│   ├── gradient_descent.py
│   └── main.py
├── plots/
├── README.md
├── requirements.txt
├── .gitignore
└── config.json
```

- `data/`: Contains the input data files for the project.
- `src/`: Contains the source code for data preprocessing, gradient descent, and main script.
- `plots/`: Stores any generated plots from training.
- `README.md`: This file, explaining the project.
- `requirements.txt`: Python dependencies.
- `config.json`: Configuration file for setting up parameters.

### Running the Project

To run the project, use the following command:

```bash
python src/main.py
```

This script will normalize the dataset, perform gradient descent, and predict the price for a sample input.

## How the Code Works

### 1. Data Preprocessing

The `data_preprocessing.py` file contains functions to normalize the data. The data is read from `housing.txt`, which includes features like area and the number of bedrooms along with the corresponding price. The data is normalized using the z-score normalization technique.

### 2. Gradient Descent

The `gradient_descent.py` file contains the implementation of gradient descent to learn the weights of a linear model. It takes in the learning rate, number of iterations, and training data and returns the optimal weights that minimize the cost function.

### 3. Main Script

The `main.py` file is the main entry point for the project. It reads and normalizes the data, runs gradient descent, and outputs the optimal weights. It also uses the learned weights to make predictions for a given test input.

## Example Usage

The project reads data from `housing.txt`, which contains housing data in the following format:

```
area,bedrooms,price
2104,3,399900
1600,3,329900
2400,3,369000
...
```

The model normalizes this data and then performs gradient descent to learn the relationship between area, number of bedrooms, and the price of a house.

## Documentation

### `data_preprocessing.py`

#### `get_mean_stddev(numbers)`

Calculates the mean and standard deviation for a given list of numbers.

- **Parameters**:
  - `numbers` (list): A list of numerical values.
- **Returns**:
  - `mean` (float): The mean of the input numbers.
  - `std_dev` (float): The standard deviation of the input numbers.

#### `calculate_normalized_data(numbers)`

Normalizes a list of numbers using z-score normalization.

- **Parameters**:
  - `numbers` (list): A list of numerical values.
- **Returns**:
  - `normalized_data` (list): Normalized values.
  - `mean` (float): The mean of the input numbers.
  - `std_dev` (float): The standard deviation of the input numbers.

#### `create_normalized_data(housing_txt, output_file)`

Reads the housing data, normalizes it, and writes the normalized data to an output file.

- **Parameters**:
  - `housing_txt` (str): The input file path containing housing data.
  - `output_file` (str): The output file path to write the normalized data.
- **Returns**:
  - `feature_mean_std_dev` (dict): A dictionary containing mean and standard deviation for each feature.

### `gradient_descent.py`

#### `gradient_descent(alpha, num_iters, data)`

Performs gradient descent to learn the weights for a linear model.

- **Parameters**:
  - `alpha` (float): The learning rate.
  - `num_iters` (int): Number of iterations.
  - `data` (tuple): A tuple containing the features and target values.
- **Returns**:
  - `w0, w1, w2` (float): The weights learned by gradient descent.
  - `J_history` (list): The history of cost function values.

### `main.py`

The main script orchestrates the entire flow from data normalization, training using gradient descent, and making predictions for given inputs.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request. For major changes, please open an issue to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions, feel free to reach out via GitHub.

