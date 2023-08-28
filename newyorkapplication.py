
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import streamlit as st
import plotly.express as px
from PIL import Image


st.set_page_config (page_title = 'New York City  EDA 🚴‍♂️' , layout = "wide" , page_icon = '📊')
Data_Info , Univariate , Bivariate  , Multivariate,program = st.tabs (['Data Information 💾' , 'Univariate Analysis 🔴'  , 'Bivariate Analysis 🟠' , 'Multivariate Analysis🟢','program 🟢'])

df=pd.read_csv("/content/NYC_2019new.csv")
pd.options.display.float_format = '{:,.2f}'.format
df.last_review = pd.to_datetime(df.last_review)

with Data_Info:
    with st.container():
        st.image('/content/226165_Ya9pWjt4.jpg', width=300)
        st.markdown('''This app is created to analyze new york city according regions.''')
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

    with st.container():
        st.subheader('Heatmap Corrolation')
        corrolation = st.checkbox('Show Corrolations')
        if corrolation :
            cor = df.select_dtypes(exclude='object').corr()
            fig_corr = px.imshow(cor , text_auto=True , width= 900 , height= 900  , color_continuous_scale='rdbu')
            st.plotly_chart(fig_corr,use_container_width=True)

        st.subheader("Hierarchical view of price using TreeMap")
        fig3 = px.treemap(df, path = ["neighbourhood_group","neighbourhood","room_type"], values = "price",hover_data = ["price"],color = "room_type")
        st.plotly_chart(fig3, use_container_width=True)



with Univariate:
    with st.container():
        st.header('Univariate Analysis 🔴')

        lst=st.selectbox('Select yaxis :',['please select','neighbourhood_group','neighbourhood','price'])
        if lst == 'please select':
            st.write(":red[pleas choise a column from the list]")

        else:
            fig=px.pie(data_frame=df,names=lst,color="room_type")
            fig1=px.histogram(data_frame=df,x=lst,color="room_type")

            st.plotly_chart(fig,use_container_width=True)
            st.plotly_chart(fig1,use_container_width=True)
with Bivariate:
    with st.container():
        st.header('Univariate Analysis 🔴')

        col1, col2, col3 = st.columns((3))
        with col1:
            x=st.selectbox('Select xaxis :',["please selectx","neighbourhood_group",'neighbourhood','latitude','longitude','room_type','price','minimum_nights',
                           "last_review","reviews_per_month","distance"])
        with col2:
            y=st.selectbox('Select yaxis :',["please selecty","neighbourhood_group",'neighbourhood','latitude','longitude','room_type','price','minimum_nights',
                           "last_review","reviews_per_month","distance"])

        with col3:
            color=st.selectbox('Select coloraxis :',["please selecty color",'room_type','neighbourhood_group'])


        if x=="please selectx" or y=="please selecty" or color=="please selecty color" :
            st.write(":red[please choise for x&y&color:]")
        else:
            fig= px.histogram(df, x=x, y=y, color= color)
            fig2=px.scatter(df, x=x, y=y, color=color )
            fig_bi_1 = px.line(df , x = x , y = y , color=color , markers=True)
            fig_bi_2=px.box(df, x=x, y=y, color= color)
            fig3 = px.area(df, x=x, y=y,color=color)

            st.plotly_chart(fig,use_container_width=True)
            st.plotly_chart(fig2,use_container_width=True)
            st.plotly_chart(fig_bi_1,use_container_width=True)
            st.plotly_chart(fig_bi_2,use_container_width=True)
            st.plotly_chart(fig3,use_container_width=True)



with Multivariate:
    with st.container():
        st.header('Multivariate 🔴')
        st.subheader("price>1000")

        col1, col2, col3 = st.columns((3))
        with col1:
            x=st.selectbox('Select xaxis :',["please selectx1","neighbourhood_group",'neighbourhood','latitude','longitude','room_type','price','minimum_nights',
                           "last_review","reviews_per_month","distance"])
        with col2:
            y=st.selectbox('Select yaxis :',["please selecty1","neighbourhood_group",'neighbourhood','latitude','longitude','room_type','price','minimum_nights',
                           "last_review","reviews_per_month","distance"])

        with col3:
            color=st.selectbox('Select coloraxis :',["please selecty color1",'room_type','neighbourhood_group'])


        if x=="please selectx1" or y=="please selecty1" or color=="please selecty color1" :
            st.write(":red[please choise for x&y&color:]")
        else:
            df2 = df[df.price>1000]
            fig= px.histogram(df2, x=x, y=y, color= color)
            fig2=px.scatter(df2, x=x, y=y, color=color )
            fig_bi_1 = px.line(df2 , x = x , y = y , color=color , markers=True)
            fig_bi_2=px.box(df2, x=x, y=y, color= color)
            fig4 = px.area(df2, x=x, y=y,color=color)


            st.plotly_chart(fig,use_container_width=True)
            st.plotly_chart(fig2,use_container_width=True)
            st.plotly_chart(fig_bi_1,use_container_width=True)
            st.plotly_chart(fig_bi_2,use_container_width=True)
            st.plotly_chart(fig4,use_container_width=True)




        st.subheader("price<1000")

        col1, col2, col3 = st.columns((3))
        with col1:
            x=st.selectbox('Select xaxis :',["please selectx2","neighbourhood_group",'neighbourhood','latitude','longitude','room_type','price','minimum_nights',
                           "last_review","reviews_per_month","distance"])
        with col2:
            y=st.selectbox('Select yaxis :',["please selecty2","neighbourhood_group",'neighbourhood','latitude','longitude','room_type','price','minimum_nights',
                           "last_review","reviews_per_month","distance"])

        with col3:
            color=st.selectbox('Select coloraxis :',["please selecty color2",'room_type','neighbourhood_group'])


        if x=="please selectx2" or y=="please selecty2" or color=="please selecty color2" :
            st.write(":red[please choise for x&y&color:]")
        else:
            df3 = df[df.price<1000]
            fig= px.histogram(df3, x=x, y=y, color= color)
            fig2=px.scatter(df3, x=x, y=y, color=color )
            fig_bi_1 = px.line(df3 , x = x , y = y , color=color , markers=True)
            fig_bi_2=px.box(df3, x=x, y=y, color= color)
            fig5 = px.area(df3, x=x, y=y,color=color)


            st.plotly_chart(fig,use_container_width=True)
            st.plotly_chart(fig2,use_container_width=True)
            st.plotly_chart(fig_bi_1,use_container_width=True)
            st.plotly_chart(fig_bi_2,use_container_width=True)
            st.plotly_chart(fig5,use_container_width=True)

with program:
    with st.container():
        st.header('program 🔴')
        st.subheader("chosie a sutibale place for you")
        region=st.selectbox("please select region:",df.neighbourhood_group.unique())
        price = st.slider('price?', 0, 15000, 500)
        roomtype=st.selectbox("please selectroomtype:",df.room_type.unique())
        if region=="please select region" or price=="price?" or roomtype=="please selectroomtype:" :
            st.write(":red[please choise :]")

        else:
            data=df[(df.neighbourhood_group==region)&(df.price<price)&(df.room_type==roomtype)]
            data = data.groupby(['neighbourhood'])['price'].mean()
            st.write(data)

