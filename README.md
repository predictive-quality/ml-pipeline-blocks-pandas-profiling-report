# Pandas Profiling Report
This is a repository to generates profile reports from a pandas DataFrame.

For each column the following statistics - if relevant for the column type - are presented in an interactive HTML report:

* **Type inference**: detect the [types](#types) of columns in a dataframe.
* **Essentials**: type, unique values, missing values
* **Quantile statistics** like minimum value, Q1, median, Q3, maximum, range, interquartile range
* **Descriptive statistics** like mean, mode, standard deviation, sum, median absolute deviation, coefficient of variation, kurtosis, skewness
* **Most frequent values**
* **Histogram**
* **Correlations** highlighting of highly correlated variables, Spearman, Pearson and Kendall matrices
* **Missing values** matrix, count, heatmap and dendrogram of missing values
* **Text analysis** learn about categories (Uppercase, Space), scripts (Latin, Cyrillic) and blocks (ASCII) of text data.
* **File and Image analysis** extract file sizes, creation dates and dimensions and scan for truncated images or those containing EXIF information.


## Installation

Clone the repository and install all requirements using `pip install -r requirements.txt` using Python>3.8.


## Usage

You can run the code in two ways.
1. Use command line flags as arguments `python main.py --input_path= --output_path=...`
2. Use a flagfile.txt which includes the arguments `python main.py --flagfile=example/flagfile.txt`

### Input Flags/Arguments

#### --input_path

Specify the a local or s3 object storage path where the dataframe is stored.
For a s3 object storage path a valid s3 configuration yaml file is required.

#### --output_path

Specify the path where the profile report will be stored.
For a s3 object storage path a valid s3 configuration yaml file is required.

#### --dataset_rows_max=i

For large datasets it could be necessary to generate the profile report for a limited amount of rows in order to prevent too large html files. \
The i rows are randomly selected.

#### --filename_list

A profile report will be created for every entry of the filename_list. If the list is empty, a profile report is created for every feather file in the input_path directory. 

## Example

Run `python main.py --flagfile=example/flagfile.txt` to create a report for x.fth and y.fth for 200 randomly selected rows.

## Data Set

The data set was recorded with the help of the Festo Polymer GmbH. The features (`x.csv`) are either parameters explicitly set on the injection molding machine or recorded sensor values. The target value (`y.csv`) is a crucial length measured on the parts. We measured with a high precision coordinate-measuring machine at the Laboratory for Machine Tools (WZL) at RWTH Aachen University.

If you use this data set, the citation of our publication is required! (Details see above)