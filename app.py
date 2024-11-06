import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from model.fmp import Fmp
import pandas as pd

##  Setting up the env
load_dotenv()


with st.sidebar:
    st.title('Navigation Bar')
    st.html("""<a href='#introduction'>Introduction</a>""")
    st.html("""<a href='#key-metrics'>Key Metrics</a>""")
    # st.html("""<a href='#key-metrics'>Key Metrics</a>""")


# Set the title of the app
st.title('Simple Stock Analyser')

# Add a text input for the stock symbol
stock_symbol = st.text_input('Enter Stock Ticker Symbol', '')
stock_symbol = stock_symbol.upper()

# Add a button to submit the form
if st.button('Analyze'):
    st.header(f'Analyzing stock: {stock_symbol}')
    
    st.header('Introduction')
    with st.expander("See Introduction"):            
        with st.spinner("Loading..."):
        
            # Get introduction of the company
            # genai.configure(api_key=os.getenv("GENAI_API_KEY"))
            # model = genai.GenerativeModel("gemini-1.5-flash")
            
            # response = model.generate_content(f"Explain this US company with the stock symbol {stock_symbol}")
            # st.write(f'{response.text}')
            st.write('Successs....')

    st.header('Key Metrics')
    tab1, tab2 = st.tabs(["Annual", "Quarter"])
    fmp = Fmp()
    
    with tab1:
        with st.spinner("Loading..."):
            # data = fmp.get_company_key_metrics(period='annual', symbol=stock_symbol)
            # st.dataframe(data)
            st.write('tab1')
            
    with tab2:
        with st.spinner("Loading..."):
            # data = fmp.get_company_key_metrics(period='quarter', symbol=stock_symbol)
            st.write('tab2')
    
        
        
        
    

