import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# ---- Google Sheets Setup ----
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SHEET_ID = "1BLltyU70nZ4gxCesSp7RrkhBrgW_UUMTSqNdaNcpnUc"

def get_gs_client():
    if "gcp_service_account" in st.secrets:
        creds = Credentials.from_service_account_info(
            st.secrets["gcp_service_account"], scopes=SCOPES
        )
    else:
        creds = Credentials.from_service_account_file(
            "pivotal-leaf-471506-p3-651eda94f85e.json", scopes=SCOPES
        )
    return gspread.authorize(creds)

def get_user_data(phone_number: str):
    client = get_gs_client()
    sh = client.open_by_key(SHEET_ID).sheet1
    data = sh.get_all_records()  # all rows as list of dicts
    df = pd.DataFrame(data)
    user_df = df[df["phone_num"].astype(str) == str(phone_number)]
    return user_df

# ---- Streamlit UI ----


st.title("📊 Personal Dashboard")

phone_input = st.text_input("Enter your phone number to view your data")

if st.button("Fetch My Data"):
    if phone_input.strip():
        df = get_user_data(phone_input.strip())
        if not df.empty:
            st.success(f"Found {len(df)} record(s) for {phone_input}")
            st.dataframe(df)
        else:
            st.warning("No data found for this phone number.")
    else:
        st.error("Please enter a valid phone number.")
    st.subheader("Anxiety index overtime")
    st.line_chart(df["anxiety_index"],use_container_width=True)
    col1,col2=st.columns(2)
    with col1:
        st.subheader("Resilience score overtime")
        st.line_chart(df["resilience_score"],use_container_width=True)
    with col2:
        st.subheader("Recent Results")
        cols=["Anxiety Index","Resilience Score", "Wellbeing Score"]
        new_df = df[["anxiety_index", "resilience_score", "wellbeing_score"]]
        new_df.columns=cols
        new_df=new_df.head(1)
        st.table(new_df)
