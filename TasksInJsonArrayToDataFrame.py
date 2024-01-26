import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt

# Function to convert JSON array to DataFrame
def json_to_df(json_data):
    try:
        df = pd.json_normalize(json_data)
        return df
    except ValueError as e:
        st.error(f"Error in JSON parsing: {e}")
        return None

# Streamlit app layout
def main():
    st.title('Tasks In JSON Array To Data Frame')
    st.subheader('Input Task JSON Array')

    # Text area for JSON input
    json_input = st.text_area("Enter JSON Array:", height=300)
    if st.button('Convert JSON to DataFrame'):
        if json_input:
            json_data = json.loads(json_input)
            df = json_to_df(json_data)

            if df is not None:
                st.write(df)

                # Plotting (example with a bar plot)
                st.subheader('Data Visualization')
                if st.button('Generate Plot'):
                    fig, ax = plt.subplots()
                    df.plot(kind='bar', ax=ax)
                    st.pyplot(fig)

if __name__ == "__main__":
    main()
