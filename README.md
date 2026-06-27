📩 SMS Spam Detection System
📌 Project Overview
The SMS Spam Detection System is a Machine Learning-based web application developed using Python, Streamlit, and Natural Language Processing (NLP). The application classifies SMS messages as either Spam or Ham (Safe) and provides prediction probabilities along with model performance metrics.

This project demonstrates how machine learning can be used to automatically detect unwanted messages and improve communication security.

🚀 Features
✅ SMS Classification
Predicts whether a message is Spam or Ham.

✅ Real-Time Prediction
Users can enter a message and receive instant results.

✅ Probability Analysis
Displays Spam and Ham probabilities.

✅ Performance Metrics
Shows Accuracy, Precision, Recall, and F1 Score.

✅ Interactive Pie Chart
Visualizes prediction probabilities.

✅ Prediction History
Stores previous predictions during the session.

✅ CSV File Upload
Allows users to upload CSV files for preview and analysis.

✅ User-Friendly Interface
Built with Streamlit for an interactive experience.

🛠 Technologies Used
Technology	Purpose
Python	Programming Language
Streamlit	Web Application Framework
Pandas	Data Processing
Scikit-Learn	Machine Learning
TF-IDF Vectorizer	Text Feature Extraction
Logistic Regression	Classification Model
Matplotlib	Data Visualization
📊 Dataset Information
The project uses the SMS Spam Collection Dataset.

Dataset Columns
Column	Description
v1	Label (Spam/Ham)
v2	SMS Message
Example:

ham,Hello how are you?
spam,Win ₹5000 now! Click here.
⚙️ Machine Learning Workflow
Step 1: Data Loading
Load SMS dataset using Pandas.

Step 2: Data Cleaning
Convert text to lowercase and remove punctuation.

Step 3: Feature Extraction
Transform text into numerical vectors using TF-IDF Vectorizer.

Step 4: Train-Test Split
Split dataset into training and testing sets.

Step 5: Model Training
Train Logistic Regression classifier.

Step 6: Prediction
Classify user-entered messages as Spam or Ham.

📈 Model Performance Metrics
The application evaluates the model using:

Accuracy
Measures overall correctness.

Precision
Measures how many predicted spam messages are actually spam.

Recall
Measures how many actual spam messages are detected.

F1 Score
Balances Precision and Recall.

▶️ Installation
Step 1: Clone Repository
git clone https://github.com/your-username/sms-spam-detection.git
Step 2: Navigate to Project Folder
cd sms-spam-detection
📊 Example Predictions
Example 1
Input:

Congratulations! You have won ₹10,000. Claim now.
Output:

Spam
Example 2
Input:

Hi, let's meet tomorrow at 5 PM.
Output:

Ham (Safe Message)
📈 Visualization
The application generates a pie chart showing:

Spam Probability
Ham Probability
This helps users understand prediction confidence.

📂 CSV Upload Feature
Users can upload CSV files directly into the application.

Supported Format:

message
Hello friend
Win cash now
Uploaded data is displayed in an interactive table.

🔒 Error Handling
The application handles:

Empty Input Messages
Displays a warning if no message is entered.

Invalid Files
Supports only CSV uploads.

Missing Dataset
Alerts the user if the dataset is unavailable.

🔮 Future Enhancements
Deep Learning Models (LSTM/BERT)
Email Spam Detection
Multiple Language Support
Bulk SMS Classification
Download Prediction Reports
Cloud Deployment
User Authentication
📄 License
This project is created for educational and learning purposes. Users are free to modify and enhance the application for academic, personal, or professional use.



🎥 A Movie Recommendation System built with Python and Streamlit that suggests similar movies based on title similarity. The application uses CountVectorizer and Cosine Similarity to provide quick and interactive movie recommendations.


