import json
import pandas as pd

# Load the JSON file into a Python object for the Top data - 2022
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2022/1.json") as f:
    data_Top_Trans_2022_1 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2022/2.json") as f:
    data_Top_Trans_2022_2 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2022/3.json") as f:
    data_Top_Trans_2022_3 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2022/4.json") as f:
    data_Top_Trans_2022_4 = json.load(f)

# Load the JSON file into a Python object for the map data - 2021
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2021/1.json") as f:
    data_Top_Trans_2021_1 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2021/2.json") as f:
    data_Top_Trans_2021_2 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2021/3.json") as f:
    data_Top_Trans_2021_3 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2021/4.json") as f:
    data_Top_Trans_2021_4 = json.load(f)

# Load the JSON file into a Python object for the map data - 2020
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2020/1.json") as f:
    data_Top_Trans_2020_1 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2020/2.json") as f:
    data_Top_Trans_2020_2 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2020/3.json") as f:
    data_Top_Trans_2020_3 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2020/4.json") as f:
    data_Top_Trans_2020_4 = json.load(f)

# Load the JSON file into a Python object for the map data - 2019
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2019/1.json") as f:
    data_Top_Trans_2019_1 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2019/2.json") as f:
    data_Top_Trans_2019_2 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2019/3.json") as f:
    data_Top_Trans_2019_3 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2019/4.json") as f:
    data_Top_Trans_2019_4 = json.load(f)

# Load the JSON file into a Python object for the map data - 2018
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2018/1.json") as f:
    data_Top_Trans_2018_1 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2018/2.json") as f:
    data_Top_Trans_2018_2 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2018/3.json") as f:
    data_Top_Trans_2018_3 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/transaction/country/india/2018/4.json") as f:
    data_Top_Trans_2018_4 = json.load(f)

# Data Frames for 2022
df_Top_Trans_2022_1 = pd.json_normalize(data_Top_Trans_2022_1['data']['states'])
df_Top_Trans_2022_2 = pd.json_normalize(data_Top_Trans_2022_2['data']['states'])
df_Top_Trans_2022_3 = pd.json_normalize(data_Top_Trans_2022_3['data']['states'])
df_Top_Trans_2022_4 = pd.json_normalize(data_Top_Trans_2022_4['data']['states'])

# Data Frames for 2021
df_Top_Trans_2021_1 = pd.json_normalize(data_Top_Trans_2021_1['data']['states'])
df_Top_Trans_2021_2 = pd.json_normalize(data_Top_Trans_2021_2['data']['states'])
df_Top_Trans_2021_3 = pd.json_normalize(data_Top_Trans_2021_3['data']['states'])
df_Top_Trans_2021_4 = pd.json_normalize(data_Top_Trans_2021_4['data']['states'])

# Data Frames for 2020
df_Top_Trans_2020_1 = pd.json_normalize(data_Top_Trans_2020_1['data']['states'])
df_Top_Trans_2020_2 = pd.json_normalize(data_Top_Trans_2020_2['data']['states'])
df_Top_Trans_2020_3 = pd.json_normalize(data_Top_Trans_2020_3['data']['states'])
df_Top_Trans_2020_4 = pd.json_normalize(data_Top_Trans_2020_4['data']['states'])

# Data Frames for 2019
df_Top_Trans_2019_1 = pd.json_normalize(data_Top_Trans_2019_1['data']['states'])
df_Top_Trans_2019_2 = pd.json_normalize(data_Top_Trans_2019_2['data']['states'])
df_Top_Trans_2019_3 = pd.json_normalize(data_Top_Trans_2019_3['data']['states'])
df_Top_Trans_2019_4 = pd.json_normalize(data_Top_Trans_2019_4['data']['states'])

# Data Frames for 2018
df_Top_Trans_2018_1 = pd.json_normalize(data_Top_Trans_2018_1['data']['states'])
df_Top_Trans_2018_2 = pd.json_normalize(data_Top_Trans_2018_2['data']['states'])
df_Top_Trans_2018_3 = pd.json_normalize(data_Top_Trans_2018_3['data']['states'])
df_Top_Trans_2018_4 = pd.json_normalize(data_Top_Trans_2018_4['data']['states'])


df_Top_Transaction_2022 = pd.concat([df_Top_Trans_2022_1, df_Top_Trans_2022_2, df_Top_Trans_2022_3, df_Top_Trans_2022_4], axis=0)
df_Top_Transaction_2021 = pd.concat([df_Top_Trans_2021_1, df_Top_Trans_2021_2, df_Top_Trans_2021_3, df_Top_Trans_2021_4], axis=0)
df_Top_Transaction_2020 = pd.concat([df_Top_Trans_2020_1, df_Top_Trans_2020_2, df_Top_Trans_2020_3, df_Top_Trans_2020_4], axis=0)
df_Top_Transaction_2019 = pd.concat([df_Top_Trans_2019_1, df_Top_Trans_2019_2, df_Top_Trans_2019_3, df_Top_Trans_2019_4], axis=0)
df_Top_Transaction_2018 = pd.concat([df_Top_Trans_2018_1, df_Top_Trans_2018_2, df_Top_Trans_2018_3, df_Top_Trans_2018_4], axis=0)

df_Top_Transaction = pd.concat([df_Top_Transaction_2022,df_Top_Transaction_2021,df_Top_Transaction_2020,df_Top_Transaction_2019,df_Top_Transaction_2018], axis=0)

df_Top_Transaction.to_excel("df_Top_Transaction.xlsx")

#display(df_Top_Transaction)

