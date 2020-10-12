import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.set_option('deprecation.showPyplotGlobalUse', False)

dataframe_loc = 'data/consolidated_df.csv'

df = pd.read_csv(dataframe_loc, sep='|')
df.drop(['Unnamed: 0'], axis=1, inplace=True)


def menu():
    menu_dispatcher = {
        'Sobre o Projeto': intro,
        'Análise Exploratória dos Dados': eda,
        'Testes de Hipótese': hypothesis_testing
    }

    st.sidebar.header('**Ciência de Dados**\n'
                      '**Análise de Plataformas de Streaming**')

    page = st.sidebar.radio("", ('Sobre o Projeto',
                                 'Análise Exploratória dos Dados',
                                 'Testes de Hipótese'))

    menu_dispatcher[page]()


def intro():
    st.title('Análise de Plataformas de Streaming')

    '''
        Este projeto foi desenvolvido como requisito para aprovação na disciplina de 
        _Introdução aos Sistemas Inteligentes_ da PUC Minas. O trabalho teve como objetivo 
        a aplicação dos fundamentos teóricos de Ciência dos Dados à uma base de dados escolhida pelo grupo.
    '''

    st.header('Bases de Dados utilizadas')

    '''
    - Base principal: [Movies on Netflix, Prime Video, Hulu and Disney+](https://www.kaggle.com/ruchi798/movies-on-netflix-prime-video-hulu-and-disney)
    - Base para enriquecimento: [The Oscar Award, 1927 - 2020](https://www.kaggle.com/unanimad/the-oscar-award)
    '''

    st.header('Hipóteses Iniciais')

    '''
        1. A idade de um filme e a sua nota no IMDB são negativamente correlatas
        2. A maior parte dos filmes do Disney Plus tem classificação etária < 16 anos
        3. Filmes de terror têm notas inferiores no IMDB
        4. Filmes que foram indicados ao Oscar têm as maiores notas no IMDB 
    '''

    st.header('Fatos e Julgamentos')

    '''
        1. De quando é o filme mais antigo do dataset? Que filme é esse?
        2. Quantos filmes existem no dataset?
        3. Qual é a duração média dos filmes?
        4. Qual é o filme com mais indicações ao Oscar? Quantas indicações ele possui?
        5. Qual a média de avaliação no IMDB? Qual é essa média por plataforma?
        6. Qual a plataforma com o maior número de vencedores de categorias do Oscar?
        7. Quantos idiomas diferentes existem no dataset? Quais são?
        8. Qual é a linguagem mais frequente?
        9. Como é a distribuição de filmes produzidos por ano?
        10. Qual a quantidade de filmes produzidos por país?
        11. Quais são os 10 filmes mais longos?
        12. Quais são os 10 filmes com mais indicações ao Oscar?
        13. Qual é a participação de cada Plataforma de Streaming no dataset?
        14. Quais são os títulos com maior nota no IMDB?
        15. Quais são os diretores mais produtivos (com maior número de produções)?
        16. Quais são os 10 gêneros mais comuns?
    '''

    st.header('Autores')

    '''
    * **Lucas Rotsen** - [LucasRotsen](https://github.com/LucasRotsen)
    * **Laercio Nazareno** - [LaercioNazareno](https://github.com/LaercioNazareno)
    '''


