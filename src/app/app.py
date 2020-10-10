import re
import time
import calendar
import webbrowser
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from datetime import date
from streamlit import caching
from datetime import datetime
import plotly.graph_objs as go
from collections import Counter
import matplotlib.pyplot as plt


def menu():

    menu_dispatcher = {
        'Introdução': intro,
        'Análise Exploratória dos Dados': eda,
        'Testes de Hipótese': hypothesis_testing
    }

    st.sidebar.header('**Ciência de Dados**\n'
                      '**Análise de Plataformas de Streaming**')

    page = st.sidebar.radio("", ('Introdução',
                                 'Análise Exploratória dos Dados',
                                 'Testes de Hipótese'))

    menu_dispatcher[page]()


def intro():
    st.title('Introdução')

    '''
        Introdução
    '''


def eda():
    st.title('Análise Exploratória dos Dados')


def hypothesis_testing():
    st.title('Testes de Hipótese')


if __name__ == '__main__':
    menu()
