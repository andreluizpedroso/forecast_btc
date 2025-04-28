# Previsão de Preços do Ibovespa com LSTM

Este projeto utiliza Machine Learning para prever preços futuros do índice **Ibovespa** (`^BVSP`) com base em dados históricos, utilizando redes neurais LSTM.
Além disso, o projeto gera uma recomendação automática de **Compra** ou **Aguardar** baseada em médias móveis.

---

## 📚 Tecnologias Utilizadas

- Python 3.10+
- Streamlit
- TensorFlow/Keras
- Scikit-learn
- yFinance
- Pandas
- Plotly
- SQLite3

---

## 🎯 Objetivo do Projeto

- Coletar dados históricos do Ibovespa via Yahoo Finance e armazenar em um banco de dados SQLite.
- Treinar um modelo LSTM para previsão de preços.
- Permitir ao usuário escolher uma data futura para previsão através da interface do Streamlit.
- Exibir a previsão de preço e uma recomendação automática baseada nas médias móveis de 20 e 80 dias.
- Visualizar os dados graficamente com Plotly.

---

## 💪 Processo Completo

### 1. Configuração Inicial

Clone o repositório:
```bash
git clone https://github.com/andreluizpedroso/forecast_btc.git
cd forecast_btc
```

Crie um ambiente virtual e ative:
```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

### 2. Estrutura de Arquivos
```
Forecast_BTC/
├── app.py               # Código principal do projeto (Streamlit)
├── finance.db           # Banco de dados SQLite contendo os históricos
├── modelo_lstm.h5       # Modelo LSTM treinado e salvo
├── requirements.txt     # Lista de dependências do projeto
├── README.md            # Documentação
```

### 3. Executar o Projeto

Rode o aplicativo Streamlit:
```bash
streamlit run app.py
```

A aplicação abrirá no seu navegador local em `http://localhost:8501`.

---

## 🔢 Funcionalidades

- [x] Carregamento e armazenamento de dados do Ibovespa em banco SQLite.
- [x] Treinamento de modelo LSTM.
- [x] Interface para escolha de data futura com barra de seleção (até 30 dias).
- [x] Previsão de preço futuro.
- [x] Recomendacão automática de Compra ou Aguardar.
- [x] Gráfico interativo com Preços, MM20 e MM80.

---

## 📊 Exemplo de Uso

1. Acesse o aplicativo Streamlit.
2. Escolha uma data dentro do intervalo permitido (próximos 30 dias).
3. Clique em "Gerar Previsão".
4. Visualize:
   - Preço previsto.
   - Recomendação de Compra ou Aguardar.
   - Gráfico interativo.

---

## 📊 Modelo de Machine Learning

- Arquitetura: LSTM com uma camada de 64 neurônios e uma camada densa final.
- Função de perda: `mse` (Erro Quadrático Médio).
- Otimizador: `adam`
- Treinado com 70% dos dados históricos.
- Previsão incremental para datas futuras.


---

## 📅 Limitações

- Previsão limitada a 30 dias à frente.
- Base de dados `finance.db` deve ser mantida atualizada manualmente se quiser novos dados.

---

## 🌐 Fonte de Dados

- [Yahoo Finance - IBOVESPA (^BVSP)](https://finance.yahoo.com/quote/%5EBVSP)

---

## 👤 Autor

**Andre Luiz Pedroso**  
Projeto desenvolvido para a **Pós-Tech - Tech Challenge Fase 3**.


---

# 🚀 Vamos prever o futuro! 📈
(https://forecastbtc-jisdg7mfjdwzjngbr6suwq.streamlit.app/)
