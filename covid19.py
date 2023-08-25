
import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots



st.set_page_config (page_title = 'covid19' , layout = "wide" , page_icon = '📊')


with st.sidebar:
    st.header('covid19 analysis')
    About = st.sidebar.checkbox(":blue[covid19 analysis EDA]")
    Planning = st.sidebar.checkbox(":orange[Show About Application]")
    About_me = st.sidebar.checkbox(":green[Show About me]")



"----------------------------------------------------------------------------------------"
Data_Informatio , Data_analysis_country ,Data_analysis_region,report  ,maps  = st.tabs (['Data_Informatio 💾' , ' Data_analysis_country 🔴'  , 'Data_analysis_region',' report  🟠' ,'maps'])


pd.options.display.float_format = '{:.,2f}'.format
df = pd.read_csv('/content/covid19')
df['date_reported'] = pd.to_datetime(df['date_reported'])

with Data_Informatio:

    with st.container():
        st.header("Data Describe  💾")
        DI_select = st.selectbox('Please select:',['Please select','All Columns' , 'Categorical' , 'Numerical' , 'custom'])
        if DI_select == 'Please select':
            st.write(":red[Please Choise a column from the list:]")
        elif DI_select == 'All Columns':
            st.write(":violet[Describe Table (All Columns):]")
            st.dataframe(data=df.describe().T , use_container_width=True)
        elif DI_select == 'Numerical':
            st.write(":orange[*Describe Table (All Numerical):*]")
            st.dataframe(data=df.describe(exclude = ['object']).T , use_container_width=True)
        elif DI_select == 'Categorical':
            st.write(":orange[*Describe Table (All Categorical):*]")
            st.dataframe(data=df.describe(include = ['object']).T , use_container_width=True)
        else:
            columns = st.selectbox('Please select:',df.columns.tolist())
            st.write(":orange[*Describe Table for :*]",columns)
            st.dataframe(data=df[columns].describe())

    with st.container():
        pd.options.display.float_format = '{:,.0f}'.format
        st.header("Data Information")
        DataInfo = st.checkbox("Show Data Info")
        if DataInfo :
            st.dataframe(data=df.dtypes.reset_index(name='Type'), hide_index=True, use_container_width=True)

#########______________________________________________________________________________________________-

with Data_analysis_country:
    st.header(' Data_analysis_country 🔴')
    with st.container():
        st.subheader('cumulative_cases country analysis ')
        start_date = st.date_input('Start date', datetime(2020, 1, 1))
        start_date = pd.to_datetime(start_date)
        end_date = st.date_input('End date', datetime(2023, 1, 1))
        end_date = pd.to_datetime(end_date)

        lst = st.selectbox('Please select', df.country.unique())
        y = st.selectbox('Select yaxis :' , ['Please select1','new_cases', 'cumulative_cases','new_deaths','cumulative_deaths'])

        st.write(f'Pie Chart by : {lst}')
        if lst == 'Please select' or y == 'Please select1':

            st.write(":red[Please Choise a column from the list:]")
        else:
            data = df[(df.country == lst) & (df.date_reported >= start_date) & (df.date_reported <= end_date)]
            fig = px.line(data, x='date_reported', y=y ,
            title= f'{y} for {lst} from {start_date} to {end_date}', width=1000, height=500, markers=True)

            fig1 = px.line(data, x='date_reported', y=y ,color='season',
            title= f'{y} for {lst} from {start_date} to {end_date}', width=1000, height=500, markers=True)

            fig2 = px.line(data, x='month_year', y=y ,color='month',
            title= f'{y} for {lst} from {start_date} to {end_date}', width=1000, height=500, markers=True)

            fig3=px.bar(data, x='date_reported', y=y , color='year', title= f'{y} for {lst} from {start_date} to {end_date}')
            fig4=px.bar(data, x='date_reported', y=y , color='month', title= f'{y} for {lst} from {start_date} to {end_date}')
            fig5=px.bar(data, x='date_reported', y=y , color='season', title= f'{y} for {lst} from {start_date} to {end_date}')
            fig6= px.pie(data_frame=data , names=y , color='month',color_discrete_sequence=px.colors.qualitative.D3)
            fig7= px.pie(data_frame=data , names=y , color='season',color_discrete_sequence=px.colors.qualitative.D3)
            fig8= px.pie(data_frame=data , names=y , color='year',color_discrete_sequence=px.colors.qualitative.D3)




            st.plotly_chart(fig,use_container_width=True)
            st.plotly_chart(fig1,use_container_width=True)
            st.plotly_chart(fig2,use_container_width=True)
            st.plotly_chart(fig3,use_container_width=True)
            st.plotly_chart(fig4,use_container_width=True)
            st.plotly_chart(fig5,use_container_width=True)
            st.plotly_chart(fig6,use_container_width=True)
            st.plotly_chart(fig7,use_container_width=True)
            st.plotly_chart(fig8,use_container_width=True)




