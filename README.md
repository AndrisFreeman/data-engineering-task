## Task description
A customer wants to analyze data for our nerd facts business from `swapi.dev` because their business model of having Greta to be their one and only person to sell fun interesting nerdy facts is not scalable. On a daily basis, make a rudimentary stack for downloading data from the API and making it available for analysis.

## Chosen API
`swapi.dev` was chosen due to my familiarity with the SW universe. The data also allows the creation of link tables for a fully working relational DB storage solution.

## General pipeline
The pipeline for this project could look like this:
1. **Download data from API** - Retrieves data and handles pagination of `swapi.dev` results that span multiple pages
2. **Preprocess data** - Not implemented. Data is clean and free of missing values. Additional steps like feature engineering could be implemented in the future.
3. **Store data** - Currently, downloaded data is saved locally as CSV files. Future iterations could connect to databases or data warehouses for scalable and accessible storage.

## Limitations

### Data download
The current approach downloads all data from the SWAPI on each execution. While this works well for small datasets, it would be less efficient for larger ones.  
**Suggestion:** To improve scalability, we could implement mechanisms to download only new or changed data. One way to achieve this is by storing a timestamp of the last download and comparing it with the API's data update timestamp. This ensures data is downloaded only when it's actually been updated on the API side. Alternative approaches, like checking individual entries for changes, would be more complex.

### Data preprocessing
The current implementation assumes the downloaded data is already clean and free of missing values. While this might be the case for SWAPI, it's not guaranteed for all datasets. Additionally, no transformations are currently performed to change data types or engineer new features, and link tables haven't been created to establish relationships between different resources (e.g., starships to films).

### Data storage
Currently, data is stored locally as CSV files, which is not scalable and limits data accessibility for multiple users.  
An SQL DB server or a cloud storage solution such as Google Cloud SQL offers a more scalable and collaborative storage solution.

### Scheduling
Since this project isn't hosted anywhere, no scheduling is done. However, assuming the project would be hosted on a server, a cron job could be created to schedule its execution.

An example cron job definition that runs a Python script every day at 4:00 would look like this:  
`0 4 * * * /usr/bin/python3 <path-to-script>/main.py`

**Explanation:**  
* `0`: Minute (0 - runs at the beginning of the hour)
* `4`: Hour (4 - specifies 4 AM)
* `*`: Day of month (every day)
* `*`: Month (every month)
* `*`: Day of week (every day)
* `/usr/bin/python3`: Path to the Python 3 executable
* `<path-to-script>/main.py`: Path to the Python script to run
