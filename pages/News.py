import streamlit as st
from services.news import News
from utils.base_ui import baseUI

class NewsUI(baseUI):
    
    def __init__(self):
        st.set_page_config(layout="wide", page_title='Stock Analyser Dashboard', page_icon='📈') 
        self.news = News()
        
    def sidebarUI(self):
        pass
    
    def titleUI(self):
        center_title = st.columns([1, 2, 1])
        
        with center_title[1]:
            # Set the title of the app
            st.html("<h1 style='text-align: center;'>News Searcher</h1>")
            
            # Add a text input for the stock symbol
            self.search = st.text_input('Enter the News you wanted to find', '').upper()
            
            click = st.button('Search')
            
            return click
    
    def newsUI(self, news):
        with st.spinner("Loading News..."): 
            st.subheader(f"Total Results: {news['articles'].__len__()}")
        
            for article in news['articles']:
                if article['title'] != '[Removed]':
                    with st.container(border=True):
                        
                        image, text = st.columns([1, 4])
                        
                        with image: 
                            if article['urlToImage'] is not None:
                                st.image(article['urlToImage'])
                            else:
                                st.image('https://static.vecteezy.com/system/resources/previews/004/141/669/non_2x/no-photo-or-blank-image-icon-loading-images-or-missing-image-mark-image-not-available-or-image-coming-soon-sign-simple-nature-silhouette-in-frame-isolated-illustration-vector.jpg')
                        
                        with text:
                            st.subheader(article['title'])
                            st.write(article['description'])
                            st.write(f"Author: {article['author']}")
                            st.write(f"Published at: {article['publishedAt']}")
                            st.write(f"Source: {article['source']['name']}")
                            
                            with st.expander("Read more"):
                                st.markdown(f'<a href="{article["url"]}" target="_blank">{article["content"]}</a>', unsafe_allow_html=True)
         
    def display(self):
        self.sidebarUI()
        click = self.titleUI()
        
        if click and self.search != '':           
            news = self.news.get_news(self.search)
            self.newsUI(news)
                
        elif click and self.search == '':
            st.error('Please insert text before searching!')

news = NewsUI()
news.display()