def eda():
    st.title('Análise Exploratória dos Dados')

    st.text('')

    st.markdown('#### De quando é o filme mais antigo do dataset? Que filme é esse?')

    st.text('')

    st.table(df[df['YEAR'] == df['YEAR'].min()][['TITLE', 'YEAR']])

    st.markdown('#### Quantos filmes existem no dataset?')

    st.text('')

    st.markdown(df.shape[0])

    st.markdown('#### Qual é a duração média dos filmes?')

    st.text('')

    f"{round(df['DURATION'].mean())} minutos"

    st.markdown('#### Qual é o filme com mais indicações ao Oscar? Quantas indicações ele possui?')

    st.text('')

    st.table(df[df['#OSCAR_INDICATIONS'] == df['#OSCAR_INDICATIONS'].max()][['TITLE', '#OSCAR_INDICATIONS']])

    st.markdown('#### Qual a média de avaliação no IMDB? Qual é essa média por plataforma?')

    st.text('')

    st.markdown(f"Média geral: **{round(df['IMDB'].mean(), 2)}**")

    imdb_dict = {'Netflix': round(df[df['NETFLIX'] == 1]['IMDB'].mean(), 2),
                 'Prime Video': round(df[df['PRIME_VIDEO'] == 1]['IMDB'].mean(), 2),
                 'Hulu': round(df[df['HULU'] == 1]['IMDB'].mean(), 2),
                 'Disney+': round(df[df['DISNEY_PLUS'] == 1]['IMDB'].mean(), 2)}

    st.markdown(f"Prime Video IMDB mean: **{imdb_dict['Prime Video']}**")
    st.markdown(f"Hulu IMDB mean: **{imdb_dict['Hulu']}**")
    st.markdown(f"Netflix IMDB mean: **{imdb_dict['Netflix']}**")
    st.markdown(f"Disney+ IMDB mean: **{imdb_dict['Disney+']}**")

    imdb_dict = {k: v for k, v in sorted(imdb_dict.items(), key=lambda item: item[1])}

    plt.figure(figsize=(12, 6))

    chart = sns.barplot(
        list(imdb_dict.keys()),
        list(imdb_dict.values())
    ).set_title('IMDB mean per Streaming Platform')

    plt.xticks(
        rotation=45,
        horizontalalignment='right',
        fontweight='light',
        fontsize='x-large'
    )

    st.pyplot()

    st.markdown('#### Qual a plataforma com o maior número de vencedores de categorias do Oscar?')

    st.text('')

    oscar_winners_dict = {'Netflix': df[(df['NETFLIX'] == 1) & (df['WON_OSCAR_CATEGORY'] == 1)].shape[0],
                          'Prime Video': df[(df['PRIME_VIDEO'] == 1) & (df['WON_OSCAR_CATEGORY'] == 1)].shape[0],
                          'Hulu': df[(df['HULU'] == 1) & (df['WON_OSCAR_CATEGORY'] == 1)].shape[0],
                          'Disney+': df[(df['DISNEY_PLUS'] == 1) & (df['WON_OSCAR_CATEGORY'] == 1)].shape[0]}

    oscar_winners_dict = {k: v for k, v in sorted(oscar_winners_dict.items(), key=lambda item: item[1])}

    plt.figure(figsize=(12, 6))

    chart = sns.barplot(
        list(oscar_winners_dict.keys()),
        list(oscar_winners_dict.values())
    ).set_title('# of Oscar Winners per Streaming Platform')

    plt.xticks(
        rotation=45,
        horizontalalignment='right',
        fontweight='light',
        fontsize='x-large'
    )

    st.pyplot()

    st.markdown('#### Quantos idiomas diferentes de filmes existem no dataset? Quais são os Top #10?')

    st.text('')

    languages = list(df['LANGUAGE'].dropna().unique())

    unique_languages = []

    for language in languages:
        if ',' in language:
            langs = language.split(',')
            unique_languages += langs
        else:
            unique_languages.append(language)

    unique_languages = set(unique_languages)

    st.markdown(f'Linguagens diferentes: **{len(unique_languages)}**')

    movie_count_by_language = df.groupby('LANGUAGE')['TITLE'].count().reset_index().sort_values('TITLE',
                                                                                                ascending=False).head(
        10).rename(columns={'TITLE': 'Movie Count'})
    fig = px.bar(movie_count_by_language, x='LANGUAGE', y='Movie Count', color='LANGUAGE', height=600)

    st.plotly_chart(fig)

    st.markdown('#### Como é a distribuição de filmes produzidos por ano?')

    st.text('')

    yearly_movie_count = df.groupby('YEAR')['TITLE'].count().reset_index().rename(columns={'TITLE': 'Movie Count'})
    fig = px.bar(yearly_movie_count, x='YEAR', y='Movie Count', color='Movie Count', height=600)

    st.plotly_chart(fig)

    st.markdown('#### Qual a quantidade de filmes produzidos por país?')

    st.text('')

    movies_by_country = df.groupby('COUNTRY')['TITLE'].count().reset_index().sort_values('TITLE', ascending=False).head(
        10).rename(columns={'TITLE': 'Movie Count'})
    fig = px.bar(movies_by_country, x='COUNTRY', y='Movie Count', color='COUNTRY', height=600)

    st.plotly_chart(fig)

    st.markdown('#### Quais são os 10 filmes mais longos?')

    st.text('')

    lengthiest_movies = df.sort_values('DURATION', ascending=False).head(10)
    fig = px.bar(lengthiest_movies, x='TITLE', y='DURATION', color='TITLE', height=600)

    st.plotly_chart(fig)

    st.markdown('#### Quais são os 10 filmes com mais indicações ao Oscar?')

    st.text('')

    lengthiest_movies = df.sort_values('#OSCAR_INDICATIONS', ascending=False).head(10)
    fig = px.bar(lengthiest_movies, x='TITLE', y='#OSCAR_INDICATIONS', color='TITLE', height=600)

    st.plotly_chart(fig)

    st.markdown('#### Qual é a participação de cada Plataforma de Streaming no dataset?')

    st.text('')

    digital_platforms = df[['NETFLIX', 'HULU', 'PRIME_VIDEO', 'DISNEY_PLUS']].sum().reset_index()
    digital_platforms.columns = ['Platform', 'Movie Count']
    digital_platforms = digital_platforms.sort_values('Movie Count', ascending=False)
    labels = digital_platforms.Platform
    values = digital_platforms['Movie Count']
    pie = go.Pie(labels=labels, values=values, marker=dict(line=dict(color='#000000', width=1)))
    fig = go.Figure(data=[pie])

    st.plotly_chart(fig)

    st.markdown('#### Quais são os títulos com maior nota no IMDB?')

    st.text('')

    top_rated_movies = df.sort_values('IMDB', ascending=False).head(10)
    fig = px.bar(top_rated_movies, x='TITLE', y='IMDB', color='IMDB', height=600)

    st.plotly_chart(fig)

    st.markdown('#### Quais são os diretores mais produtivos (com maior número de produções)?')

    st.text('')

    top_directors = df.groupby('DIRECTORS')['TITLE'].count().reset_index().rename(
        columns={'TITLE': 'Movie Count'}).sort_values('Movie Count', ascending=False).head(10)
    fig = px.bar(top_directors, x='DIRECTORS', y='Movie Count', color='Movie Count', height=600)

    st.plotly_chart(fig)

    st.markdown('#### Quais são os 10 gêneros mais comuns?')

    st.text('')

    top_genres = df.groupby('GENRES')['TITLE'].count().reset_index().rename(
        columns={'TITLE': 'Movie Count'}).sort_values('Movie Count', ascending=False).head(10)
    fig = px.bar(top_genres, x='GENRES', y='Movie Count', color='Movie Count', height=600)

    st.plotly_chart(fig)

    st.markdown('### Como as colunas se relacionam entre si?')

    st.text('')

    df_corr = df.corr()

    fig, ax = plt.subplots(figsize=(12, 10))

    mask = np.triu(np.ones_like(df_corr, dtype=np.bool))

    mask = mask[1:, :-1]
    corr = df_corr.iloc[1:, :-1].copy()

    cmap = sns.diverging_palette(0, 230, 90, 60, as_cmap=True)

    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f",
                linewidths=5, cmap=cmap, vmin=-1, vmax=1,
                cbar_kws={"shrink": .8}, square=True)

    yticks = [i.upper() for i in corr.index]
    xticks = [i.upper() for i in corr.columns]
    plt.yticks(plt.yticks()[0], labels=yticks, rotation=0)
    plt.xticks(plt.xticks()[0], labels=xticks)

    st.pyplot(fig)


