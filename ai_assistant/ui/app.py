import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Support Ticket Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Support Ticket Assistant")

st.write("Ask questions about your support tickets using natural language.")

question = st.text_input(
    "Ask a question",
    placeholder="Example: How many tickets are open?"
)

if st.button("Ask"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Thinking..."):

            response = requests.post(
                f"{API_URL}/query",
                json={
                    "question": question
                }
            )

        result = response.json()

        if result["success"]:

            st.success(result["answer"])
            st.info(f"Total Records: {result['total_records']}")

            with st.expander("Generated SQL"):

                st.code(
                    result["generated_sql"],
                    language="sql"
                )

            st.subheader("Query Result")

            st.json(result["data"])

        else:

            st.error(result["error"])

st.divider()

st.header("🚨 Anomaly Detection")

if st.button("Detect Anomalies"):

    response = requests.get(
        f"{API_URL}/anomalies"
    )

    anomalies = response.json()

    for title, rows in anomalies.items():

        st.subheader(
            title.replace("_", " ").title()
        )

        if rows:

            st.dataframe(rows)

        else:

            st.info("No anomalies found.")