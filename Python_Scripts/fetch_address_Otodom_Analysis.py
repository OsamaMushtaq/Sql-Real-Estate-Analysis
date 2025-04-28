import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
from snowflake.connector.pandas_tools import pd_writer
import time
import dask.dataframe as dd

start_time = time.time()

# Set up SQLAlchemy engine for Snowflake
engine = create_engine(URL(
    account='mcqllwf-ne07241',
    user='usamamushtaq',
    password='Snowflake128950',
    database='demo',
    schema='public',
    warehouse='demo_wh'
))

with engine.connect() as conn:
    try:
        # SQL query to fetch lat/long
        query = """
            SELECT RN, CONCAT(latitude, ',', longitude) AS LOCATION
            FROM (
                SELECT RN,
                       SUBSTR(location, REGEXP_INSTR(location, ' ', 1, 4) + 1) AS LATITUDE,
                       SUBSTR(location, REGEXP_INSTR(location, ' ', 1, 1) + 1,
                              (REGEXP_INSTR(location, ' ', 1, 2) - REGEXP_INSTR(location, ' ', 1, 1) - 1)) AS LONGITUDE
                FROM otodom_data_short_flatten
                WHERE RN BETWEEN 1 AND 100
                ORDER BY RN
            )
        """

        # Load data from Snowflake
        df = pd.read_sql(query, conn)
        df.columns = map(lambda x: str(x).upper(), df.columns)

        # Convert to Dask DataFrame
        ddf = dd.from_pandas(df, npartitions=10)
        print(ddf.head(5, npartitions=-1))

        # Function to reverse geocode a partition
        def get_address_batch(df_partition):
            geolocator = Nominatim(user_agent="otodomprojectanalysis")

            def reverse_lookup(loc):
                try:
                    location = geolocator.reverse(loc, timeout=10)
                    return location.raw['address']
                except Exception as e:
                    return None  # Optionally use: return str(e)

            df_partition['ADDRESS'] = df_partition['LOCATION'].apply(reverse_lookup)
            return df_partition

        # Apply the function to all partitions
        ddf = ddf.map_partitions(get_address_batch)

        # Compute the result
        pandas_df = ddf.compute()
        print(pandas_df.head())

        # Save to Snowflake
        pandas_df.to_sql(
            'otodom_data_flatten_address',
            con=engine,
            if_exists='append',
            index=False,
            chunksize=16000,
            method=pd_writer
        )

    except Exception as e:
        print('--- Error ---', e)
    finally:
        conn.close()

engine.dispose()
print("--- %s seconds ---" % (time.time() - start_time))
