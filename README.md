
# Mutual Fund Return Prediction

This project predicts the 3-year return for mutual funds based on various financial metrics using machine learning. It evaluates the performance of multiple regression models and compares their efficiency.

## Table of Contents

1. [Overview](#overview)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Data Preprocessing](#data-preprocessing)
5. [Model Evaluation](#model-evaluation)
6. [Learnings from the Data](#learnings-from-the-data)
7. [Contributing](#contributing)

## Overview

The goal of this project is to predict the 3-year returns of mutual funds based on historical performance data. Various regression algorithms have been applied and evaluated to select the best-performing model. Additionally, outlier detection and capping methods have been applied to improve model stability and prevent overfitting.

## Technologies

* Python
* pandas
* numpy
* seaborn
* matplotlib
* scikit-learn
* joblib

## Installation

To run this project, you’ll need to have Python and the required libraries installed. You can install all the necessary dependencies by using `pip` with the following command:

```bash
pip install -r requirements.txt
```

### Requirements.txt

```txt
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
```


* Handle missing values
* Apply encoding to categorical variables like `Market Cap`, `Type`, `Risk`, and `Star Rating`
* Treat outliers (optional: capping based on IQR)


Multiple regression models are trained and evaluated. The models include:

* **Linear Regression**
* **Random Forest Regressor**
* **Gradient Boosting Regressor**
* **Decision Tree Regressor**
* **Support Vector Regressor**

## Data Preprocessing

1. **Outlier Handling:** Outliers in `1YrReturn%`, `5YrReturn%`, `Sharpe Ratio`, and `Expense Ratio` were capped using the IQR method to reduce the influence of extreme values.

2. **Encoding:** Ordinal encoding was applied to the categorical features (`Market Cap`, `Type`, `Risk`, and `Star Rating`) to convert them into numerical values for use in regression models.

3. **Normalization/Standardization:** Features were standardized where required to ensure consistency across the models.

## Model Evaluation

Multiple regression models were tested to predict the 3-year return of the mutual funds. The models were evaluated using the following metrics:

* **Root Mean Squared Error (RMSE)**
* **Mean Absolute Error (MAE)**
* **R² Score**

### Results:

| Model                    | RMSE  | MAE   | R² Score |
| ------------------------ | ----- | ----- | -------- |
| Random Forest            | 1.062 | 0.727 | 0.855    |
| Gradient Boosting        | 1.166 | 0.778 | 0.826    |
| Linear Regression        | 1.236 | 0.662 | 0.804    |
| Decision Tree            | 1.482 | 0.969 | 0.718    |
| Support Vector Regressor | 2.701 | 2.137 | 0.063    |

The **Random Forest Regressor** performed the best based on **R² Score** and **RMSE**.

## Learnings from the Data

* **Sharpe Ratio** has a strong positive correlation with returns, making it a good risk-adjusted performance indicator.
* Funds with **higher Expense Ratios** generally showed **lower returns**, indicating the importance of low-cost funds for long-term investments.
* **Star Ratings** had a moderate relationship with returns, suggesting that it is not the sole factor to base investment decisions on.
* **Market Cap** and **Fund Type** influenced returns, with **Large Cap** funds being more stable but with lower returns compared to **Mid and Small Cap** funds.

## Contributing

Contributions are welcome! If you want to contribute to this project, feel free to fork the repository and submit a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Let me know if you'd like to make any changes to the README or add further details!
