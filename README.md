# sp_500
For this project, I was curious to see which S&P 500 companies are most related to each other.  To answer this, I first took a look at daily changes in stock prices for the last 500 days.  'Load_data' gets a current list of SP 500 companies from CNN Money and then joins that data with historical data from Alpha Vantage.  'Analyze' loops through each company and returns its Pearson Correlation Coefficient and P-Value.

# To Run:
1. Create your virtualenv
2. Install all of the libraries from requirements.txt
3. Run load_data to export data to sqlite file
4. Run analyze to return a sorted list of correlations and p-values for those companies

# Top 20 Positive Correlations
|Company Y|Company X|   PCC   |P-Value |
|---------|---------|--------:|-------:|
|FITB     |BBT      | 0.990730|0.000000|
|LNC      |BAC      | 0.990740|0.000000|
|RCL      |CCL      | 0.990795|0.000000|
|ZION     |BAC      | 0.990869|0.000000|
|BAC      |CMA      | 0.991308|0.000000|
|CMA      |BAC      | 0.991308|0.000000|
|ZION     |MS       | 0.991484|0.000000|
|ZION     |RJF      | 0.991733|0.000000|
|JPM      |BAC      | 0.991812|0.000000|
|STI      |CMA      | 0.991903|0.000000|
|ZION     |FITB     | 0.991963|0.000000|
|ZION     |CMA      | 0.992192|0.000000|
|RJF      |CMA      | 0.992800|0.000000|
|CFG      |BAC      | 0.992815|0.000000|
|ZION     |LNC      | 0.992930|0.000000|
|ZION     |RF       | 0.992971|0.000000|
|RF       |CMA      | 0.994576|0.000000|
|NWSA     |NWS      | 0.996235|0.000000|
|DISCK    |DISCA    | 0.997946|0.000000|
|GOOG     |GOOGL    | 0.999081|0.000000|

# Top 20 Negative Correlations
|Company Y|Company X|   PCC   |P-Value |
|---------|---------|--------:|-------:|
|COL      |MAT      |-0.959398|0.000000|
|CDNS     |UAA      |-0.958843|0.000000|
|PYPL     |RRC      |-0.955181|0.000000|
|KIM      |ROP      |-0.950961|0.000000|
|ROK      |UAA      |-0.950453|0.000000|
|ALL      |UAA      |-0.949423|0.000000|
|MAT      |PYPL     |-0.949199|0.000000|
|ADBE     |UAA      |-0.947968|0.000000|
|DE       |NLSN     |-0.946641|0.000000|
|RHT      |RRC      |-0.946606|0.000000|
|BA       |RRC      |-0.946600|0.000000|
|MA       |RRC      |-0.945842|0.000000|
|AME      |RRC      |-0.944147|0.000000|
|ALL      |TRIP     |-0.943926|0.000000|
|KIM      |MAR      |-0.943374|0.000000|
|MAT      |RHT      |-0.943304|0.000000|
|PGR      |RRC      |-0.943187|0.000000|
|AJG      |UAA      |-0.942811|0.000000|
|CBOE     |MAT      |-0.941948|0.000000|
|BA       |UAA      |-0.941933|0.000000|