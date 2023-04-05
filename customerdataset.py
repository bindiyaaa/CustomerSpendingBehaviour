
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

st.set_page_config(layout="wide")
st.title('Customer Spending behaviour based on various demographics')


DATA_URL = ('https://raw.githubusercontent.com/bindiyaaa/CustomerSpendingBehaviour/main/Customers.csv')


@st.cache_data
def load_data(nrows):
    customerdata = pd.read_csv(DATA_URL, error_bad_lines = False)
    return customerdata


customerdataupdate = load_data(10000)
agecol1,agecol2 = st.columns((2,1))
familycol1,familycol2 = st.columns((2,1))
col3,col4=st.columns((2,1))
profcol1,profcol2 =st.columns((2,1))

#remov column with 0 value
#customerdataupdate = customerdata.dropna()



#grouping the age in range
with agecol1:
    age_spending = customerdataupdate.groupby('Age')['Spending Score (1-100)'].mean() # calculate the average spending for each age group
    age_group = pd.cut(customerdataupdate['Age'],bins=[0,15,25,35,45,55,65,75,85,95])
    age=customerdataupdate.groupby(age_group)['Spending Score (1-100)'].mean()
    st.text("Spending behaviour based on Age Group")
    st.bar_chart(data=age,width=0, height=0, use_container_width=True)

with agecol2:
    st.write(age)



#family spending
with familycol1:
    family_spending = customerdataupdate.groupby('Family Size')['Spending Score (1-100)'].mean()
    #st.write(family_spending)
    st.text("Spending behaviour based on family size")
    st.bar_chart(data=family_spending, width=0, height=0, use_container_width=True)


with familycol2:
    st.write(family_spending)
#gender based spending in bar_chart
with col3:
    gender_spending = customerdataupdate.groupby('Gender')['Spending Score (1-100)'].sum() # calculate the total spending for each gender
    st.text("Spending behaviour based on gender")
    fig1, ax1 = plt.subplots()
    #spending = gender_spending["Spending Score (1-100)"] = pd.to_numeric(gender_spending["Spending Score (1-100)"], downcast="float")
    ax1.pie(gender_spending, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

#gender based spending
with col4:
    st.write(gender_spending)

with profcol1:
    # get uniques profession
    st.text("Spending behaviour based on profession")
    professionlist=customerdataupdate['Profession'].unique()
    profession_spending = customerdataupdate.groupby('Profession')['Spending Score (1-100)'].mean()
    #st.write(profession_spending)
    st.bar_chart(data=profession_spending,width=0, height=0, use_container_width=True)

with profcol2:
    st.write(profession_spending)