# Load the JSON file into a Python object for the Top User data - 2022
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2022/1.json") as f:
    data_Top_user_2022_1 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2022/2.json") as f:
    data_Top_user_2022_2 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2022/3.json") as f:
    data_Top_user_2022_3 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2022/4.json") as f:
    data_Top_user_2022_4 = json.load(f)

# Load the JSON file into a Python object for the Top User data - 2021
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2021/1.json") as f:
    data_Top_user_2021_1 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2021/2.json") as f:
    data_Top_user_2021_2 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2021/3.json") as f:
    data_Top_user_2021_3 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2021/4.json") as f:
    data_Top_user_2021_4 = json.load(f)

# Load the JSON file into a Python object for the Top User data - 2020
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2020/1.json") as f:
    data_Top_user_2020_1 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2020/2.json") as f:
    data_Top_user_2020_2 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2020/3.json") as f:
    data_Top_user_2020_3 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2020/4.json") as f:
    data_Top_user_2020_4 = json.load(f)

# Load the JSON file into a Python object for the Top User data - 2019
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2019/1.json") as f:
    data_Top_user_2019_1 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2019/2.json") as f:
    data_Top_user_2019_2 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2019/3.json") as f:
    data_Top_user_2019_3 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2019/4.json") as f:
    data_Top_user_2019_4 = json.load(f)

# Load the JSON file into a Python object for the Top User data - 2018
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2018/1.json") as f:
    data_Top_user_2018_1 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2018/2.json") as f:
    data_Top_user_2018_2 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2018/3.json") as f:
    data_Top_user_2018_3 = json.load(f)
with open(
        "C:/Users/Mayur/pulse/data/top/user/country/india/2018/4.json") as f:
    data_Top_user_2018_4 = json.load(f)

# Data Frames for 2022
df_Top_user_2022_1 = pd.DataFrame(data_Top_user_2022_1["data"]["states"])
df_Top_user_2022_2 = pd.DataFrame(data_Top_user_2022_2["data"]["states"])
df_Top_user_2022_3 = pd.DataFrame(data_Top_user_2022_3["data"]["states"])
df_Top_user_2022_4 = pd.DataFrame(data_Top_user_2022_4["data"]["states"])

# Data Frames for 2021
df_Top_user_2021_1 = pd.DataFrame(data_Top_user_2021_1["data"]["states"])
df_Top_user_2021_2 = pd.DataFrame(data_Top_user_2021_2["data"]["states"])
df_Top_user_2021_3 = pd.DataFrame(data_Top_user_2021_3["data"]["states"])
df_Top_user_2021_4 = pd.DataFrame(data_Top_user_2021_4["data"]["states"])

# Data Frames for 2020
df_Top_user_2020_1 = pd.DataFrame(data_Top_user_2020_1["data"]["states"])
df_Top_user_2020_2 = pd.DataFrame(data_Top_user_2020_2["data"]["states"])
df_Top_user_2020_3 = pd.DataFrame(data_Top_user_2020_3["data"]["states"])
df_Top_user_2020_4 = pd.DataFrame(data_Top_user_2020_4["data"]["states"])

# Data Frames for 2019
df_Top_user_2019_1 = pd.DataFrame(data_Top_user_2019_1["data"]["states"])
df_Top_user_2019_2 = pd.DataFrame(data_Top_user_2019_2["data"]["states"])
df_Top_user_2019_3 = pd.DataFrame(data_Top_user_2019_3["data"]["states"])
df_Top_user_2019_4 = pd.DataFrame(data_Top_user_2019_4["data"]["states"])

# Data Frames for 2019
df_Top_user_2019_1 = pd.DataFrame(data_Top_user_2019_1["data"]["states"])
df_Top_user_2019_2 = pd.DataFrame(data_Top_user_2019_2["data"]["states"])
df_Top_user_2019_3 = pd.DataFrame(data_Top_user_2019_3["data"]["states"])
df_Top_user_2019_4 = pd.DataFrame(data_Top_user_2019_4["data"]["states"])

# Data Frames for 2018
df_Top_user_2018_1 = pd.DataFrame(data_Top_user_2018_1["data"]["states"])
df_Top_user_2018_2 = pd.DataFrame(data_Top_user_2018_2["data"]["states"])
df_Top_user_2018_3 = pd.DataFrame(data_Top_user_2018_3["data"]["states"])
df_Top_user_2018_4 = pd.DataFrame(data_Top_user_2018_4["data"]["states"])

df_Top_user_2022 = pd.concat([df_Top_user_2022_1, df_Top_user_2022_2, df_Top_user_2022_3, df_Top_user_2022_4], axis=0)
df_Top_user_2021 = pd.concat([df_Top_user_2021_1, df_Top_user_2021_2, df_Top_user_2021_3, df_Top_user_2021_4], axis=0)
df_Top_user_2020 = pd.concat([df_Top_user_2020_1, df_Top_user_2020_2, df_Top_user_2020_3, df_Top_user_2020_4], axis=0)
df_Top_user_2019 = pd.concat([df_Top_user_2019_1, df_Top_user_2019_2, df_Top_user_2019_3, df_Top_user_2019_4], axis=0)
df_Top_user_2018 = pd.concat([df_Top_user_2018_1, df_Top_user_2018_2, df_Top_user_2018_3, df_Top_user_2018_4], axis=0)

df_Top_user = pd.concat([df_Top_user_2022,df_Top_user_2021,df_Top_user_2020,df_Top_user_2019,df_Top_user_2018], axis=0)

df_Top_user.to_excel("df_Top_user.xlsx")
#display(df_Top_user)