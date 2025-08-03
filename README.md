Fraud Detection in Financial Transactions
This project is a fraud detection web application built with Streamlit. It uses a pre-trained scikit-learn model (saved as model.pkl) to flag potentially fraudulent financial transactions in user-uploaded CSV files. Users can upload a transaction CSV, preview the data, and the app will predict which transactions are fraudulent. In short, it turns a simple CSV of transactions into an interactive fraud analysis dashboard using an ML model.
Features
•	CSV Upload: Users can upload a transaction CSV file via a browser widget. The app uses Streamlit’s st. file uploader to accept CSV inputs.
•	Data Preview: After uploading, the first few rows of the data are shown with st.dataframe, letting users verify contents.
•	Prediction: The app runs the ML model on the uploaded data to predict fraud for each transaction. Predicted frauds are added as a new column.
•	Download Results: Users can download the annotated results as a new CSV via a Download button. Streamlit’s st.download_button is used to export the DataFrame with predictions.

	Tech Stack
•	Python 3.9+ – Core programming language (officially supports Python 3.9–3.13).
•	Streamlit – For the web interface. Streamlit is an open-source Python app framework for data apps. It makes it easy to build interactive UIs with a few lines of code.
•	scikit-learn – For the machine learning model. Scikit-learn is a popular open-source ML library providing classification algorithms and utilities.
•	pandas & NumPy – Used for data handling and manipulation.
•	joblib – To load/save the trained model (model.pkl). The model is serialized with joblib (e.g. joblib.load('model.pkl')).
•	Other libraries: (e.g.) matplotlib, seaborn (for any charts or reports, if used), etc.
In summary, the stack is typical for Python ML apps: Python + Streamlit + pandas + scikit-learn + joblib.





	How to Run the Fraud Detection App 
Follow these steps to run the Streamlit-based fraud detection app locally.
________________________________________
1. Download the Project Folder
Go to the Google Drive link you received.
Download the entire project folder (usually as a ZIP).
Extract/unzip the folder to any location on your machine (e.g., Desktop or Documents).
________________________________________
2. Create a Virtual Environment
Open your terminal (or Anaconda Prompt), navigate to the extracted folder:
cd “path/to/your/project-folder”
________________________________________
4. Run the App
Still inside the project folder, start the Streamlit app
streamlit run app.py
This will open a browser window (or visit http://localhost:8501 manually).
________________________________________
5. Use the App
Upload your transactions CSV file using the upload button. 
The app will show predictions, fraud summaries, and allow you to download the results.






	Folder Structure
A simple structure for this project might look like:
fraud-detection-app/
├── app.py             # Streamlit application source code
├── model.pkl          # Trained scikit-learn model (saved with joblib)
├── IPYNB File         # Python dependencies
├── README.md          # This documentation file
├── Sample data/       # directory to hold example input CSVs
└── results/           # directory for output reports or logs
This separates code from data and outputs, which is a common practice. In the example above, data/ might contain sample transaction files, and results/ could store any analysis exports. The app.py and model.pkl stay in the root for easy access.
Usage
To use the app, open it in your browser (after running as above).
•	Upload a CSV: Click the file uploader widget (“📁 Upload your transaction CSV”) and select a CSV of transactions. Streamlit’s st.file_uploader will accept the file. The app immediately reads it with pd.read_csv(uploaded_file) (as per Streamlit’s examples).
•	Preview Data: Once uploaded, the first few rows of the data are displayed as an interactive table (st.dataframe), so you can confirm the upload.
•	Run Predictions: The app automatically runs the model on the uploaded data. It checks required columns (e.g. 'type' must be present) and drops unused columns (nameOrig, nameDest, isFraud) before prediction. It then adds two new columns: Predicted_Fraud (0 or 1) and Risk_Score (fraud probability).
•	Summary Statistics: A summary section displays total transactions, total predicted frauds, and fraud percentage. These summary metrics update based on the uploaded data.
•	Download Results: Finally, click the “Download CSV” button to save the annotated data. Streamlit’s st.download_button is used to export the DataFrame to a CSV file[6]. This downloaded file will include the original columns plus the Predicted_Fraud and Risk_Score for each row.
Each time you upload a new file or modify the data, the UI will update automatically. This provides a real-time way to explore and understand how the model flags transactions. The process is similar to examples in Streamlit’s documentation, which often show uploading and processing a CSV.


	Requirements
•	Python 3.9 or higher (Streamlit officially supports Python 3.9–3.13).
•	streamlit 
•	pandas, numpy
•	scikit-learn (for the ML model)
•	joblib (for loading the model)
You can install all required packages via:
pip install streamlit pandas numpy scikit-learn joblib
or using the provided requirements.txt (if available).
	Notes
•	model.pkl File: The pre-trained model must be named model.pkl and located in the same folder as app.py. The app loads it with joblib.load("model.pkl"). If this file is missing or corrupt, the app will show an error on startup.
•	Input CSV Format: Your transaction CSV should have the same features used in training. For example, a common fraud dataset includes columns like step, type, amount, nameOrig, oldbalanceOrg, newbalanceOrig, nameDest, oldbalanceDest, newbalanceDest, etc. (Our example uses a PaySim-like dataset.) The code automatically drops nameOrig, nameDest, and any isFraud label before predicting, but it requires the type column (and any numeric features used by the model). If the CSV lacks expected columns, the app will report which ones are missing.
•	Data Consistency: Ensure categorical columns (like type) match what the model was trained on. Also, numeric columns should be of compatible scale/units. If you trained the model on PaySim data (as one example project did), your CSV should follow that schema. Otherwise, retrain the model accordingly.
•	Extending the App: The code can be modified to accept additional columns or to use a different model. Just update the required_cols or drop_cols lists in app.py as needed, and replace model.pkl with your own serialized model.
With these instructions, you should be able to clone the repository, install dependencies, and launch the app locally for testing and development. Enjoy exploring fraud detection with this Streamlit application! 
________________________________________
