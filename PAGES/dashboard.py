import streamlit as st
import pandas as pd
import numpy as np 
import plotly.figure_factory as ff
import plotly.express as px



import matplotlib.pyplot as plt
import scipy.stats as stats

#####PRUEBA SOLO EMISOR



import pyarrow as pa
import pyarrow.csv
def skip_comment(row):
    if row.text.startswith("# "):
        return 'skip'
    else:
        return 'error'

parse_options = pa.csv.ParseOptions(delimiter=",", invalid_row_handler=skip_comment)
df_RAW_DATA_EMI = pa.csv.read_csv(r".\DATA_APP\transaction_data.csv",parse_options=parse_options).to_pandas()



###hacer filtro por mes por ....
aux_EMI=df_RAW_DATA_EMI

import random
random.seed(1023)
aux_EMI['MES']=[random.randint(1,12) for i in range(aux_EMI.shape[0])]




st.set_page_config(
    page_title = 'Streamlit Sample Dashboard Template',
    page_icon = '✅',
    layout = 'wide'
)


#################################################INTRO
MES_ANIO = ['TODO']+sorted(aux_EMI['MES'].value_counts().index.tolist())

# *** SCATTER PLOT WITH DROPDOWN SELECTBOXES ***
st.title('Scatter Plot')
scatter_x = st.selectbox('seleccionar mes', MES_ANIO)
st.write('selceccionaste :',scatter_x)
########################################################
if scatter_x=='TODO':
    pass
else:
    aux_EMI=aux_EMI[aux_EMI['MES']==scatter_x]





st.markdown("## KPI First Row")

# kpi 1 

kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.markdown("**NUMERO TRX FRAUDULENTAS**")
    number1 = 'la suma es: {:,.2f}'.format(aux_EMI.shape[0])
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with kpi2:
    st.markdown("**Valor de fraude**")

    number2 ='la suma es: {:,.2f}'.format(sum(aux_EMI['CostPerItem']))+' $'
    
    st.metric(label="", value=number2, delta="en pesos CO")
with kpi3:
    st.markdown("**N° comercios afectados en el mes**")
    number3 = len(aux_EMI['ItemDescription'].value_counts().index)
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number3}</h1>", unsafe_allow_html=True)

st.markdown("<hr/>",unsafe_allow_html=True)


st.markdown("## KPI Second Row")

# kpi 1 

kpi01, kpi02, kpi03, kpi04, kpi05 = st.columns(5)

with kpi01:
    st.markdown("**Another 1st KPI**")
    number1 = np.nan
    st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

with kpi02:
    st.markdown("**Another 1st KPI**")
    number1 = np.nan
    st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

with kpi03:
    st.markdown("**Another 1st KPI**")
    number1 = np.nan 
    st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

with kpi04:
    st.markdown("**Another 1st KPI**")
    number1 = np.nan
    st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

with kpi05:
    st.markdown("**Another 1st KPI**")
    number1 = np.nan
    st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

st.markdown("<hr/>",unsafe_allow_html=True)

st.markdown("## Chart Layout")

chart1, chart2 = st.columns(2)

with chart1:
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

with chart2:
    chart_data = pd.DataFrame(np.random.randn(2000, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)
    ###########DENSIDAD
    #source = {"AGW": aux_EMI.CostPerItem}
    #df=pd.DataFrame(source)

    #df["AGW"].sort_values()
    #df_mean = np.mean(df["AGW"])
    #df_std = np.std(df["AGW"])

    #pdf = stats.norm.pdf(df["AGW"].sort_values(), df_mean, df_std)

    #st.line_chart(pdf)


    
chart3, chart4 = st.columns(2)

with chart3:
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

with chart4:
    #################BARPLOT
    top=4
    aux_pie=pd.DataFrame(aux_EMI.Country.value_counts())
    name_aux=aux_pie.columns[0]
    aux_pie.columns=['conteo']
    aux_pie[name_aux]=aux_pie.index
    aux_pie=aux_pie.iloc[0:top,:]

    data_canada = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(aux_pie, x=aux_pie.columns[1], y=aux_pie.columns[0])
    fig.update_layout(margin=dict(l=20, r=20, t=30, b=0),)
    st.plotly_chart(fig, use_container_width=True)









cols = st.columns([1, 1])

with cols[0]:
    #################PIE CHART
    top=4
    aux_pie=pd.DataFrame(aux_EMI.Country.value_counts())
    name_aux=aux_pie.columns[0]
    aux_pie.columns=['conteo']
    aux_pie[name_aux]=aux_pie.index
    aux_pie=aux_pie.iloc[0:top,:]
    


    fig = px.pie(aux_pie, values=aux_pie.columns[0], names=aux_pie.columns[1], title='Population of European continent')
    fig.update_layout(margin=dict(l=20, r=20, t=30, b=0),)
    st.plotly_chart(fig, use_container_width=True)

with cols[1]:
    ##############HISTOGRAMA
    df = px.data.tips()
    fig = px.histogram(df, x="total_bill")
    fig.update_layout(margin=dict(l=20, r=20, t=30, b=0),)
    st.plotly_chart(fig, use_container_width=True)
