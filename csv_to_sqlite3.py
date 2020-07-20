# This script is for importing a csv file into sqlite3

import pandas as pd
from sqlalchemy import create_engine # database connection
import datetime as dt
#write_to_sqlite()


def write_to_sqlite3(filename_no_extension):
	#pd.read_csv(filename + '.csv', nrows=2)
	disk_engine = create_engine('sqlite:///' + filename + '.db')

	start = dt.datetime.now()
	chunksize = 20000
	j = 0
	index_start = 1


	for df in pd.read_csv(filename_no_extension + '.csv', chunksize=chunksize, iterator=True, encoding='utf-8'):

	    df = df.rename(columns={c: c.replace(' ', '') for c in df.columns}) # Remove spaces from columns

	    df.index += index_start

	    
	    print ('{} seconds: completed {} rows'.format((dt.datetime.now() - start).seconds, j*chunksize))

	    df.to_sql('filename', disk_engine, if_exists='append')
	    index_start = df.index[-1] + 1
	    j = j + 1