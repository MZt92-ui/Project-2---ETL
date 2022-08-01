import pandas as pd
from sqlalchemy import create_engine
from config import postgres_password

database_url = f"postgresql://postgres:{postgres_password}@localhost:5432/AU_tourism"
engine = create_engine(database_url)

# Scraping data from website to get population by country-of-birth
url = "https://www.abs.gov.au/statistics/people/population/australias-population-country-birth/2021"
tables = pd.read_html(url)

# the 1st table is of interest
population_df = tables[1]
population_df.columns = ["_".join(col) for col in population_df.columns.values]
population_df.rename(columns={"Unnamed: 0_level_0_Country of birth(b)":"countryname",
                                  "2021_'000":"population_2021_thousands",
                                  "Unnamed: 4_level_0_%(c)":"population_2021_percentage"},inplace=True)
population = population_df[["countryname","population_2021_thousands","population_2021_percentage"]].iloc[:20] 

# Load it into database
population.to_sql(name="auborncountry", con=engine,if_exists="append",index=False)

# load the survey data
path_int = "Resource/International_survey.xlsx"
in_visitor_df = pd.read_excel(path_int,sheet_name=0,skiprows=3,header=[0,1])

# Data cleaning to get Internation of visitors inbound by Country: 
in_visitor_df = in_visitor_df.iloc[:23]
in_visitor_df.columns = ["_".join(col) for col in in_visitor_df.columns.values]
in_visitor_df.rename(columns={"Country of_residence":"countryname",
                              "Visitors_Year ending March 2022":"visitor_est_in_2022_thousands"},inplace=True)
in_visitor = in_visitor_df[["countryname","visitor_est_in_2022_thousands"]]
in_visitor.loc[:,"visitor_est_in_2022_thousands"] = in_visitor["visitor_est_in_2022_thousands"]/1000

in_visitor.to_sql(name="countryorigin", con=engine,if_exists="append",index=False)

# load the survey data
path_nat = "Resource/National_survey.xlsx"
out_visitor_df = pd.read_excel(path_nat,sheet_name="Table 18",skiprows=3,header=[0,1],nrows=27)

# Data cleaning to get Internation visitors outbound by Country: 
out_visitor_df.columns = ["_".join(col) for col in out_visitor_df.columns.values]
out_visitor_df.rename(columns={"Unnamed: 0_level_0_Visitors ('000)":"countryname",
                               "Year Ending December 2021_Unnamed: 2_level_1":"visitor_est_out_2021_thousands"},inplace = True)
out_visitor = out_visitor_df[["countryname","visitor_est_out_2021_thousands"]]

out_visitor = out_visitor.loc[out_visitor["visitor_est_out_2021_thousands"]!="np"]
out_visitor["visitor_est_out_2021_thousands"] = out_visitor["visitor_est_out_2021_thousands"].astype(float)

out_visitor.to_sql(name="countrydestination", con=engine,if_exists="append",index=False)