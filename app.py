import streamlit as st
from model.gemini import geminiService
from model.fmp import Fmp
import pandas as pd
import plotly.graph_objects as go

class mainUI:
    
    def __init__(self):
        st.set_page_config(layout="wide") 
        self.fmp = Fmp()
        self.gemini = geminiService()
            
    def sidebarUI(self):
        with st.sidebar:
            st.title('Navigation Bar')
            st.markdown("[Introduction](#introduction)")
            st.markdown("[Historical Data](#historicalData)")
            st.markdown("[Key Metrics](#key-metrics)")
            st.markdown("[Key Metrics Graph](#key-metrics-graph)")

    def titleUI(self):
        center_title = st.columns([1, 2, 1])
        
        with center_title[1]:
            # Set the title of the app
            st.html("<h1 style='text-align: center;'>Simple Stock Analyser</h1>")

    def introductionUI(self):
        st.header('Introduction',anchor='introduction')
        with st.spinner("Loading..."):
            with st.expander("See Introduction"):            
            
                # Get introduction of the company
                # st.write(self.gemini.get_introduction(symbol=self.stock_symbol))
                st.write('Successs....') ## remove it when done

    def historicalDataUI(self):
        st.header('Historical Data',anchor='historicalData')
        with st.spinner("Loading Historical Data..."):
            
            # Get key metrics of the company
            historicalData = self.fmp.get_historical_data(symbol=self.stock_symbol) 
            historicalData = pd.DataFrame(historicalData['historical'])
            
            # Calculate the Simple Moving Average (e.g., 50-day SMA)
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

        
            # Add the SMA line
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
            
            # Customize the layout
            fig.update_layout(
                title=f"{self.stock_symbol} Historical Stock Price (USD)",
                xaxis_title="Date",
                yaxis_title="Price" 
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    def keyMetricsUI(self):
        st.header('Key Metrics', anchor='key-metrics')
        data = [{'symbol': 'MSFT', 'date': '2024-06-30', 'calendarYear': '2024', 'period': 'FY', 'revenuePerShare': 32.986408289597634, 'netIncomePerShare': 11.860584039833132, 'operatingCashFlowPerShare': 15.953169156237385, 'freeCashFlowPerShare': 9.967837437760732, 'cashPerShare': 10.165926524020993, 'bookValuePerShare': 36.12932310590769, 'tangibleBookValuePerShare': 16.37195532229848, 'shareholdersEquityPerShare': 36.12932310590769, 'interestDebtPerShare': 7.342887902032028, 'marketCap': 3393960630000, 'enterpriseValue': 3442772630000, 'peRatio': 38.508221725515114, 'priceToSalesRatio': 13.846005784874471, 'pocfratio': 28.629421247089788, 'pfcfRatio': 45.82037005035709, 'pbRatio': 12.641532161041727, 'ptbRatio': 12.641532161041727, 'evToSales': 14.045139277584223, 'enterpriseValueOverEBITDA': 26.137053067112056, 'evToOperatingCashFlow': 29.04117007456895, 'evToFreeCashFlow': 46.479359398415035, 'earningsYield': 0.025968480370970007, 'freeCashFlowYield': 0.021824354515273207, 'debtToEquity': 0.19230697601656752, 'debtToAssets': 0.10080775065750552, 'netDebtToEBITDA': 0.3705739447312481, 'currentRatio': 1.2749549031815206, 'interestCoverage': 37.285519591141394, 'incomeQuality': 1.345057638195516, 'dividendYield': 0.006414629506176681, 'payoutRatio': 0.24701597531088318, 'salesGeneralAndAdministrativeToRevenue': 0.031041685364838735, 'researchAndDdevelopementToRevenue': 0.12038903076835208, 'intangiblesToTotalAssets': 0.2866606920062558, 'capexToOperatingCashFlow': 0.3751813611364173, 'capexToRevenue': 0.18144842160230415, 'capexToDepreciation': 1.9956476869924171, 'stockBasedCompensationToRevenue': 0.04379043904667879, 'grahamNumber': 98.19157113773981, 'roic': 0.2795375057846275, 'returnOnTangibleAssets': 0.24123981102844974, 'grahamNetNet': -16.79814291481631, 'workingCapital': 34448000000, 'tangibleAssetValue': 121660000000, 'netCurrentAssetValue': -83952000000, 'investedCapital': 335817000000, 'averageReceivables': 52806000000, 'averagePayables': 20045500000, 'averageInventory': 1873000000, 'daysSalesOutstanding': 84.76293437553545, 'daysPayablesOutstanding': 108.32690179992983, 'daysOfInventoryOnHand': 6.136357503305718, 'receivablesTurnover': 4.3061274682032185, 'payablesTurnover': 3.3694308056010183, 'inventoryTurnover': 59.481540930979136, 'roe': 0.32828137978299815, 'capexPerShare': 5.985331718476652}, {'symbol': 'MSFT', 'date': '2023-06-30', 'calendarYear': '2023', 'period': 'FY', 'revenuePerShare': 28.460247112543648, 'netIncomePerShare': 9.718103679828095, 'operatingCashFlowPerShare': 11.76228847703465, 'freeCashFlowPerShare': 7.987510072522159, 'cashPerShare': 14.942519473542841, 'bookValuePerShare': 27.695809830781627, 'tangibleBookValuePerShare': 17.32084340585549, 'shareholdersEquityPerShare': 27.695809830781627, 'interestDebtPerShare': 6.608246038141284, 'marketCap': 2535660840000, 'enterpriseValue': 2560921840000, 'peRatio': 35.04181589530272, 'priceToSalesRatio': 11.96546181251917, 'pocfratio': 28.951849010070564, 'pfcfRatio': 42.63406204287516, 'pbRatio': 12.29572278552829, 'ptbRatio': 12.29572278552829, 'evToSales': 12.084665266734303, 'enterpriseValueOverEBITDA': 24.35378098996719, 'evToOperatingCashFlow': 29.24027585576945, 'evToFreeCashFlow': 43.05879512400168, 'earningsYield': 0.02853733388097755, 'freeCashFlowYield': 0.023455423951730073, 'debtToEquity': 0.2290578645446919, 'debtToAssets': 0.11465959182088277, 'netDebtToEBITDA': 0.240226332556702, 'currentRatio': 1.76916725076573, 'interestCoverage': 44.98119918699187, 'incomeQuality': 1.2103481156976825, 'dividendYield': 0.00780861528783952, 'payoutRatio': 0.2736280593137187, 'salesGeneralAndAdministrativeToRevenue': 0.03574546398320081, 'researchAndDdevelopementToRevenue': 0.12832975485454073, 'intangiblesToTotalAssets': 0.18751577761811367, 'capexToOperatingCashFlow': 0.3209221072823183, 'capexToRevenue': 0.13263336715192411, 'capexToDepreciation': 2.027775773753697, 'stockBasedCompensationToRevenue': 0.04535308968218389, 'grahamNumber': 77.81961132791403, 'roic': 0.28297384820877547, 'returnOnTangibleAssets': 0.2161810924821644, 'grahamNetNet': -7.618184260005372, 'workingCapital': 80108000000, 'tangibleAssetValue': 128971000000, 'netCurrentAssetValue': -21496000000, 'investedCapital': 267347000000, 'averageReceivables': 46474500000, 'averagePayables': 18547500000, 'averageInventory': 3121000000, 'daysSalesOutstanding': 83.85966071302173, 'daysPayablesOutstanding': 100.27898820278456, 'daysOfInventoryOnHand': 13.854516192703034, 'receivablesTurnover': 4.3525098586920805, 'payablesTurnover': 3.639845261121857, 'inventoryTurnover': 26.3452, 'roe': 0.35088714643856406, 'capexPerShare': 3.77477840451249}, {'symbol': 'MSFT', 'date': '2022-06-30', 'calendarYear': '2022', 'period': 'FY', 'revenuePerShare': 26.45010672358591, 'netIncomePerShare': 9.703575240128067, 'operatingCashFlowPerShare': 11.877668089647813, 'freeCashFlowPerShare': 8.691168623265742, 'cashPerShare': 13.975053361792956, 'bookValuePerShare': 22.217449306296693, 'tangibleBookValuePerShare': 11.702241195304163, 'shareholdersEquityPerShare': 22.217449306296693, 'interestDebtPerShare': 6.916221985058698, 'marketCap': 1925197680000, 'enterpriseValue': 1972536680000, 'peRatio': 26.467564134290193, 'priceToSalesRatio': 9.709979724617945, 'pocfratio': 21.622931206828774, 'pfcfRatio': 29.550686579993553, 'pbRatio': 11.559832834960549, 'ptbRatio': 11.559832834960549, 'evToSales': 9.948740001008726, 'enterpriseValueOverEBITDA': 19.744123717531654, 'evToOperatingCashFlow': 22.15462099174482, 'evToFreeCashFlow': 30.27731323581329, 'earningsYield': 0.03778209414837857, 'freeCashFlowYield': 0.033840161286710045, 'debtToEquity': 0.2989095843691081, 'debtToAssets': 0.13644611336476264, 'netDebtToEBITDA': 0.4738401481407337, 'currentRatio': 1.7846069708251824, 'interestCoverage': 40.41832283082889, 'incomeQuality': 1.224050702521378, 'dividendYield': 0.009419811891732594, 'payoutRatio': 0.24931947537738183, 'salesGeneralAndAdministrativeToRevenue': 0.029757401523175468, 'researchAndDdevelopementToRevenue': 0.12362939426035205, 'intangiblesToTotalAssets': 0.21604538975989473, 'capexToOperatingCashFlow': 0.2682765204694783, 'capexToRevenue': 0.12047208352246935, 'capexToDepreciation': 1.6518672199170124, 'stockBasedCompensationToRevenue': 0.037837292580824126, 'grahamNumber': 69.6472938972942, 'roic': 0.3349096839750487, 'returnOnTangibleAssets': 0.25431266563642846, 'grahamNetNet': -7.800727054429029, 'workingCapital': 74602000000, 'tangibleAssetValue': 87720000000, 'netCurrentAssetValue': -28614000000, 'investedCapital': 240970000000, 'averageReceivables': 41152000000, 'averagePayables': 17081500000, 'averageInventory': 3189000000, 'daysSalesOutstanding': 81.48113683361075, 'daysPayablesOutstanding': 110.69433359936153, 'daysOfInventoryOnHand': 21.80095770151636, 'receivablesTurnover': 4.479564402069542, 'payablesTurnover': 3.2973684210526315, 'inventoryTurnover': 16.742383752004276, 'roe': 0.4367546925099975, 'capexPerShare': 3.1864994663820703}, {'symbol': 'MSFT', 'date': '2021-06-30', 'calendarYear': '2021', 'period': 'FY', 'revenuePerShare': 22.27216112362528, 'netIncomePerShare': 8.118590168278786, 'operatingCashFlowPerShare': 10.16827878627269, 'freeCashFlowPerShare': 7.435802305551875, 'cashPerShare': 17.269643566980257, 'bookValuePerShare': 18.813833311249503, 'tangibleBookValuePerShare': 11.193454352722936, 'shareholdersEquityPerShare': 18.813833311249503, 'interestDebtPerShare': 8.015370345832782, 'marketCap': 2044482299999.9998, 'enterpriseValue': 2098033299999.9998, 'peRatio': 33.367862447160974, 'priceToSalesRatio': 12.163166317643137, 'pocfratio': 26.641677091477717, 'pfcfRatio': 36.43184539719876, 'pbRatio': 14.398979491224608, 'ptbRatio': 14.398979491224608, 'evToSales': 12.48175539003379, 'enterpriseValueOverEBITDA': 25.026938721952497, 'evToOperatingCashFlow': 27.339500912170962, 'evToFreeCashFlow': 37.38610249830713, 'earningsYield': 0.029968955955255765, 'freeCashFlowYield': 0.027448513494100685, 'debtToEquity': 0.4095134800123954, 'debtToAssets': 0.1742050877976146, 'netDebtToEBITDA': 0.6387971036967232, 'currentRatio': 2.0799936835218875, 'interestCoverage': 29.80221653878943, 'incomeQuality': 1.2524685413980512, 'dividendYield': 0.008080774286967414, 'payoutRatio': 0.269638164874084, 'salesGeneralAndAdministrativeToRevenue': 0.030382894674218265, 'researchAndDdevelopementToRevenue': 0.12324496692208843, 'intangiblesToTotalAssets': 0.17230263138184249, 'capexToOperatingCashFlow': 0.26872556684910087, 'capexToRevenue': 0.12268573604302509, 'capexToDepreciation': 1.7646756803012151, 'stockBasedCompensationToRevenue': 0.036397601256484696, 'grahamNumber': 58.6232935643997, 'roic': 0.3010432193294547, 'returnOnTangibleAssets': 0.22178102422285606, 'grahamNetNet': -4.187988604743607, 'workingCapital': 95749000000, 'tangibleAssetValue': 84477000000, 'netCurrentAssetValue': -7385000000, 'investedCapital': 224063000000, 'averageReceivables': 35027000000, 'averagePayables': 13846500000, 'averageInventory': 2265500000, 'daysSalesOutstanding': 82.6096746942078, 'daysPayablesOutstanding': 105.95985219788636, 'daysOfInventoryOnHand': 18.420508500536073, 'receivablesTurnover': 4.418368688063507, 'payablesTurnover': 3.4447009167051377, 'inventoryTurnover': 19.814871016691956, 'roe': 0.4315223821731414, 'capexPerShare': 2.732476480720816}, {'symbol': 'MSFT', 'date': '2020-06-30', 'calendarYear': '2020', 'period': 'FY', 'revenuePerShare': 18.793035479632064, 'netIncomePerShare': 5.818791064388962, 'operatingCashFlowPerShare': 7.973061760840999, 'freeCashFlowPerShare': 5.944021024967149, 'cashPerShare': 17.94047306176084, 'bookValuePerShare': 15.545860709592642, 'tangibleBookValuePerShare': 8.924441524310119, 'shareholdersEquityPerShare': 15.545860709592642, 'interestDebtPerShare': 8.662023653088042, 'marketCap': 1548711100000, 'enterpriseValue': 1606133100000, 'peRatio': 34.97461891104537, 'priceToSalesRatio': 10.829011642135441, 'pocfratio': 25.52469880510919, 'pfcfRatio': 34.23776583985498, 'pbRatio': 13.09094451582364, 'ptbRatio': 13.09094451582364, 'evToSales': 11.230521973219592, 'enterpriseValueOverEBITDA': 23.483194677973536, 'evToOperatingCashFlow': 26.471085290482076, 'evToFreeCashFlow': 35.5072091789362, 'earningsYield': 0.028592162863687102, 'freeCashFlowYield': 0.029207513266999895, 'debtToEquity': 0.5352904381931296, 'debtToAssets': 0.2101715503250794, 'netDebtToEBITDA': 0.8395642956356458, 'currentRatio': 2.5157654542940118, 'interestCoverage': 20.439598610575068, 'incomeQuality': 1.370226507983108, 'dividendYield': 0.009773933950625136, 'payoutRatio': 0.34183961518484224, 'salesGeneralAndAdministrativeToRevenue': 0.03573751005139321, 'researchAndDdevelopementToRevenue': 0.1347341187987274, 'intangiblesToTotalAssets': 0.16723252718951515, 'capexToOperatingCashFlow': 0.25448702101359705, 'capexToRevenue': 0.10796769569625564, 'capexToDepreciation': 1.206705220381369, 'stockBasedCompensationToRevenue': 0.036982134741111075, 'grahamNumber': 45.11438347320392, 'roic': 0.24344253400843888, 'returnOnTangibleAssets': 0.1764731669602506, 'grahamNetNet': -2.8284165571616295, 'workingCapital': 109605000000, 'tangibleAssetValue': 67915000000, 'netCurrentAssetValue': -1092000000, 'investedCapital': 212898000000, 'averageReceivables': 30767500000, 'averagePayables': 10956000000, 'averageInventory': 1979000000, 'daysSalesOutstanding': 81.69782889906652, 'daysPayablesOutstanding': 99.25452493597813, 'daysOfInventoryOnHand': 15.010959677069318, 'receivablesTurnover': 4.4676829839742584, 'payablesTurnover': 3.677414205905826, 'inventoryTurnover': 24.3155672823219, 'roe': 0.37429841763592103, 'capexPerShare': 2.02904073587385}]
        
        with st.spinner("Loading Key Metrics..."):
            # Get key metrics of the company
            # data = self.fmp.get_company_key_metrics(period='annual', symbol=self.stock_symbol)
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
    
    def predictionUI(self):
        st.header('Prediction', anchor='prediction')
        with st.spinner("Loading Prediction..."):
            pass
    
    def main(self):
        self.sidebarUI()
        self.titleUI()

        # Add a text input for the stock symbol
        self.stock_symbol = st.text_input('Enter Stock Ticker Symbol', '').upper()

        # Add a button to submit the form
        if st.button('Analyze'):
            st.header(f'Analyzing stock: {self.stock_symbol}')
            
            self.introductionUI() 
            self.historicalDataUI()
            keyMetrics = self.keyMetricsUI()
            self.keyMetricsGraphUI(keyMetrics)
            


if __name__ == "__main__":
    app = mainUI()
    app.main()   