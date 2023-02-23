import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache 
def process_data(file):
    ''' 
    loads data from the csv file when provided
    '''
    df = pd.read_csv(file)
    return df

def main():
    st.set_page_config(page_title="CSV Plotting Tool", page_icon = ":bar_chart", layout = "wide")
    st.title("Upload a CSV file")

    uploaded_file = st.file_uploader("Choose a CSv file", type=["csv"])

    if uploaded_file is not None:
        df = process_data(uploaded_file)
        st.dataframe(df.head())
        width = st.sidebar.slider("plot width", 1, 25, 3)
        height = st.sidebar.slider("plot height", 1, 25, 1)

        ''' Plot a histogram of a column '''
        if st.checkbox("Generate Histogram"):
            column = st.selectbox("Select a column", df.columns)
            st.write(px.histogram(df, x=column, nbins=20, width=1200, height=800))

        ''' Plot a scatter plot of two columns '''
        if st.checkbox("Generate Scatterplot"):
            x_column = st.selectbox("Select the X column", df.columns)
            y_column = st.selectbox("Select the Y column", df.columns)
            st.write(px.scatter(df, x=x_column, y=y_column, width=1200, height=800))

        ''' Plot a timeseries plot of two columns '''
        if st.checkbox("Generate Timeseries"):
            xt_column = st.selectbox("Select X column", df.columns)
            yt_column = st.selectbox("Select Y column", df.columns)
            st.write(px.line(df, title="TimeSeries", x=xt_column, y=yt_column, width=1200, height=800))  

        # ''' Plot a Donut of columns '''
        # if st.checkbox("Generate Donut"):
        #     columns = st.selectbox("Select column", df.columns)
        #     st.write(px.pie(df, columns ))  


        # categories = df[['Host','Status']].agg(', '.join, axis=1)
        # # print(categories)          
        # fig = px.histogram(df, x="total_bill", color =categories)
        # fig.show()
        

if __name__ == "__main__":
    main()
    