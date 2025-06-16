Sleep Quality Predictor

A Flask-based web application that predicts a person's sleep quality score based on their lifestyle data using a machine learning regression model.

🚀 Features
- Upload lifestyle data via CSV file
- Predicts sleep quality score (0–10 scale)
- Styled frontend using HTML and CSS
- Built with Python, Flask, and scikit-learn

🛠️ Tech Stack
- Python
- Flask
- Scikit-learn
- XGBoost
- HTML + CSS

📂 Project Structure
sleep-quality-predictor/
├── app.py
├── sleep\_model.pkl
├── sample\_input\_23\_columns.csv
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md

📦 Setup Instructions
1. Clone the repo:
   
   git clone https://github.com/satvika1609/sleep-quality-predictor.git
   cd sleep-quality-predictor

2. Install dependencies:

   pip install -r requirements.txt

3. Run the app:

   python app.py
   
4. Open in browser:

   http://localhost:5000
