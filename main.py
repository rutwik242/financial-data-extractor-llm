import pandas as pd
import streamlit as st

from data_extractor import extract

# Title
st.title("Financial Data Extractor")

# Input box
paragraph = st.text_area("Enter financial paragraph:")


# Button to extract data
if st.button("Extract"):
    if paragraph:
        extracted_data = extract(paragraph)

        metrics = {
            "Revenue": "revenue",
            "EPS": "eps",
            "Net Income": "net_income",
            "Operating Income": "operating_income",
            "Free Cash Flow": "free_cash_flow",
            "Gross Margin": "gross_margin",
        }

        data = {
            "Measure": list(metrics.keys()),
            "Estimated": [
                extracted_data.get(f"{key}_expected") or "Not reported"
                for key in metrics.values()
            ],
            "Actual": [
                extracted_data.get(f"{key}_actual") or "Not reported"
                for key in metrics.values()
            ],
        }

        df = pd.DataFrame(data)
        st.table(df)

    else:
        st.warning("Please enter a paragraph to extract data from.")
