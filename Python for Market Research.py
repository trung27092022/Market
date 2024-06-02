import pandas as pd
import numpy as np

N_STORES = 20
N_WEEKS = 104

columns = ('store_num', 'year', 'week', 'p1_sales', 'p2_sales', 'p1_price', 'p2_price', 'p1_promo', 'p2_promo', 'country')
n_rows = N_STORES * N_WEEKS
store_sales = pd.DataFrame(np.empty(shape=(n_rows, 10)), columns=columns)

store_sales.shape

store_sales.head()

store_numbers = range(101, 101 + N_STORES)
list(store_numbers)

store_country = dict(zip(store_numbers,['USA', 'USA', 'USA', 'DEU', 'DEU', 'DEU','DEU', 'DEU', 'GBR', 'GBR', 'GBR', 'BRA','BRA', 'JPN', 'JPN', 'JPN', 'JPN', 'AUS','CHN', 'CHN']))

store_country

i = 0 
for store_num in store_numbers:
    for year in [1, 2]:
        for week in range(1, 53):
            store_sales.loc[i, 'store_num'] = store_num
            store_sales.loc[i, 'year'] = year
            store_sales.loc[i, 'week'] = week
            store_sales.loc[i, 'country'] = store_country[store_num]
            i += 1

store_sales.head()
 
store_sales.dtypes

type(store_sales.country[0])

store_sales.country = store_sales.country.astype( 
    pd.CategoricalDtype())
store_sales.store_num = store_sales.store_num.astype(
    pd.CategoricalDtype()) 
store_sales.store_num.head()
store_sales.country.head()

store_sales.dtypes

store_sales.head(60).round(0)
store_sales.tail(60).round(0)
store_sales.sample(60).round(0)

np.random.seed(37204)

# 10% promoted
store_sales.p1_promo = np.random.binomial(n=1, p=0.1, size=n_rows)
# 15% promoted
store_sales.p2_promo = np.random.binomial(n=1, p=0.15, size=n_rows)
store_sales.head(10) # how does it look so far? (not shown)

store_sales.p1_promo.value_counts()

store_sales.p1_price = np.random.choice([2.19, 2.29, 2.49, 2.79,
                                        2.99],
                                        size=n_rows)
store_sales.p2_price = np.random.choice([2.29, 2.49, 2.59, 2.99,
                                         3.19],
                                        size=n_rows)
store_sales.sample(5) # now how does it look?

# sales data, using poisson (counts) distribution, np.random.poisson()
# first, the default sales in the absence of promotion
sales_p1 = np.random.poisson(lam=120, size=n_rows)
sales_p2 = np.random.poisson(lam=100, size=n_rows)

# scale sales according to the ratio of log(price)
log_p1_price = np.log(store_sales.p1_price)
log_p2_price = np.log(store_sales.p2_price)

sales_p1 = sales_p1 * log_p2_price/log_p1_price
sales_p2 = sales_p2 * log_p1_price/log_p2_price

# final sales get a 30% or 40% lift when promoted
store_sales.p1_sales = np.floor(sales_p1 *
                                (1 + store_sales.p1_promo * 0.3))
store_sales.p2_sales = np.floor(sales_p2 *
                                (1 + store_sales.p2_promo * 0.4))
print(store_sales.sample(10))