def hypothesis_testing():
    st.title('Testes de Hipótese')

    st.text('')

    st.markdown('#### A idade de um filme e a sua nota no IMDB são negativamente correlatas')

    st.text('')

    st.markdown('Através do gráfico abaixo podemos observar que não há correlação clara entre as variáveis:')

    fig = px.scatter(df, x='MOVIE_AGE', y='IMDB')
    st.plotly_chart(fig)

    st.markdown('Ainda assim um fato curioso pode ser observado. A distribuição das notas no IMDB parece se afunilar'
                ' conforme a idade dos filmes aumenta. Filmes que possuem entre 80 e 100 anos , por exemplo, possuem a '
                ' maior parte das notas distribuídas entre 4 e 8.')

    st.markdown('#### A maior parte dos filmes do Disney Plus tem classificação etária < 16 anos')

    st.text('')

    st.markdown('Conforme pode ser observado na tabela abaixo, de fato a maior parte dos filmes dos Disney + possui '
                'faixa etária livre ou inferior à 16 anos.')

    st.table(df[df['DISNEY_PLUS'] == 1]['AGE_CLASSIFICATION'].value_counts())

    st.markdown('#### Filmes de terror têm notas inferiores no IMDB')

    st.text('')

    st.markdown('A tabela abaixo apresenta os gêneros dos 10 filmes com menores notas no IMDB. Podemos observar que '
                'entre eles há, de fato, filmes de terror.')

    st.table(df.sort_values(by=['IMDB'])[['GENRES', 'IMDB']].head(10))

    st.markdown('#### Filmes que foram indicados ao Oscar têm as maiores notas no IMDB')

    st.text('')

    st.markdown(f"A maior nota no IMDB dos filmes deste dataset é **{df['IMDB'].max()}**")

    sorted_df = df[df['WON_OSCAR_CATEGORY'] == 1]
    sorted_df = sorted_df.sort_values(by=['IMDB'], ascending=False)[['TITLE', 'IMDB']].head(10)

    fig = px.bar(sorted_df, x='TITLE', y='IMDB', color='IMDB', height=600)
    st.plotly_chart(fig)


if __name__ == '__main__':
    menu()
