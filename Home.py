import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from prophet.plot import plot_plotly, plot_components_plotly
from services.gemini import geminiService
from model.forecast import Forecast
from utils.base_ui import baseUI
from services.fmp import Fmp

class mainUI(baseUI):
    
    def __init__(self):
        st.set_page_config(layout="wide", page_title='Stock Analyser Dashboard', page_icon='📈') 
        self.fmp = Fmp()
        self.gemini = geminiService()
        self.forecast = Forecast()
            
    def sidebarUI(self):
        
        with st.sidebar:
            st.title('Sections')
            st.markdown("[Introduction](#introduction)")
            st.markdown("[Historical Data](#historicalData)")
            st.markdown("[Key Metrics](#key-metrics)")
            st.markdown("[Key Metrics Graph](#key-metrics-graph)")
            st.markdown("[Stock Forecast](#stock-forecast)")

    def titleUI(self):
        center_title = st.columns([1, 2, 1])
        
        with center_title[1]:
            # Set the title of the app
            st.html("<h1 style='text-align: center;'>Stock Analyser Dashboard</h1>")
            
            # Add a text input for the stock symbol
            self.stock_symbol = st.text_input('Enter Stock Ticker Symbol', '').upper()
            
            click = st.button('Analyse Stock')
            
            return click

    def introductionUI(self):
        st.header('Introduction',anchor='introduction')
        with st.spinner("Loading..."):
            with st.expander("See Introduction"):            
            
                # Get introduction of the company
                st.write(self.gemini.get_introduction(symbol=self.stock_symbol))

    def historicalDataUI(self):
        st.header('Historical Data',anchor='historicalData')
        with st.spinner("Loading Historical Data..."):
            
            # Get key metrics of the company
            historicalData = self.fmp.get_historical_data(symbol=self.stock_symbol) 
            historicalData = pd.DataFrame(historicalData['historical'])
            
            # Calculate the Simple Moving Average
            historicalData['SMA_50'] = historicalData['close'].rolling(window=50).mean()
            historicalData['SMA_150'] = historicalData['close'].rolling(window=150).mean()
            
            # Create the candlestick chart
            fig = go.Figure(
                data=[
                    go.Candlestick(
                        x=historicalData["date"],
                        open=historicalData["open"],
                        high=historicalData["high"],
                        low=historicalData["low"],
                        close=historicalData["close"],
                        increasing_line_color="green",
                        decreasing_line_color="red",
                    )
                ]
            )

            # Add SMA lines
            fig.add_trace(
                go.Scatter(
                    x=historicalData["date"],
                    y=historicalData["SMA_50"],
                    mode="lines",
                    name="50-Day SMA",
                    line=dict(color="blue", width=2)
                )
            )
            
            fig.add_trace(
                go.Scatter(
                    x=historicalData["date"],
                    y=historicalData["SMA_150"],
                    mode="lines",
                    name="150-Day SMA",
                    line=dict(color="green", width=2)
                )
            )
            
            fig.update_layout(
                title=f"{self.stock_symbol} Historical Stock Price (USD)",
                xaxis_title="Date",
                yaxis_title="Price" 
            )
            
            self.historicalData = historicalData
            st.plotly_chart(fig, use_container_width=True)
    
    def keyMetricsUI(self):
        st.header('Key Metrics', anchor='key-metrics')
        
        with st.spinner("Loading Key Metrics..."):
            # Get key metrics of the company
            data = self.fmp.get_company_key_metrics(period='annual', symbol=self.stock_symbol)
            st.dataframe(data)     
            return pd.DataFrame(data)
        
    def keyMetricsGraphUI(self, keyMetrics):  
        st.subheader('Key Metrics Graph', anchor='key-metrics-graph')
        revenueCol, netIncomeCol, operatingCashFlowCol, freeCashFlowCol = st.columns(4)
        
        with revenueCol:
            st.text('Revenue Per Share Growth Over the Years')
            st.bar_chart(keyMetrics, x='calendarYear', y='revenuePerShare', x_label='Year', y_label='Revenue Per Share ($)')
            
        with netIncomeCol:
            st.text('Net Income Per Share Growth Over the Years')
            st.bar_chart(keyMetrics, x='calendarYear', y='netIncomePerShare', x_label='Year', y_label='Net Income Per Share ($)', color='#FFA500')
        
        with operatingCashFlowCol:
            st.text('Operating Cash Flow Per Share Growth Over the Years')
            st.bar_chart(keyMetrics, x='calendarYear', y='operatingCashFlowPerShare', x_label='Year', y_label='Operating Cash Flow Per Share ($)',color='#00ff00')
            
        with freeCashFlowCol:
            st.text('Free Cash Flow Per Share Growth Over the Years')
            st.bar_chart(keyMetrics, x='calendarYear', y='freeCashFlowPerShare', x_label='Year', y_label='Free Cash Flow Per Share ($)',color='#CB9DF0')
    
    def forecastUI(self):
        st.header('Stock Forecast', anchor='stock-forecast')
        with st.spinner("Loading Prediction..."):
            
            m, forecast = self.forecast.fbProphet(self.historicalData)
            st.subheader(f'Forecast Data for {self.stock_symbol} using Facebook Prophet')
            st.plotly_chart(plot_plotly(m, forecast), theme=None, use_container_width=True)
            st.plotly_chart(plot_components_plotly(m, forecast), theme=None, use_container_width=True)
    
    def display(self):
        
        self.sidebarUI()
        click = self.titleUI()
        
        if click and self.stock_symbol != '':
            st.header(f'Analysing stock: {self.stock_symbol}')
            
            self.introductionUI() 
            self.historicalDataUI()
            keyMetrics = self.keyMetricsUI()
            self.keyMetricsGraphUI(keyMetrics)
            self.forecastUI()
        
        elif click and self.stock_symbol == '':
            st.error('Please enter a stock symbol to analyse!')


if __name__ == "__main__":
    app = mainUI()
    app.display()   