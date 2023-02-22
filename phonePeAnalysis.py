import streamlit as st
import sqlite3
import pandas as pd
import json 
import plotly.express as px

app_title="Dashboard of Phonepe Pulse Data Visualiation"
app_sub_title="Credit: Mayur"

st.set_page_config(app_title)
st.title(app_title)

st.markdown(
    """
    <style>
    .main {
    background-color: #F99999;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

st.header('Data Visualization and Exploration:')
st.subheader(app_sub_title)


col1, col2 ,col3 = st.columns(3)

with col1:
    option1 = st.selectbox( 
        'Please Select', 
        ('Transactions', 'Users'))
    st.write('You selected:', option1)

with col2:
    option2 = st.selectbox(
        'Year',
        ('2018','2019','2020','2021','2022'))

    st.write('You selected:', option2)

with col3:
    option3 = st.selectbox(
        'Month',
        ('Q1(Jan-Mar)','Q2(Apr-Jun)','Q3(Jul-Sep)','Q4(Oct-Dec)'))

    st.write('You selected:', option3)

if option1 =='Transactions':
    if option2 == '2018': 
        if option3 == 'Q1(Jan-Mar)':
            df=pd.read_json('/Users/Mayur/pulse/data/aggregated/transaction/country/india/2018/1.json')            
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2018/1.json')            
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/transaction/hover/country/india/2018/1.json')
        if option3 == 'Q2(Apr-Jun)':
            df=pd.read_json('/Users/Mayur/pulse/data/aggregated/transaction/country/india/2018/2.json')            
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2018/2.json')            
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/transaction/hover/country/india/2018/2.json')
        if option3 == 'Q3(Jul-Sep)':
            df=pd.read_json('/Users/Mayur/pulse/data/aggregated/transaction/country/india/2018/3.json')            
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2018/3.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/transaction/hover/country/india/2018/3.json') 
        if option3 == 'Q4(Oct-Dec)':
            df=pd.read_json('/Users/Mayur/pulse/data/aggregated/transaction/country/india/2018/4.json')            
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2018/4.json')            
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/transaction/hover/country/india/2018/4.json')

    if option2 == '2019':
        if option3 == 'Q1(Jan-Mar)':
            df=pd.read_json('/Users/Mayur/pulse/data/aggregated/transaction/country/india/2019/1.json')           
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2019/1.json')           
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/transaction/hover/country/india/2019/1.json')
        if option3 == 'Q2(Apr-Jun)':
            df=pd.read_json('/Users/Mayur/pulse/data/aggregated/transaction/country/india/2019/2.json')            
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2019/2.json')            
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/transaction/hover/country/india/2019/2.json')
        if option3 == 'Q3(Jul-Sep)':
            df=pd.read_json('/Users/Mayur/pulse/data/aggregated/transaction/country/india/2019/3.json')            
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2019/3.json')             
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/transaction/hover/country/india/2019/3.json')
        if option3 == 'Q4(Oct-Dec)':
            df=pd.read_json('/Users/Mayur/pulse/data/aggregated/transaction/country/india/2019/4.json')            
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2019/4.json')            
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/transaction/hover/country/india/2019/4.json')

    if option2 == '2020':
        if option3 == 'Q1(Jan-Mar)':
            df=pd.read_json('/Users/Mayur/pulse/data/aggregated/transaction/country/india/2020/1.json')            
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2020/1.json')            
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/transaction/hover/country/india/2020/1.json')
        if option3 == 'Q2(Apr-Jun)':
            df=pd.read_json('/Users/Mayur/pulse/data/aggregated/transaction/country/india/2020/2.json')            
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2020/2.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/transaction/hover/country/india/2020/2.json')
        if option3 == 'Q3(Jul-Sep)':
            df=pd.read_json('//Users/Mayur/pulse/data/aggregated/transaction/country/india/2020/3.json')
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2020/3.json') 
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/transaction/hover/country/india/2020/3.json')
        if option3 == 'Q4(Oct-Dec)':
            df=pd.read_json('/Users/Mayur/pulse/data/aggregated/transaction/country/india/2020/4.json')            
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2020/4.json')            
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/transaction/hover/country/india/2020/4.json')

    if option2 == '2021':
        if option3 == 'Q1(Jan-Mar)':
            df=pd.read_json('/Users/Mayur/pulse/data/aggregated/transaction/country/india/2021/1.json')
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2021/1.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/transaction/hover/country/india/2021/1.json')
        if option3 == 'Q2(Apr-Jun)':
            df=pd.read_json('/Users/Mayur/pulse/data/aggregated/transaction/country/india/2021/2.json')
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2021/2.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/transaction/hover/country/india/2021/2.json')
        if option3 == 'Q3(Jul-Sep)':
            df=pd.read_json('/Users/Mayur/pulse/data/aggregated/transaction/country/india/2021/3.json')
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2021/3.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/transaction/hover/country/india/2021/3.json') 
        if option3 == 'Q4(Oct-Dec)':
            df=pd.read_json('/Users/Mayur/pulse/data/aggregated/transaction/country/india/2021/4.json')
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2021/4.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/transaction/hover/country/india/2021/4.json')

    if option2 == '2022':  
        if option3 == 'Q1(Jan-Mar)':
            df=pd.read_json('/Users/Mayur/pulse/data/aggregated/transaction/country/india/2022/1.json')
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2022/1.json')
            dmap=pd.read_json('//Users/Mayur/pulse/data/map/transaction/hover/country/india/2022/1.json')
        if option3 == 'Q2(Apr-Jun)':
            df=pd.read_json('/Users/Mayur/pulse/data/aggregated/transaction/country/india/2022/2.json')
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2022/2.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/transaction/hover/country/india/2022/2.json')
        if option3 == 'Q3(Jul-Sep)':
            df=pd.read_json('/Users/Mayur/pulse/data/aggregated/transaction/country/india/2022/3.json')
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2022/3.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/transaction/hover/country/india/2022/3.json') 
        if option3 == 'Q4(Oct-Dec)':
            df=pd.read_json('/Users/Mayur/pulse/data/aggregated/transaction/country/india/2022/4.json')
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/transaction/country/india/2022/4.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/transaction/hover/country/india/2022/4.json')
      


    fg=df['data']['transactionData']
            
    fg1=pd.json_normalize(fg)
                
    fgs=fg1['paymentInstruments']
    f1=pd.DataFrame(fgs[0],index=[0])
    f2=pd.DataFrame(fgs[1],index=[1])
    f3=pd.DataFrame(fgs[2],index=[2])
    f4=pd.DataFrame(fgs[3],index=[3])
    f5=pd.DataFrame(fgs[4],index=[4])


    fs=[f1,f2,f3,f4,f5]
    re=pd.concat(fs)
                
    co2=fg1['name']
    co2_1=pd.DataFrame(co2)

    det=co2_1.join(re)

    table_name1 = 'Top'
    conn1 = sqlite3.connect('mydb.sqlite')
    query1 = f'Create table if not Exists {table_name1} (Name text, Type text, Count real, Amount real)'
    conn1.execute(query1)
    det.to_sql('Categories',conn1,if_exists='replace',index=False)
    conn1.commit()


    rdf1 = pd.read_sql("select * from Top",conn1)

                
    st.subheader('Categories:')
    st.write(det)

    dmap=dmap['data']['hoverDataList']
    dmap=pd.json_normalize(dmap)
    a=dmap['name']

    fx=[]

    for x in range(len(dmap['metric'])):
        fx.append(dmap['metric'][x][0])
        
    dfma=pd.DataFrame(fx)
    
    dfma['state_name']=a
    #print(type(df))
    dfma['state_name'][9]='dadara & nagar havelli'
    dfma['state_name'][11]='andaman & nicobar island'
    dfma.drop(14,axis=0,inplace=True)
    dfma['state_name'][33]='arunanchal pradesh'
    dfma.drop(34,axis=0,inplace=True)

    table_name4 = 'Top'
    conn4 = sqlite3.connect('mydb.sqlite')
    query4 = f'Create table if not Exists {table_name4} (Type text, Count real, Amount real, Name Text)'
    conn4.execute(query4)
    dfma.to_sql(table_name4,conn4,if_exists='replace',index=False)
    conn4.commit()


    dfma = pd.read_sql("select * from Top",conn4)
    st.bar_chart(data=dfma, x="state_name", y="count", width=500, height=500, use_container_width=True)

    india_states= json.load(open("/Users/Mayur/indian-geomap/indiangeomap.json","r"))

    state_id_map = {}
    for feature in india_states['features']:
        feature['id']=feature['properties']['state_code']
        state_id_map[feature['properties']['st_nm']]=feature['id']

    new_dict = dict((k.lower(), v) for k, v in state_id_map.items()) 

    dfma['id']=dfma['state_name'].apply(lambda x: new_dict[x])

    fig=px.choropleth(dfma, 
                    locations='id',
                    geojson=india_states,
                    color='count',
                    hover_name='state_name',
                    hover_data=['amount'],
                    title='Transactions')
    fig.update_geos(fitbounds='locations',visible=False)

if option1 =='Users':   
    if option2 == '2018': 
        if option3 == 'Q1(Jan-Mar)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2018/1.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2018/1.json')
        if option3 == 'Q2(Apr-Jun)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2018/2.json')        
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2018/2.json')
        if option3 == 'Q3(Jul-Sep)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2018/3.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2018/3.json')
        if option3 == 'Q4(Oct-Dec)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2018/4.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2018/4.json')
    
    if option2 == '2019':
        if option3 == 'Q1(Jan-Mar)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2019/1.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2019/1.json')
        if option3 == 'Q2(Apr-Jun)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2019/2.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2019/2.json')
        if option3 == 'Q3(Jul-Sep)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2019/3.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2019/3.json')
        if option3 == 'Q4(Oct-Dec)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2019/4.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2019/4.json')
    
    if option2 == '2020':
        if option3 == 'Q1(Jan-Mar)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2020/1.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2020/1.json')
        if option3 == 'Q2(Apr-Jun)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2020/2.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2020/2.json')
        if option3 == 'Q3(Jul-Sep)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2020/3.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2020/3.json')
        if option3 == 'Q4(Oct-Dec)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2020/4.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2020/4.json')
    
    if option2 == '2021':
        if option3 == 'Q1(Jan-Mar)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2021/1.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2021/1.json')
        if option3 == 'Q2(Apr-Jun)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2021/2.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2021/2.json')
        if option3 == 'Q3(Jul-Sep)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2021/3.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2021/3.json')
        if option3 == 'Q4(Oct-Dec)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2021/4.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2021/4.json')

    if option2 == '2022':  
        if option3 == 'Q1(Jan-Mar)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2022/1.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2022/1.json')
        if option3 == 'Q2(Apr-Jun)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2022/2.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2022/2.json')
        if option3 == 'Q3(Jul-Sep)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2022/3.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2022/3.json')
        if option3 == 'Q4(Oct-Dec)':
            dfs=pd.read_json('/Users/Mayur/pulse/data/top/user/country/india/2022/4.json')
            dmap=pd.read_json('/Users/Mayur/pulse/data/map/user/hover/country/india/2022/4.json')

    dmap=dmap['data']['hoverData']

    l1=list(dmap.keys())
    l1=pd.DataFrame(l1)

    l2=list(dmap.values())
    l2=pd.DataFrame(l2)  

    dfm=pd.concat([l1,l2],axis=1)  
    dfm.rename({0:'state_name'},axis=1,inplace=True) 

    dfm['state_name'][9]='dadara & nagar havelli'
    dfm['state_name'][11]='andaman & nicobar island'
    dfm.drop(14,axis=0,inplace=True)
    dfm['state_name'][33]='arunanchal pradesh'
    dfm.drop(34,axis=0,inplace=True)     

    table_name8 = 'Top'
    conn8 = sqlite3.connect('mydb.sqlite')
    query8 = f'Create table if not Exists {table_name8} (state_name text, registeredUsers real, appOpens real)'
    conn8.execute(query8)
    dfm.to_sql(table_name8,conn8,if_exists='replace',index=False)
    conn8.commit()

    dfm = pd.read_sql("select * from Top",conn8)
    st.bar_chart(data=dfm, x="state_name", y="registeredUsers", width=500, height=500, use_container_width=True)

    india_states= json.load(open("/Users/Mayur/indian-geomap/indiangeomap.json","r"))

    state_id_map = {}
    for feature in india_states['features']:
        feature['id']=feature['properties']['state_code']
        state_id_map[feature['properties']['st_nm']]=feature['id']
            
    new_dict = dict((k.lower(), v) for k, v in state_id_map.items()) 
    dfm['id']=dfm['state_name'].apply(lambda x: new_dict[x])

    fig=px.choropleth(
        dfm, 
        locations='id',
        geojson=india_states,
        color='registeredUsers',
        hover_name='state_name',
        hover_data=['appOpens'],
        title='Users',
        )
    fig.update_geos(fitbounds='locations',visible=False)

st.subheader('Top 10')
col1,col2,= st.columns(2)
with col1:
    if st.button('States'):
            if option1 == 'Users':
       
                df1=dfs['data']['states']
                df1=pd.DataFrame(df1)

                table_name5 = 'Top'
                conn5 = sqlite3.connect('mydb.sqlite')
                query5 = f'Create table if not Exists {table_name5} (Name text, RegisteredUsers)'
                conn5.execute(query5)
                df1.to_sql(table_name5,conn5,if_exists='replace',index=False)
                conn5.commit()

                rdf5 = pd.read_sql("select * from Top",conn5)

                st.table(rdf5)

            if option1 =='Transactions':
                df1=dfs['data']['states']
                fg1=pd.json_normalize(df1)

                table_name = 'Top'
                conn = sqlite3.connect('mydb.sqlite')
                query = f'Create table if not Exists {table_name} (Name text, Type text, Count real, Amount real)'
                conn.execute(query)
                fg1.to_sql(table_name,conn,if_exists='replace',index=False)
                conn.commit()

                rdf = pd.read_sql("select * from Top",conn)
                st.table(rdf)

with col2:
        if st.button('Districts'):
            if option1 == 'Users':
                df1=dfs['data']['districts']
                df1=pd.DataFrame(df1)

                table_name6 = 'Top'
                conn6 = sqlite3.connect('mydb.sqlite')
                query6 = f'Create table if not Exists {table_name6} (Name text, RegisteredUsers)'
                conn6.execute(query6)
                df1.to_sql(table_name6,conn6,if_exists='replace',index=False)
                conn6.commit()

                rdf6 = pd.read_sql("select * from Top",conn6)
                st.table(rdf6)

            if option1 =='Transactions':
                df1=dfs['data']['districts']
                fg1=pd.json_normalize(df1)

                table_name2 = 'Top'
                conn2 = sqlite3.connect('mydb.sqlite')
                query2 = f'Create table if not Exists {table_name2} (Name text, Type text, Count real, Amount real)'
                conn2.execute(query2)
                fg1.to_sql(table_name2,conn2,if_exists='replace',index=False)
                conn2.commit()

                rdf2 = pd.read_sql("select * from Top",conn2)
                st.table(rdf2)      

if st.button('Pincodes'):
        if option1 == 'Users':
                df1=dfs['data']['pincodes']
                df1=pd.DataFrame(df1)

                table_name7 = 'Top'
                conn7 = sqlite3.connect('mydb.sqlite')
                query7 = f'Create table if not Exists {table_name7} (Name text, RegisteredUsers)'
                conn7.execute(query7)
                df1.to_sql(table_name7,conn7,if_exists='replace',index=False)
                conn7.commit()

                rdf7 = pd.read_sql("select * from Top",conn7)
                st.table(rdf7)


        if option1 =='Transactions':
                df1=dfs['data']['pincodes']
                fg1=pd.json_normalize(df1)

                table_name3 = 'Top'
                conn3 = sqlite3.connect('mydb.sqlite')
                query3 = f'Create table if not Exists {table_name3} (Name text, Type text, Count real, Amount real)'
                conn3.execute(query3)
                fg1.to_sql(table_name3,conn3,if_exists='replace',index=False)
                conn3.commit()

                rdf3 = pd.read_sql("select * from Top",conn3)
                st.table(rdf3)   
        
st.plotly_chart(fig)
