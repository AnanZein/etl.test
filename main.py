from prefect import flow, task
import pandas as pd

import os

os.system("prefect cloud login -k pnu_zRvC10TUJgeie856jM3jVT8QxWepaf2XkXjy")

@task(retries=3)
def read_csv():
    df = "anan"
    return df


####################################################################


@task(retries=3)
def transform_data(df):
    #df['Menu Items'] = df['Menu Items'].str.lower()
    return df


####################################################################


@task(retries=3)
def load(df):
    #df.to_csv('lowerCaseMenu.csv')
    print(df)

####################################################################


@flow(name="test")
def indian_MAC_ETL():
    df = read_csv()
    transform_data(df)
    load(df)


####################################################################


# call the flow!
indian_MAC_ETL()
