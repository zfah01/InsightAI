
import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Make project root accessible
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from src.agent import create_agent, answer_business_question

# Page configuration
st.set_page_config(
    page_title="InsightAI",
    page_icon="📊",
    layout="wide"
)

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv(PROJECT_ROOT / "data" / "sales.csv")

df = load_data()

# Initialise InsightAI conversation
if "agent" not in st.session_state:
    st.session_state.agent = create_agent(df)

# Application heading
st.title("📊 InsightAI")
st.caption("Your AI-powered conversational business analytics assistant")

st.divider()

# Business performance dashboard

st.header("Business Overview")

completed_df = df[df["order_status"] == "Completed"]

col1, col2, col3 = st.columns(3)

with col1:
    total_revenue = completed_df["revenue"].sum()
    st.metric("Total Revenue", f"£{total_revenue:,.2f}")

with col2:
    st.metric("Total Orders", len(df))

with col3:
    cancellation_rate = (
        (df["order_status"] == "Cancelled").sum() / len(df)
    ) * 100

    st.metric("Cancellation Rate", f"{cancellation_rate:.1f}%")

st.divider()

# Revenue by region and product

col1, col2 = st.columns(2)

with col1:
    st.subheader("Revenue by Region")

    region_revenue = (
        completed_df.groupby("region")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(region_revenue)

with col2:
    st.subheader("Revenue by Product")

    product_revenue = (
        completed_df.groupby("product")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(product_revenue)

st.divider()

# Sidebar
with st.sidebar:
    st.header("About InsightAI")
    st.write(
        "Ask questions about business performance, "
        "revenue, products, regions and orders."
    )

    st.metric("Total orders", len(df))
    st.metric(
        "Completed orders",
        len(df[df["order_status"] == "Completed"])
    )

    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.session_state.agent = create_agent(df)
        st.rerun()

# Initialise chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
question = st.chat_input("Ask InsightAI a business question...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Analysing your business data..."):
            try:
                answer = answer_business_question(
                    st.session_state.agent,
                    question
                    )
                st.markdown(answer)

            except Exception as error:
                answer = (
                    "Sorry, something went wrong while "
                    "analysing your question."
                )
                st.error(answer)
                st.exception(error)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
