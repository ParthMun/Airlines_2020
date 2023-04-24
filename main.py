import os
import pandas as pd
ROOT_DIR = os.path.dirname(os.path.abspath(path="Airlines_2020"))

active_weather_df = pd.read_csv(ROOT_DIR + "/resources/ActiveWeather.csv")
cancellation_df = pd.read_csv(ROOT_DIR + "/resources/Cancellation.csv")
carriers_df = pd.read_csv(ROOT_DIR + "/resources/Carriers.csv" )
complete_data_df = pd.read_csv(ROOT_DIR + "/resources/CompleteData.csv")
station_df = pd.read_csv(ROOT_DIR + "/resources/Stations.csv")

