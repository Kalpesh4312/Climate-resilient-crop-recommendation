# 🌿 Climate-Resilient Crop Recommendation System  

## 📌 Project Overview  
Climate change has made traditional farming practices less sustainable. This project uses **Machine Learning** to recommend the **most suitable crop** for a region based on soil and climate conditions.  

The system predicts crops using features such as:  
- 🌡️ Temperature (°C)  
- 💧 Humidity (%)  
- 🌧️ Rainfall (mm)  
- 🧪 Soil pH  
- 🪨 Nitrogen (N), Phosphorus (P), Potassium (K) levels  

It is deployed as a **Flask web app**, where farmers can input environmental parameters and get **crop recommendations** instantly.  

---

## ⚙️ Tech Stack  
- **Python 3.10+**  
- **Flask** (for web app deployment)  
- **scikit-learn** (ML models)  
- **joblib** (model persistence)  
- **HTML, CSS** (frontend)  

---

## 🚀 Features  
✅ Crop recommendation based on **7 soil & climate features**  
✅ Supports **multiple ML models** (Decision Tree, Random Forest, KNN, Neural Network)  
✅ **Validation checks** (no negative inputs, valid numeric values)  
✅ Easy to deploy locally using Flask  
✅ Ready for cloud deployment (Heroku / Render / Railway)  

---

## 📂 Project Structure  
<img width="473" height="230" alt="image" src="https://github.com/user-attachments/assets/2602c450-7665-4939-a5ea-eb927e0a7436" />
<img width="528" height="108" alt="image" src="https://github.com/user-attachments/assets/b0e5dd84-15d2-4962-be1b-f17eceff5e2b" />


---

## 🛠️ Setup Instructions  

### 1. Clone Repository
```bash
git clone https://github.com/your-username/crop_recommendation_flask.git
cd crop_recommendation_flask

## Create Virtual Enviroment(Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux

## Install Dependencies
pip install -r requirements.txt

## Run flask App
python app.py

## Open in Browser

Go to: 👉 http://127.0.0.1:5000/

🎯 Example Usage

Enter climate & soil values:

Temperature: 26°C

Humidity: 80%

Rainfall: 200 mm

pH: 6.5

N: 90, P: 42, K: 43

Click Predict

System suggests:

🌱 Recommended Crop: Rice

📊 Machine Learning Models

We trained and tested multiple ML algorithms:

🌳 Decision Tree (simple, interpretable)

🌲 Random Forest (high accuracy, robust)

👥 KNN (uses similarity-based prediction)

🤖 Neural Network (captures complex patterns)

The best-performing model (based on accuracy & precision) is deployed.

🛡️ Input Validation

✅ Valid ranges ensured (e.g., pH between 0–14, humidity 0–100)

🌍 Future Scope

Integrate real-time weather APIs

Use satellite data (FAO/NASA) for climate resilience

Deploy as a mobile app for farmers

Add multi-language support for wider accessibility

👨‍💻 Author

Kalpesh Kishor Patil

Internship Project under AICTE


---

👉 Save this as **`README.md`** in your GitHub project root folder.  

Would you also like me to generate a **`requirements.txt`** file (with exact versions of Flask, sklearn, pandas, numpy, joblib) so your GitHub repo is plug-and-play?
