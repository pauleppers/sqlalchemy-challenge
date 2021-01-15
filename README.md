# SQLAlchemy - Surfs Up!


## Climate Analysis and Exploration

Python and SQLAlchemy are used to do basic climate analysis and data exploration of your climate database. All of the following analysis completed using SQLAlchemy 
ORM queries, Pandas, and Matplotlib.

* Use  [starter notebook](climate_starter.ipynb) and [hawaii.sqlite](Resources/hawaii.sqlite) files to complete climate analysis and data exploration.

* Choose a start date and end date for a trip. Make sure that your vacation range is approximately 3-15 days total.

* SQLAlchemy is used as`create_engine` to connect to the sqlite database.

* Used SQLAlchemy `automap_base()` to reflect tables into classes and saved as reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis

* Designed a query to retrieve the last 12 months of precipitation data.

* Selected only the `date` and `prcp` values.

* Load the query results into a Pandas DataFrame and set the index to the date column.

* Sort the DataFrame values by `date`.

* Ploted the results using the DataFrame `plot` method.

* Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Used a query to calculate the total number of stations.

* A query is used to find the most active stations.

  * List the stations and observation counts in descending order.

  * Sort station has the highest number of observations

* Created a query to retrieve the last 12 months of temperature observation data (TOBS).

  * Filtered by the station with the highest number of observations.

  * Plot the results as a histogram with `bins=12`.

## Climate App

Designed a Flask API based on the queries based on the above.

* Flask used to create your routes.

## Bonus: Other Analyses

### Temperature Analysis I

* Hawaii is reputed to enjoy mild weather all year. Detrermined if there a meaningful difference between the temperature in, for example, June and December?

* You may either use SQLAlchemy or pandas's `read_csv()` to perform this portion.

* Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.

* Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?

### Temperature Analysis II

* The starter notebook contains a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d`. The function will return the minimum, average, and maximum temperatures for that range of dates.

* Calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").

* Plot the min, avg, and max temperature from the previous query as a bar chart.

  * Average temperature as the bar height.

  * Used the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).


### Daily Rainfall Average

* Calculated the rainfall per weather station using the previous year's matching dates.

* Calculated the daily normals. Normals are the averages for the min, avg, and max temperatures.

* Use a function called `daily_normals` that calculate the daily normals for a specific date. This date string will be in the format `%m-%d`.

* Created a list of dates for the trip in the format `%m-%d`. Used the `daily_normals` function to calculate the normals for each date string and append the results to a list.

* Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.

* Used Pandas to plot an area plot (`stacked=False`) for the daily normals.

