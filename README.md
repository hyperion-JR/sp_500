# sp_500
For this project, I was curious to see which S&P 500 companies are most related to each other.  To answer this, I first took a look at daily changes in stock prices for the last 1,000 days.  'Load_data' gets a current list of SP 500 companies from CNN Money and then joins that data with historical data from Alpha Vantage.  'Analyze' loops through each company and returns its Pearson Correlation Coefficient and P-Value.

# To Run:
1. Create your virtualevnv
2. Install all of the libraries from requirements.txt
3. Run load_data to export data to sqlite file
4. Run analyze to return a sorted list of correlations and p-values for those companies

# Top 10 Positive Correlations
|Company Y|Company X|   PCC   |P-Value |
|---------|---------|--------:|-------:|
|CMA      |RJF      | 0.992800|0.000000|
|RJF      |CMA      | 0.992800|0.000000|
|BAC      |CFG      | 0.992815|0.000000|
|CFG      |BAC      | 0.992815|0.000000|
|LNC      |ZION     | 0.992930|0.000000|
|ZION     |LNC      | 0.992930|0.000000|
|RF       |ZION     | 0.992971|0.000000|
|ZION     |RF       | 0.992971|0.000000|
|CMA      |RF       | 0.994576|0.000000|
|RF       |CMA      | 0.994576|0.000000|

# Top 10 Negative Correlations
|Company Y|Company X|   PCC   |P-Value |
|---------|---------|--------:|-------:|
|COL      |MAT      |-0.959398|0.000000|
|MAT      |COL      |-0.959398|0.000000|
|CDNS     |UAA      |-0.958843|0.000000|
|UAA      |CDNS     |-0.958843|0.000000|
|PYPL     |RRC      |-0.955181|0.000000|
|RRC      |PYPL     |-0.955181|0.000000|
|KIM      |ROP      |-0.950961|0.000000|
|ROP      |KIM      |-0.950961|0.000000|
|ROK      |UAA      |-0.950453|0.000000|
|UAA      |ROK      |-0.950453|0.000000|