# Import the libraries  
import pandas as pd 
import plotly.express as px
import streamlit as st
# create the streamlite feature
st. set_page_config(
    page_title= ' Hunda Data Analytics Portal', 
    page_icon= ''
)
st.title(":rainbow[Data Analytis App]")
st.subheader(':gray[Explore the data simply.]', divider='blue')
files=st.file_uploader('Upload CSV / xls file', type=['csv', 'xlsx'])
if (files !=None):
    if (files.name.endswith('xlsx')):
        data =pd.read_excel(files)
    
    else:
        data = pd.read_csv(files)
        
    st.dataframe(data)
    st.info('File is Successfully Uploaded', icon= '✅')
    
    st.subheader(':rainbow[Basic Data Statistics and Information of the Dataset]', divider= 'rainbow')
    tab1,tab2,tab3,tab4 = st.tabs (['Summary', 'Top and Bottom Rows', 'Data Types', 'Column Names'])
        
    with tab1:
            st.subheader(':grey[Stasical Summary of the Dataset]')
            st.dataframe(data.describe())
    with tab2:
            st.subheader(':grey[Top Rows]')
            toprows= st.slider('Number of rowS You Went', data.shape[0], 5, key='topslider')
            st.dataframe(data.head(toprows))
            st.subheader('Bottom Rows')
            bottomrows= st.slider('Number of Rows You Went', 1, data.shape[0],5,key='bottomSlider' )
            st.dataframe(data.tail(bottomrows))
    with tab3:
            st.subheader(':grey[Data Types of Colimns]')
            st.dataframe(data.dtypes)
    with tab4:
            st.subheader(':grey[Column names]')
            st.write(list(data.columns)) 
    
    st.subheader(':rainbow[Cooresponding Column Value To Counts]', divider= 'rainbow')
    with st.expander('Value Counts'):
        colm1,colm2= st.columns(2)
        with colm1:
            column= st.selectbox('Choose column name', options = list(data.columns))
        with colm2:
            toprows =st.number_input('Top Rows', min_value=1, step=1)
        count= st.button('Count')
        if (count==True):
            result =data[column].value_counts().reset_index().head(toprows)
            st.data_editor(result)
            st.subheader('Graphical Visualization', divider='gray')
            fig= px.bar(data_frame=result, x=column, y='count', text='count', template='seaborn')
            st.plotly_chart(fig)
            fig= px.line(data_frame=result, x=column, y='count', text='count', template='seaborn')
            #fig= px.line_3d(data_frame=result, x=column, y='count', text='count', template='seaborn')
            st.plotly_chart(fig)
            fig= px.pie(data_frame=result, names= column, values='count')
            st.plotly_chart(fig)
            
    st.subheader(':rainbow[Group By: The Method to Simplify Analiysing the Datasets]', divider='rainbow')
    st.write('The Groupby option lets help you to Summarize and Organize your Data')        
    
    with st.expander('Groupby Operatio'):
        col1,col2,col3= st.columns(3)
        with col1:
            groupby_cols=st.multiselect('Choose Column Groupby', options=list(data.columns))  
        with col2:
            OPeration_cols=st.selectbox('Choose Column Groupby', options=list(data.columns))
        with col3:
            operation=st.selectbox('Choose Operation', options= ['sum', 'max', 'min','mean', 'Median','count'])
            
        if(groupby_cols):
            result=data.groupby(groupby_cols).agg(
               Mathematical_operations=(OPeration_cols, operation)
            ).reset_index()
            
            st.dataframe(result) 
            
            st.subheader(':gray[Data Visualization]', divider='gray')
            graphs =st.selectbox('Choose Your graphs', options=['line', 'bar', 'scatter', 'pie', 'sunbrust'] )
            if (graphs=='line'):
                x_axis=st.selectbox('Choose X axis', options=list(result.columns))
                y_axis=st.selectbox('Choose Y axis', options=list(result.columns))
                color=st.selectbox('Color Information', options= [None] + list(result.columns))
                fig= px.line(data_frame=result, x=x_axis,y=y_axis, color=color, markers='o')
                st.plotly_chart(fig)
            elif (graphs=='bar'):
                x_axis=st.selectbox('Choose X axis', options=list(result.columns))       
                y_axis=st.selectbox('Choose Y axis', options=list(result.columns))
                color=st.selectbox('Color Information', options= [None] + list(result.columns))
                fig= px.bar(data_frame=result, x=x_axis,y=y_axis, color=color, facet_col=None, barmode='group')
                st.plotly_chart(fig)
            elif (graphs=='scatter'):
                x_axis=st.selectbox('Choose X axis', options=list(result.columns))       
                y_axis=st.selectbox('Choose Y axis', options=list(result.columns))
                color=st.selectbox('Color Information', options= [None] + list(result.columns))
                size=st.selectbox('Size Column', options= [None] + list(result.columns))
                fig= px.scatter(data_frame=result, x=x_axis,y=y_axis, color=color, size=size)
                st.plotly_chart(fig)
            elif (graphs=='pie'):
                Values=st.selectbox('Choose Numerical Values', options=list(result.columns))
                Names=st.selectbox('Choose Labels', options=list(result.columns))
                fig= px.pie(data_frame=result, values=Values, names=Names)
                st.plotly_chart(fig)
            elif (graphs=='sunbrust'):
                path=st.multiselect('Choose your Path', options=list(result.columns))
                values=st.selectbox('Choose your Values', options=list(result.columns))
                fig= px.sunburst(data_frame=result, path=path, values=values)
                st.plotly_chart(fig)
