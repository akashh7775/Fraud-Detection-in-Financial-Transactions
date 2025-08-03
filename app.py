import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics import classification_report

st.set_page_config(page_title="Fraud Detection App", layout="wide")
st.title("💳 Fraud Detection in Financial Transactions")

# Load saved model
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")  # Ensure model.pkl is in the same folder

model = load_model()

# Upload CSV
uploaded_file = st.file_uploader("📁 Upload your transaction CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📋 Uploaded Data Preview")
    st.dataframe(df.head(10), use_container_width=True)

    # 🔍 Required columns for model
    required_cols = ['type']  # Add more columns if model expects them
    missing_cols = [col for col in required_cols if col not in df.columns]

    if missing_cols:
        st.error(f"❌ Missing required column(s): {missing_cols}")
        st.stop()

    # 🎯 Prepare features
    drop_cols = ['nameOrig', 'nameDest', 'isFraud']  # Drop text/id/target
    X = df.drop(columns=drop_cols, errors='ignore')

    # 💡 Don't convert to numeric only — keep 'type' as is for pipeline
    try:
        y_pred = model.predict(X)
        y_prob = model.predict_proba(X)[:, 1]
    except Exception as e:
        st.error(f"🚫 Model prediction failed: {e}")
        st.stop()

    # ➕ Add predictions
    df['Predicted_Fraud'] = y_pred
    df['Risk_Score'] = (y_prob * 100).round(2)

    # ⚠️ Show fraud results
    st.subheader("🚨 Predicted Fraudulent Transactions")
    st.dataframe(df[df['Predicted_Fraud'] == 1], use_container_width=True)

    # 📊 Summary
    st.subheader("📊 Summary")
    total_txns = len(df)
    total_frauds = df['Predicted_Fraud'].sum()
    st.write(f"**Total Transactions:** {total_txns}")
    st.write(f"**Predicted Fraud:** {total_frauds}")
    st.write(f"**Fraud %:** {round((total_frauds/total_txns)*100, 2)}%")



    # ⬇️ Download results
    st.subheader("📥 Download Annotated Results")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", data=csv, file_name="fraud_results.csv", mime='text/csv')
