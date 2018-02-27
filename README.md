# sp_500
For this project, I was curious to see which S&P 500 companies are most related to each other.  To answer this, I first took a look at daily changes in stock prices for the last 1,000 days.  'Load_data' gets a current list of SP 500 companies from CNN Money and then joins that data with historical data from Alpha Vantage.  'Analyze' loops through each company and returns its Pearson Correlation Coefficient and P-Value.

# To Run:
1. Create your virtualevnv
2. Install all of the libraries from requirements.txt
3. Run load_data to export data to sqlite file
4. Run analyze to return a sorted list of correlations and p-values for those companies

# Next...
I need to examine the output and test out other variables as well as look into some sort of multivariate analysis.  It'd also be nice to join more data such as more granular company information.  Adding some concurrency would also probably be a good idea...