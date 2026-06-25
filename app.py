import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================
# CONFIGURAÇÃO DA PÁGINA
# ==========================

st.set_page_config(
    page_title="People Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==========================
# DADOS
# ==========================

dados = {
    "Departamento": [
        "TI",
        "TI",
        "RH",
        "Vendas",
        "Financeiro",
        "Vendas",
        "RH",
        "TI"
    ],
    "Idade": [
        25,
        32,
        28,
        35,
        40,
        29,
        31,
        27
    ],
    "Salario": [
        5000,
        7000,
        4500,
        4000,
        8000,
        4200,
        4700,
        6500
    ]
}

df = pd.DataFrame(dados)

# ==========================
# TÍTULO
# ==========================

st.title("📊 Dashboard de People Analytics")

st.markdown("---")

# ==========================
# FILTROS
# ==========================

st.sidebar.header("Filtros")

departamentos = st.sidebar.multiselect(
    "Departamento",
    options=df["Departamento"].unique(),
    default=df["Departamento"].unique()
)

df_filtrado = df[
    df["Departamento"].isin(departamentos)
]

# ==========================
# KPIs
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total de Funcionários",
        len(df_filtrado)
    )

with col2:
    st.metric(
        "Salário Médio",
        f"R$ {df_filtrado['Salario'].mean():,.0f}"
    )

with col3:
    st.metric(
        "Departamentos",
        df_filtrado["Departamento"].nunique()
    )

st.markdown("---")

# ==========================
# TABELA
# ==========================

st.subheader("Base de Dados")

st.dataframe(
    df_filtrado,
    use_container_width=True
)

# ==========================
# GRÁFICOS
# ==========================

col4, col5 = st.columns(2)

with col4:

    fig1 = px.histogram(
        df_filtrado,
        x="Departamento",
        title="Funcionários por Departamento",
        color="Departamento"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with col5:

    fig2 = px.box(
        df_filtrado,
        x="Departamento",
        y="Salario",
        color="Departamento",
        title="Distribuição Salarial"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# ==========================
# SALÁRIOS MÉDIOS
# ==========================

st.subheader("Salário Médio por Departamento")

salario_medio = (
    df_filtrado
    .groupby("Departamento")["Salario"]
    .mean()
    .reset_index()
)

fig3 = px.bar(
    salario_medio,
    x="Departamento",
    y="Salario",
    color="Departamento",
    title="Salário Médio por Departamento"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ==========================
# INSIGHTS
# ==========================

st.markdown("---")

st.subheader("Insights")

st.write(
    f"""
    • Total de funcionários analisados: **{len(df_filtrado)}**

    • Salário médio da empresa: **R$ {df_filtrado['Salario'].mean():,.0f}**

    • Quantidade de departamentos: **{df_filtrado['Departamento'].nunique()}**

    • O dashboard permite explorar os dados de RH de forma interativa.
    """
)

# ==========================
# RODAPÉ
# ==========================

st.markdown("---")

st.caption(
    "Projeto desenvolvido com Python, Pandas, Plotly e Streamlit."
)