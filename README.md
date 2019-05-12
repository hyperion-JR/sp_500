# sp_500
For this project, I was curious to see which S&P 500 companies are most related to each other.  To answer this, I first took a look at daily changes in stock prices for the last 500 days.  'Load_data' gets a current list of SP 500 companies from CNN Money and then joins that data with historical data from Alpha Vantage.  'Analyze' loops through each company and returns its Pearson Correlation Coefficient and P-Value.

# To Run:
1. Create your virtualenv
2. Install all of the libraries from requirements.txt
3. Run load_data to export data to sqlite file
4. Run analyze to return a sorted list of correlations and p-values for those companies

# Top 10 Positive Correlations
|Company Y|Company X|   PCC   |P-Value |
|---------|---------|--------:|-------:|
|ROST     |UNP      | 0.959059|0.000000|
|UNP      |ROST     | 0.959059|0.000000|
|AIG      |FBHS     | 0.960036|0.000000|
|FBHS     |AIG      | 0.960036|0.000000|
|FBHS     |IVZ      | 0.963732|0.000000|
|IVZ      |FBHS     | 0.963732|0.000000|
|CTXS     |FFIV     | 0.965800|0.000000|
|FFIV     |CTXS     | 0.965800|0.000000|
|NSC      |UNP      | 0.967984|0.000000|
|UNP      |NSC      | 0.967984|0.000000|

# Top 10 Negative Correlations
|Company Y|Company X|   PCC   |P-Value |
|---------|---------|--------:|-------:|
|AES      |IVZ      |-0.912307|0.000000|
|IVZ      |AES      |-0.912307|0.000000|
|AAL      |AES      |-0.909211|0.000000|
|AES      |AAL      |-0.909211|0.000000|
|IVZ      |MKC      |-0.894404|0.000000|
|MKC      |IVZ      |-0.894404|0.000000|
|AES      |PNR      |-0.884171|0.000000|
|PNR      |AES      |-0.884171|0.000000|
|HRL      |IVZ      |-0.882944|0.000000|
|IVZ      |HRL      |-0.882944|0.000000|