#########______________________________________________________________________________________________-
with Data_analysis_region:
    st.header(' Data_analysis_region 🔴')
    with st.container():
        start_date1 = st.date_input('start_date1', datetime(2020, 1, 1))
        start_date1 = pd.to_datetime(start_date)
        end_date1 = st.date_input('end_date1', datetime(2023, 1, 1))
        end_date1 = pd.to_datetime(end_date1)

        lst2 = st.selectbox('Please selectlst2', df.who_region.unique())
        y2 = st.selectbox('Please selecty2 :' , ['Please select3','new_cases', 'cumulative_cases','new_deaths','cumulative_deaths'])

        st.write(f'Pie Chart by : {lst2}')
        if lst2 == 'Please select2' or y2 == 'Please select3':

            st.write(":red[Please Choise a column from the list:]")
        else:
            data1 = df[(df.who_region == lst2) & (df.date_reported >= start_date1) & (df.date_reported <= end_date1)]

            fig = px.line(data1, x='date_reported', y=y2 ,
            title= f'{y2} for {lst2 } from {start_date1} to {end_date1}', width=1000, height=500, markers=True)

            fig1 = px.line(data1, x='date_reported', y=y2 ,color='season',
            title= f'{y2} for {lst2} from {start_date} to {end_date}', width=1000, height=500, markers=True)

            fig2 = px.line(data1, x='month_year', y=y2 ,color='month',
            title= f'{y2} for {lst2} from {start_date1} to {end_date1}', width=1000, height=500, markers=True)

            fig3=px.bar(data1, x='date_reported', y=y2 , color='year', title= f'{y2} for {lst2} from {start_date1} to {end_date1}')
            fig4=px.bar(data1, x='date_reported', y=y2 , color='month', title= f'{y2} for {lst2} from {start_date1} to {end_date1}')
            fig5=px.bar(data1, x='date_reported', y=y2 , color='season', title= f'{y2} for {lst2} from {start_date1} to {end_date1}')
            fig6= px.pie(data_frame=data1 , names=y2 , color='month',color_discrete_sequence=px.colors.qualitative.D3)
            fig7= px.pie(data_frame=data1 , names=y2 , color='season',color_discrete_sequence=px.colors.qualitative.D3)
            fig8= px.pie(data_frame=data1 , names=y2 , color='year',color_discrete_sequence=px.colors.qualitative.D3)

            st.plotly_chart(fig,use_container_width=True)
            st.plotly_chart(fig1,use_container_width=True)
            st.plotly_chart(fig2,use_container_width=True)
            st.plotly_chart(fig3,use_container_width=True)
            st.plotly_chart(fig4,use_container_width=True)
            st.plotly_chart(fig5,use_container_width=True)
            st.plotly_chart(fig6,use_container_width=True)
            st.plotly_chart(fig7,use_container_width=True)
            st.plotly_chart(fig8,use_container_width=True)

#########______________________________________________________________________________________________-


