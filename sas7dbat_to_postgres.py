## Goal: import multiple massive sas7dbat table files directly into a 
# Postgres database when no access to SAS

### initial run kind of successful but rough, not ready for show-time - need to test 
# fix and then refactor 
# (potentially set to run through folder of multiple files)

import pandas as pd
from sqlalchemy import create_engine

sas_file = 'path_to_sas7bdat_file'  # enter the path to your file here
## TO DO: Amend these to allow reading of multiple sas7bdat files e.g. in a folder

postgres_user = 'db_user_name_here'
postgres_pw = 'db_user_password_here'
postgres_db_name = 'db_name_here'
postgres_table_name = 'table_name_here'

engine = create_engine(" 'postgresql://' + postgres_user + ':'' + db_user_password_here + 'localhost:5432/'' + postgres_db_name ", echo=False)

df = pd.read_sas('sas7bdat file location')
df.to_sql('table_name_here', con=engine, if_exists='replace')
