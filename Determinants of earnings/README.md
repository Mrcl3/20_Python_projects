# The National Longitudinal Survey of Youth 1997-2011

The National Longitudinal Survey of Youth 1997-2011 dataset is a valuable resource for social scientists working with US data. This dataset contains information on a sample of young people who were born between 1980 and 1984 and who were between the ages of 12 and 17 in 1997. The dataset includes information on a wide range of variables, including demographic information, educational attainment, employment status, and health behaviors.

This project uses multivariable regression and random forest models to predict earnings based on two predictor variables: years of education and work experience. 

## Getting Started

To get started with this project, you will need to download the National Longitudinal Survey of Youth 1997-2011 dataset. You can download the dataset from the Bureau of Labor Statistics website (https://www.bls.gov/nls/y97data.htm). 

Once you have downloaded the dataset, you can run the Jupyter notebook file (`earnings_prediction.ipynb`) to explore the dataset and train the models.

## Prerequisites

To run the Jupyter notebook file, you will need to have Python installed on your computer. You will also need to install the following Python packages:

- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn

You can install these packages using pip or conda.

## Running the Code

To run the Jupyter notebook file, open a terminal or command prompt and navigate to the directory where the `earnings_prediction.ipynb` file is located. Then, enter the following command:

```
jupyter notebook earnings_prediction.ipynb
```

This will open the Jupyter notebook in your web browser. You can then run each cell in the notebook to explore the dataset and train the models.

## Results

The multivariable regression model had an R-squared value of 0.1, indicating that the model explains only a small proportion of the variance in the target variable (earnings).

The random forest model, on the other hand, had an R-squared value of 0.9, indicating that the model explains a larger proportion of the variance in the target variable. The model also had a lower mean squared error (MSE), mean absolute error (MAE), and root mean squared error (RMSE) compared to the multivariable regression model, indicating better overall performance.

## Conclusion

In conclusion, the random forest model outperformed the multivariable regression model in predicting earnings based on years of education and work experience. However, there may be other variables that could be included in the model to improve its performance. Further research and analysis could be done to identify other predictors that could be added to the model.