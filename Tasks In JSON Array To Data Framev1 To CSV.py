import streamlit as st
import json
import pandas as pd

# Function to convert JSON array to DataFrame
def json_to_df(json_data):
    try:
        df = pd.json_normalize(json_data)
        return df
    except ValueError as e:
        st.error(f"Error in JSON parsing: {e}")
        return None

# Function to download DataFrame as CSV
def download_csv(df):
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='data.csv',
        mime='text/csv',
    )

# Streamlit app layout
def main():
    st.title('Tasks In JSON Array To Data Frame v1 To CSV')
    st.subheader('Input Task JSON Array')

    # Text area for JSON input
    json_input = st.text_area("Enter JSON Array:", height=300)
    if st.button('Convert JSON to DataFrame'):
        if json_input:
            try:
                json_data = json.loads(json_input)
                df = json_to_df(json_data)

                if df is not None:
                    st.write(df)
                    # Download CSV feature
                    download_csv(df)

            except json.JSONDecodeError as e:
                st.error(f"Invalid JSON format: {e.msg}")

if __name__ == "__main__":
    main()
