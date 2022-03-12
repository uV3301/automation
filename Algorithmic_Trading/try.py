import pandas as pd

instrument_df = pd.read_json("https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json")
#print(instrument_df)

exp = "10FEB2022"
instrument_df = instrument_df[instrument_df["exch_seg"]=="NFO"]
instrument_df = instrument_df[instrument_df["name"]=="BANKNIFTY"]
instrument_df= instrument_df[instrument_df["expiry"]==exp]
temp_df = instrument_df[["symbol", "token"]]

df2=

token_mapping = {}

print(temp_df)