from prophet import Prophet

class Forecast:
        
    def fbProphet(self, data, period=365):
        
        data = data[['date', 'close']]
        data.columns = ['ds', 'y']
        
        m = Prophet(daily_seasonality=True)
        m.fit(data)
        
        future = m.make_future_dataframe(periods=period)
        prediction = m.predict(future)
        
        return m, prediction