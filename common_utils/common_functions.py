import pandas as pd
import os

ROOT_DIR = os.path.dirname(os.path.abspath(path="./"))


def merge_df(fdf, first_key, sdf, skey):
    df = fdf.merge(sdf, how='left', left_on=first_key, right_on=skey)
    return df
