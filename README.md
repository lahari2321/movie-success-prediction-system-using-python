# movie-success-prediction-system-using-python

📘 Movie Success Prediction System
A simple and interactive Streamlit web application that predicts whether a movie will be a HIT or a FLOP based on features like rating, revenue, votes, genres, and more.
🚀 Project Overview
This project uses a pre-trained machine learning model (saved as .sav using Joblib) to predict movie success.
Users can give the movie details in the UI, and the app instantly shows whether the movie is likely to be a Hit or Flop.
🧠 Features
✔ User-friendly Streamlit interface
✔ Movie input fields (rating, runtime, votes, etc.)
✔ Genre selection (Action, Adventure, Comedy)
✔ Loads pre-trained model (movie_success_model.sav)
✔ Displays prediction message clearly (Hit or Flop)

🗂️ Project Structure
📁 movie-success-prediction-system
│── app.py
│── movie_success_model.sav
│── movie_metadata.csv
│── movie_success_rate.csv
│── requirements.txt
│── README.md

🛠️ Technologies Used
Python
Streamlit
NumPy
Joblib
(scikit-learn is NOT included since it’s not used in this app)

📥 Installation & Setup
1. Clone this repository
git clone https://github.com/YOUR_USERNAME/movie-success-prediction-system.git
cd movie-success-prediction-system

2. Install dependencies
pip install -r requirements.txt

3. Run the Streamlit app
streamlit run app.py

🧾 Requirements File
Your requirements.txt should contain:
streamlit
numpy
joblib

🎯 How Prediction Works
The model takes the following inputs:
Year of release
Runtime
IMDB rating
Number of votes
Revenue
Metascore
Action (0/1)
Adventure (0/1)
Comedy (0/1)
These inputs are converted to a NumPy array and passed to the loaded model.

📌 Future Improvements
Add more genres
Add data visualization
Improve model accuracy
Deploy online using Streamlit Cloud

