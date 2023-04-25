import os
import pandas as pd

from common_utils.common_functions import merge_df

ROOT_DIR = os.path.dirname(os.path.abspath(path="Airlines_2020"))

active_weather_df = pd.read_csv(ROOT_DIR + "/resources/ActiveWeather.csv")
cancellation_df = pd.read_csv(ROOT_DIR + "/resources/Cancellation.csv")
carriers_df = pd.read_csv(ROOT_DIR + "/resources/Carriers.csv")
complete_data_df = pd.read_csv(ROOT_DIR + "/resources/CompleteData.csv")


cancelled_merged_df = merge_df(complete_data_df, "CANCELLED", cancellation_df, "STATUS")
active_weather_merged_df = merge_df(complete_data_df, "ACTIVE_WEATHER", active_weather_df, "STATUS")
carriers_merged_df = merge_df(complete_data_df, "OP_UNIQUE_CARRIER", carriers_df, "CODE")

cancelled_merged_df.to_csv(ROOT_DIR + "/resources/cancelled_merge_df.csv",index=False)
active_weather_merged_df.to_csv(ROOT_DIR + "/resources/active_weather_merged.csv",index=False)
carriers_merged_df.to_csv(ROOT_DIR + "/resources/carriers_merged.csv",index=False)

