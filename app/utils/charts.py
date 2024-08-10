import plotly.express as px
import utils.dataframes as df

grafico_map_estado = px.scatter_geo(
    df.df_rec_estado,
    lat="lat",
    lon="lon",
    scope="south america",
    size="Preço",
    template="seaborn",
    hover_name="Local da compra",
    hover_data={"lat": False, "lon": False},
    title="Receita por Estado",
)

grafico_rec_mensal = px.line(
    df.df_rec_mensal,
    x="Mes",
    y="Preço",
    markers=True,
    range_y=(0, df.df_rec_mensal.max()),
    color="Ano",
    line_dash="Ano",
    title="Receita Mensal",
)

grafico_rec_mensal.update_layout(yaxis_title="Receita")

grafico_rec_estado = px.bar(
    df.df_rec_estado.head(7),
    x="Local da compra",
    y="Preço",
    text_auto=True,
    title="Receita por Estados",
)

grafico_rec_categoria = px.bar(
    df.df_rec_categoria.head(7),
    text_auto=True,
    title="Top 7 Categorias com Maior Receita",
)

grafico_rec_vendedores = px.bar(
    df.df_vendedores[["sum"]],
    x="sum",
    y=df.df_vendedores[["sum"]].index,
    text_auto=True,
    title="Top 7 Vendedores por Receita",
)
 