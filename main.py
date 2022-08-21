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
    app.logger.info('1')
    df = read_csv()
    app.logger.info('2')
    transform_data(df)
    app.logger.info('3')
    load(df)
    app.logger.info('4')


####################################################################


# call the flow!
app.logger.info('before')
indian_MAC_ETL()
app.logger.info('after')
