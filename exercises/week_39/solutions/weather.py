"""
Example solution for collecting weather data via API.

This code gets weather data from the API provided by frost.met.no

Note: Before running the code, get the Client-ID by registering at
https://frost.met.no/auth/requestCredentials.html and paste that client-ID 
in a text file named frost_client-id.txt
"""

__author__ = 'Hans Ekkehard Plesser, NMBU'

import matplotlib.pyplot as plt
import pandas as pd
import requests


def get_data(station, element, elem_name, time, id_file='frost_client-id.txt'):
    """
    Gets data from frost.met.no for specified parameters.
    
    :param station: String value for the station name
    :param element: String value for the weather data element 
    :param elem_name: String value for the specific category of the weather element
    :param time: String value of format YYYY-MM-DD/YYYY-MM-DD specifying the period of data
    :param id_file: String value specifying filename which contains client-ID
    :return: DataFrame with Time as index and column elem_name
    """

    client_id = open(id_file).read().strip()

    endpoint = 'https://frost.met.no/observations/v0.jsonld'
    parameters = {'sources': station,
                  'elements': element,
                  'referencetime': time}

    # Using a HTML request to get the data
    frost_response = requests.get(endpoint, parameters, auth=(client_id, ' '))

    # HTML code 200 implies the request was successful
    assert frost_response.status_code == 200

    # Extract weather data from response
    frost_payload = frost_response.json()

    # Create a list of records for observations, each record containing
    # time of measurement and observed value. Since we have observations
    # for two time offsets, we chose the first one with [0].
    temp_data = [{'Time': pd.to_datetime(entry['referenceTime']),
                  elem_name: entry['observations'][0]['value']}
                 for entry in frost_payload['data']
                 ]
    return pd.DataFrame.from_records(temp_data).set_index('Time')


if __name__ == '__main__':
    # Running weather data from Ås and Oslo (Blindern), and plot the data
    t_aas = get_data('SN17850', 'mean(air_temperature P1D)',
                     'T_avg', '2021-01-01/2021-09-26',
                     id_file='../../lectures/plesser_id.txt')
    t_oslo = get_data('SN18700', 'mean(air_temperature P1D)',
                      'T_avg', '2021-01-01/2021-09-26',
                      id_file='../../lectures/plesser_id.txt')

    # Straightforward plotting with matplotlib
    plt.figure()
    plt.plot(t_aas.index, t_aas.T_avg, label='Ås')
    plt.plot(t_oslo.index, t_oslo.T_avg, label='Blindern')
    plt.title('Daily Average Temperature')
    plt.legend()  # Displays the legend in the plot

    plt.figure()
    plt.scatter(t_aas.T_avg, t_oslo.T_avg)
    plt.xlabel('Ås')
    plt.ylabel('Blindern')

    # Advanced plotting using Pandas merge (will be discussed in November)
    # pd.merge() combines data for Aas and Oslo into one dataframe with
    # columns labeled "Ås" and "Blindern". We can then plot directly from
    # the combined dataframe.
    t_all = pd.merge(t_aas, t_oslo, left_index=True, right_index=True,
                     suffixes=(' Ås', ' Blindern'))
    t_all.plot(title='Daily Average Temperature')
    t_all.plot(kind='scatter', x='T_avg Ås', y='T_avg Blindern')

    # required to see plots in PyCharm
    plt.show()
