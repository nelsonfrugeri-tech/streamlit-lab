import streamlit as st

# Configurando o layout da página
st.set_page_config(page_title="Model Race", layout="centered", initial_sidebar_state="collapsed")

# Estilo da página
st.markdown("""
    <style>
        /* Corpo da página */
        body {
            background-color: #1e1e1e;
            color: #ffffff;
            font-family: 'Helvetica Neue', sans-serif;
        }

        /* Cabeçalho */
        .header {
            text-align: center;
            margin-bottom: 50px;
        }
        .header .title {
            font-size: 50px;
            font-weight: bold;
        }
        .header .menu {
            font-size: 20px;
            margin-top: 20px;
        }
        .header .menu a {
            color: #f63366;
            text-decoration: none;
            margin: 0 15px;
        }
        .header .menu a:hover {
            text-decoration: underline;
        }

        /* Área de prompt */
        .prompt-section {
            text-align: center;
        }
        .prompt-section .prompt-title {
            font-size: 30px;
            font-weight: bold;
        }
        .prompt-section .prompt-input {
            width: 80%;
            height: 200px;
            margin: 20px auto;
            background-color: #333333;
            border: 1px solid #555555;
            border-radius: 5px;
            color: #ffffff;
        }

        /* Caixa mãe centralizada */
        .box-container {
            margin-bottom: 10px;
            padding: 10px;
        }

        /* Título das configurações com sublinhado */
        .settings-title {
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #f63366;
            font-size: 30px;
            text-align: center;
        }

        /* Seção de seleção de modelos */
        .model-section {
            display: flex;
            justify-content: space-between;
            margin-bottom: 30px;
        }
        .model-section .column {
            width: 45%;
        }
        .model-section .dropdown {
            margin-bottom: 30px;
        }
        .model-section .dropdown label {
            font-size: 18px;
            font-weight: bold;
        }

        /* Seção de configurações */
        .settings-section {
            display: flex;
            justify-content: space-between;
            margin-bottom: 30px;
        }

        .settings-section-column {
            width: 45%;
            margin-left: 10px;  
            margin-right: 10px; 
        }

        .settings-section-label {
            margin-top: 30px;
            margin-bottom: -20px;
            font-size: 18px;
            font-weight: bold;
            display: block;
            text-align: center;
        }

        /* Botão de ação */
        .action-button {
            display: flex;
            justify-content: center;
            margin-bottom: 50px;
        }
        .action-button button {
            padding: 20px 40px;  /* Aumenta o tamanho do botão */
            font-size: 42px !important;  /* Aumenta o tamanho da fonte do botão */
            background-color: #28a745 !important;  /* Altera a cor do botão para verde */
            border: none !important;
            border-radius: 5px !important;
            color: #ffffff !important;
            cursor: pointer !important;
        }
        .action-button button:hover {
            background-color: #218838 !important;  /* Altera a cor de fundo ao passar o mouse */
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown('<div class="header"><div class="title">Model Race</div><div class="menu"><a href="#">configure</a><a href="#">racing</a><a href="#">evaluate</a><a href="#">analysis</a></div></div>', unsafe_allow_html=True)

# Área de prompt
st.markdown('<div class="prompt-section"><div class="prompt-title">prompt</div><textarea class="prompt-input" placeholder="Digite seu prompt aqui..."></textarea></div>', unsafe_allow_html=True)

# Seleção de modelos e provedores
st.markdown('<div class="box-container">', unsafe_allow_html=True)
st.markdown('<div class="model-section">', unsafe_allow_html=True)
st.markdown('<div class="settings-title"><label>providers</label></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:    
    provider1 = st.selectbox("", ["OpenAI", "Bedrock", "Anthropic"], key="provider1")
    model_options1 = {"OpenAI": ["GPT-3.5", "GPT-4", "Codex"], "Bedrock": ["Titan", "Cyclone", "Nimbus"], "Anthropic": ["Claude", "Claude 2", "Ant"]}.get(provider1, [])
    model1 = st.selectbox("", model_options1, key="model1")

with col2:
    provider2 = st.selectbox("", ["OpenAI", "Bedrock", "Anthropic"], key="provider2")    
    model_options2 = {"OpenAI": ["GPT-3.5", "GPT-4", "Codex"], "Bedrock": ["Titan", "Cyclone", "Nimbus"], "Anthropic": ["Claude", "Claude 2", "Ant"]}.get(provider2, [])
    model2 = st.selectbox("", model_options2, key="model2")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Configurações
st.markdown('<div class="box-container">', unsafe_allow_html=True)
st.markdown('<div class="settings-title"><label>settings</label></div>', unsafe_allow_html=True)

st.markdown('<div class="settings-section">', unsafe_allow_html=True)
st.markdown('<div class="settings-section-label"><label>temperature</label></div>', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1], gap="large")  # Ajuste aqui para adicionar gap entre as colunas
with col1:
    temperature = st.slider("", 0.0, 1.0, 0.5, key="temperature1")
with col2:
    temperature2 = st.slider("", 0.0, 1.0, 0.5, key="temperature2")

st.markdown('<div class="settings-section-label"><label>maximum length</label></div>', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1], gap="large")  # Ajuste aqui para adicionar gap entre as colunas
with col1:
    max_tokens = st.number_input("", min_value=1, max_value=1000, value=256, key="max_tokens1")
with col2:
    max_tokens2 = st.number_input("", min_value=1, max_value=1000, value=256, key="max_tokens2")

st.markdown('<div class="settings-section-label"><label>top p</label></div>', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1], gap="large")  # Ajuste aqui para adicionar gap entre as colunas
with col1:
    top_p = st.slider("", 0.0, 1.0, 0.9, key="top_p1")
with col2:
    top_p2 = st.slider("", 0.0, 1.0, 0.9, key="top_p2")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# Botão de ação
st.markdown('<div class="action-button">', unsafe_allow_html=True)
if st.button("racing"):
    st.write("Iniciando a corrida de modelos...")
st.markdown('</div>', unsafe_allow_html=True)
