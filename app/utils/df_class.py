import pandas as pd
import plotly.express as px

class Teliframe:
    def __init__(self,df) -> None:
        self.df = df
        self.rec_estado = None
        self.rec_mensal = None
        self.rec_categoria = None
        self.df_vendedores = None
        self.update(self.df)
        
    def update(self, df):
        self.df = df
        df_rec_estado_agg = self.df.groupby('Local da compra')[["Preço"]].sum()
        self.rec_estado = self.df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']]
        self.rec_estado = self.rec_estado.merge(df_rec_estado_agg, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)
        self.rec_mensal = self.df.set_index('Data da Compra').groupby(pd.Grouper(freq='ME'))['Preço'].sum().reset_index()
        self.rec_mensal['Ano'] = self.rec_mensal['Data da Compra'].dt.year
        self.rec_mensal['Mes'] = self.rec_mensal['Data da Compra'].dt.month_name()
        self.rec_categoria = self.df.groupby("Categoria do Produto")[["Preço"]].sum().sort_values("Preço", ascending=True)
        self.df_vendedores = pd.DataFrame(self.df.groupby('Vendedor')['Preço'].agg(['sum', 'count']))

    def map_estado_chart(self):
        return px.scatter_geo(
            self.rec_estado,
            lat='lat',
            lon='lon',
            scope='south america',
            size='Preço',
            template='seaborn',
            hover_name='Local da compra',
            hover_data={'lat': False, 'lon': False},
            title='Receita por estado',
            height=450,
            width=900,
            basemap_visible=True,
        )

    def rec_mensal_chart(self):
        return px.line(
            self.rec_mensal,
            x="Mes",
            y="Preço",
            color='Ano',
            title='Receita Mensal'
        )
    
    def rec_estado_chart(self):
        return px.bar(
            self.rec_estado.head(5),
            x='Local da compra',
            y='Preço',
            text_auto=True,
            title='Top 5 Receita por Estado'
        )

    def rec_categoria_chart(self):
        return px.bar(
            self.rec_categoria.head(5),
            orientation='h',
            text_auto=True,
            title='Top 5 Categorias por Receita'
        )

    def rec_vendedores_chart(self):
        return px.bar(
            self.df_vendedores.sort_values('sum', ascending=False).head(5).iloc[::-1],
            x='sum',
            y=self.df_vendedores.sort_values('sum', ascending=False).head(5).iloc[::-1].index,
            text_auto=True,
            title='Top 5 Vendedores por Receita'
        )

    def vendas_vendedores_chart(self):
        return px.bar(
            self.df_vendedores[["count"]].sort_values('count').tail(5),
            x='count',
            y=self.df_vendedores[["count"]].sort_values('count').tail(5).index,
            text_auto=True,
            title='Top 5 Vendedores por Vendas'
        )

    def format_number(self, value, prefix = ''):
        if value < 1000:
            return f'{prefix} {value:.2f}'
        elif value < 1000000:
            value /= 1000
            return f'{prefix} {value:.2f} mil'
        elif value < 1000000000:
            value /= 1000000
            return f'{prefix} {value:.2f} milhões'
        elif value < 1000000000000:
            value /= 1000000000
            return f'{prefix} {value:.2f} bilhões'
        elif value < 1000000000000000:
            value /= 1000000000000
            return f'{prefix} {value:.2f} trilhões'