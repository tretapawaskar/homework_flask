import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:Silver@123@localhost:3306/adoption')


df_puppy = pd.read_csv("puppy.csv")

df_owner = pd.read_csv("owner.csv")

df_puppy.to_sql(
    name='puppies',
    con=engine,
    index=False,
    if_exists='fail'
)

df_owner.to_sql(
    name='owners',
    con=engine,
    index=False,
    if_exists='fail'
)


############# Query - using pandas dataframes  ###############
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:Silver@123@localhost:3306/adoption')

df_puppy = pd.read_csv("puppy.csv")

## record counts in table puppies
df_puppy.count()

##count number of columns in table puppies
ncols=df_puppy.shape[1]
##########################################################################################################

df_owner = pd.read_csv("owner.csv")
## record counts in table puppies
df_owner.count()

##count number of columns in table owners
ncols1=df_owner.shape[1]
###########################################################################################################
##group by colour and count#####
group=df_puppy.groupby('colour')
group.count()