with report:
    st.header(' final report 🔴')
    with st.container():

        st.subheader(' cases over years')
        col1, col2, col3,col4 = st.columns((4))

        with col1:
            st.subheader('new_cases over years')
            years1 =df.groupby("year")['new_cases'].sum().astype(float)
            st.write(years1)
        
        with col2:
            st.subheader('new_deaths over years')
            years2=df.groupby("year")['new_deaths'].sum().astype(float)
            st.write(years2)
        with col3:
            st.subheader('cumulative_cases over years')
            years3=df.groupby("year")['cumulative_cases'].sum().astype(float)
            st.write(years3)
        with col4:
            st.subheader('cumulative_deaths over years')
            years4=df.groupby("year")['cumulative_deaths'].sum().astype(float)
            st.write(years4)

        st.subheader(' cases for 10 largest  countries')
        col5, col6, col7,col8 = st.columns((4))
        with col5:
            st.subheader('max_newcases for 10 largest  countries')
            max_newcases=df.groupby("country")['new_cases'].max().nlargest(10)
            st.write(max_newcases)
        with col6:
            st.subheader('max_new_deaths for 10 largest  countries')
            max_newdeaths=df.groupby("country")['new_deaths'].max().nlargest(10)
            st.write(max_newdeaths)
        with col7:
            st.subheader('max_cumulative_cases for 10 largest  countries')
            max_cumulative_cases=df.groupby("country")['cumulative_cases'].max().nlargest(10)
            st.write(max_cumulative_cases)
        with col8:
            st.subheader('max_cumulative_deaths for 10 largest  countries')
            max_cumulative_deaths=df.groupby("country")['cumulative_deaths'].max().nlargest(10)
            st.write(max_cumulative_deaths)

        st.subheader(' largest  region has cases ')
        col9, col10, col11,col12 = st.columns((4))
        with col9:
            st.subheader(' largest  region has new_cases ')
            max_region_newcases=df.groupby("who_region")['new_cases'].max().nlargest(1)
            st.write(max_region_newcases)
        with col10:
            st.subheader(' largest  region has new_deaths ')
            max_region_newdeaths=df.groupby("who_region")['new_deaths'].max().nlargest(1)
            st.write(max_region_newdeaths)
        
        with col11:
            st.subheader(' largest  region has cumulative_cases ')
            max_region_cumulative_cases=df.groupby("who_region")['cumulative_cases'].max().nlargest(1)
            st.write(max_region_cumulative_cases)
        with col12:
            st.subheader(' largest  region has cumulative_deaths ')
            max_region_cumulative_deaths=df.groupby("who_region")['cumulative_deaths'].max().nlargest(1)
            st.write(max_region_cumulative_deaths)

        st.subheader(' 10 largest  country has cases in EMRO region ')
        col13, col14, col15,col16= st.columns((4))

        with col13:
            st.subheader(' 10 largest  country has new_cases in EMRO region ')
            max_EMRO_newcases=df[df['who_region']=='EMRO'].groupby("country")['new_cases'].max().nlargest(5)
            st.write(max_EMRO_newcases)

        with col14:
            st.subheader(' 10 largest  country has new_deaths in EMRO region ')
            max_EMRO_new_deaths=df[df['who_region']=='EMRO'].groupby("country")['new_deaths'].max().nlargest(5)
            st.write(max_EMRO_new_deaths)

        with col15:
            st.subheader(' 10 largest  country has cumulative_cases in EMRO region ')
            max_EMRO_cumulative_cases=df[df['who_region']=='EMRO'].groupby("country")['cumulative_cases'].max().nlargest(5)
            st.write(max_EMRO_cumulative_cases)

        with col16:
            st.subheader(' 10 largest  country has cumulative_deaths in EMRO region ')
            max_EMRO_cumulative_deaths=df[df['who_region']=='EMRO'].groupby("country")['cumulative_deaths'].max().nlargest(5)
            st.write(max_EMRO_cumulative_deaths)


        st.subheader(' 10 largest  country has cases in EURO region ')
        col17, col18, col19,col20= st.columns((4))



        with col17:
            st.subheader(' 10 largest  country has new_cases in EURO region ')
            max_EURO_newcases=df[df['who_region']=='EURO'].groupby("country")['new_cases'].max().nlargest(5)
            st.write(max_EURO_newcases)

        with col18:
            st.subheader(' 10 largest  country has new_deaths in EURO region ')
            max_EURO_new_deaths=df[df['who_region']=='EURO'].groupby("country")['new_deaths'].max().nlargest(5)
            st.write(max_EURO_new_deaths)

        with col19:
            st.subheader(' 10 largest  country has cumulative_cases in EURO region ')
            max_EURO_cumulative_cases=df[df['who_region']=='EURO'].groupby("country")['cumulative_cases'].max().nlargest(5)
            st.write(max_EURO_cumulative_cases)

        with col20:
            st.subheader(' 10 largest  country has cumulative_deaths in EURO region ')
            max_EURO_cumulative_deaths=df[df['who_region']=='EURO'].groupby("country")['cumulative_deaths'].max().nlargest(5)
            st.write(max_EURO_cumulative_deaths)





        st.subheader(' 10 largest  country has cases in AFRO region ')
        col21, col22, col23,col24= st.columns((4))



        with col21:
            st.subheader(' 10 largest  country has new_cases in AFRO region ')
            max_AFRO_newcases=df[df['who_region']=='AFRO'].groupby("country")['new_cases'].max().nlargest(5)
            st.write(max_AFRO_newcases)

        with col22:
            st.subheader(' 10 largest  country has new_deaths in AFRO region ')
            max_AFRO_new_deaths=df[df['who_region']=='AFRO'].groupby("country")['new_deaths'].max().nlargest(5)
            st.write(max_AFRO_new_deaths)

        with col23:
            st.subheader(' 10 largest  country has cumulative_cases in AFRO region ')
            max_AFRO_cumulative_cases=df[df['who_region']=='AFRO'].groupby("country")['cumulative_cases'].max().nlargest(5)
            st.write(max_AFRO_cumulative_cases)

        with col24:
            st.subheader(' 10 largest  country has cumulative_deaths in AFRO region ')
            max_AFRO_cumulative_deaths=df[df['who_region']=='AFRO'].groupby("country")['cumulative_deaths'].max().nlargest(5)
            st.write(max_AFRO_cumulative_deaths)


        st.subheader(' 10 largest  country has cases in WPRO region ')
        col25, col26, col27,col28= st.columns((4))



        with col25:
            st.subheader(' 10 largest  country has new_cases in WPRO region ')
            max_WPRO_newcases=df[df['who_region']=='WPRO'].groupby("country")['new_cases'].max().nlargest(5)
            st.write(max_WPRO_newcases)

        with col26:
            st.subheader(' 10 largest  country has new_deaths in WPRO region ')
            max_WPRO_new_deaths=df[df['who_region']=='WPRO'].groupby("country")['new_deaths'].max().nlargest(5)
            st.write(max_WPRO_new_deaths)

        with col27:
            st.subheader(' 10 largest  country has cumulative_cases in WPRO region ')
            max_WPRO_cumulative_cases=df[df['who_region']=='WPRO'].groupby("country")['cumulative_cases'].max().nlargest(5)
            st.write(max_WPRO_cumulative_cases)

        with col28:
            st.subheader(' 10 largest  country has cumulative_deaths in WPRO region ')
            max_WPRO_cumulative_deaths=df[df['who_region']=='WPRO'].groupby("country")['cumulative_deaths'].max().nlargest(5)
            st.write(max_WPRO_cumulative_deaths)


        st.subheader(' 10 largest  country has cases in AMRO region ')
        col29, col30, col31,col32= st.columns((4))



        with col29:
            st.subheader(' 10 largest  country has new_cases in AMRO region ')
            max_AMRO_newcases=df[df['who_region']=='AMRO'].groupby("country")['new_cases'].max().nlargest(5)
            st.write(max_AMRO_newcases)

        with col30:
            st.subheader(' 10 largest  country has new_deaths in AMRO region ')
            max_AMRO_new_deaths=df[df['who_region']=='AMRO'].groupby("country")['new_deaths'].max().nlargest(5)
            st.write(max_AMRO_new_deaths)

        with col31:
            st.subheader(' 10 largest  country has cumulative_cases in AMRO region ')
            max_AMRO_cumulative_cases=df[df['who_region']=='AMRO'].groupby("country")['cumulative_cases'].max().nlargest(5)
            st.write(max_AMRO_cumulative_cases)

        with col32:
            st.subheader(' 10 largest  country has cumulative_deaths in AMRO region ')
            max_AMRO_cumulative_deaths=df[df['who_region']=='AMRO'].groupby("country")['cumulative_deaths'].max().nlargest(5)
            st.write(max_AMRO_cumulative_deaths)




        st.subheader(' 10 largest  country has cases in SEARO region ')
        col33, col34, col35,col36= st.columns((4))



        with col33:
            st.subheader(' 10 largest  country has new_cases in SEARO region ')
            max_SEARO_newcases=df[df['who_region']=='SEARO'].groupby("country")['new_cases'].max().nlargest(5)
            st.write(max_SEARO_newcases)

        with col34:
            st.subheader(' 10 largest  country has new_deaths in SEARO region ')
            max_SEARO_new_deaths=df[df['who_region']=='SEARO'].groupby("country")['new_deaths'].max().nlargest(5)
            st.write(max_SEARO_new_deaths)

        with col35:
            st.subheader(' 10 largest  country has cumulative_cases in SEARO region ')
            max_SEARO_cumulative_cases=df[df['who_region']=='SEARO'].groupby("country")['cumulative_cases'].max().nlargest(5)
            st.write(max_SEARO_cumulative_cases)

        with col36:
            st.subheader(' 10 largest  country has cumulative_deaths in SEARO region ')
            max_SEARO_cumulative_deaths=df[df['who_region']=='SEARO'].groupby("country")['cumulative_deaths'].max().nlargest(5)
            st.write(max_SEARO_cumulative_deaths)
#########______________________________________________________________________________________________-



with maps:
    st.header(' maps 🔴')
    with st.container():
        df_all_max = df.groupby('country').max()
    

        map1=px.choropleth(df_all_max, locations=df_all_max.index, locationmode='country names', color=df_all_max['cumulative_cases'],
            width= 1000, height= 600, title='World wide Cumulative Cases covid19 cases', color_continuous_scale='Reds')  # Try Greens, Purples, Blues
  
        st.map(map,use_container_width=True)

 
