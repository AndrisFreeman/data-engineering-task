import requests
import pandas as pd

# Base URL for SWAPI endpoint
BASE_URL = "https://swapi.dev/api/"
VERBOSE = False

def download_resource(resource, base_url=BASE_URL, verbose=True):
    """
    This function downloads resources from the SWAPI API.

    Args:
        resource (str): The resource to download (e.g., "people", "planets", etc.).
        base_url (str, optional): The base URL of the SWAPI API. Defaults to "https://swapi.dev/api/".

    Returns:
        pandas.DataFrame: A dataframe containing the downloaded resource data.
    """

    # Construct the initial URL
    next_query = base_url + resource

    # Initialize an empty results list
    resource_results = []

    while next_query:
        if verbose:
            print(f"Downloading data from: {next_query}")  # Informative print statement

        # Send a GET request to the SWAPI endpoint
        response = requests.get(next_query)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        response_json = response.json()

        # Append the current results to the master list
        resource_results.extend(response_json["results"])

        # Get the URL for the next page of results, if available
        next_query = response_json.get("next")

    return pd.DataFrame(resource_results)


if __name__ == "__main__":
    import os
    
    # Define a list of resources to download
    resources = ["films", "people", "planets", "species", "starships", "vehicles"]

    for resource in resources:
        # Download data for the current resource
        df_resource = download_resource(resource=resource, verbose=VERBOSE)

        # A step that cleans, imputes or transforms data could be inserted here

        # Save the DF to a CSV file
        # Alternatively here one could include code for establishing connections to a database (DB) or a data warehouse (DW) to host the data
        os.makedirs(f"data", exist_ok=True)
        df_resource.to_csv(f"data/{resource}.csv")