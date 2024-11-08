from abc import ABC, abstractmethod
import streamlit as st

class baseUI(ABC):
    
    @abstractmethod
    def __init__(self):
        pass
        
    @abstractmethod
    def sidebarUI(self):
        pass
    
    @abstractmethod
    def titleUI(self):
        pass
    
    @abstractmethod
    def display(self):
        pass