# 📧 GRU-Based Spam Message Detector

A deep learning-based web application that classifies text messages as **Spam** or **Not Spam (Ham)** using a **Gated Recurrent Unit (GRU)** neural network.

The project provides a simple Flask web interface where users can enter a message and receive an instant spam classification.

---

## 🚀 Features

* 📩 Classifies messages as **Spam** or **Not Spam**
* 🧠 Uses a **GRU (Gated Recurrent Unit)** deep learning model
* 🔤 Uses a trained tokenizer for text preprocessing
* 🌐 Flask-based web application
* ⚡ Fast real-time prediction
* 💻 Simple and user-friendly interface
* 📦 Easy to install and run locally

---

## 🛠️ Technologies Used

| Technology         | Purpose                   |
| ------------------ | ------------------------- |
| Python             | Core programming language |
| TensorFlow / Keras | Deep learning model       |
| GRU                | Text classification       |
| Flask              | Web application framework |
| HTML / CSS         | Frontend interface        |
| Pickle             | Tokenizer serialization   |

---

## 🧠 Model Architecture

The project uses a **GRU-based neural network** for text classification.

### Workflow

```text
User Message
     ↓
Text Preprocessing
     ↓
Tokenization
     ↓
Sequence Processing
     ↓
GRU Neural Network
     ↓
Prediction
     ↓
Spam / Not Spam
```

GRU is a type of recurrent neural network (RNN) designed to process sequential data such as text. It can capture important information from previous words while using fewer parameters than some traditional recurrent architectures.

---

## 📂 Project Structure

```text
GRU-Spam-Detector/
│
├── app.py
├── GRU_Spam_Detector.h5
├── GRU_Tokenizer.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── .gitignore
└── README.md
```

### File Description

* `app.py` — Flask application and prediction logic
* `GRU_Spam_Detector.h5` — Trained GRU deep learning model
* `GRU_Tokenizer.pkl` — Saved tokenizer used for text preprocessing
* `requirements.txt` — Required Python libraries
* `templates/index.html` — Web interface
* `.gitignore` — Files excluded from Git tracking

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/siddhikurhade/GRU-Spam-Detector.git
```

### 2. Navigate to the project directory

```bash
cd GRU-Spam-Detector
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

### Windows

```powershell
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

The application will start on:

```text
http://127.0.0.1:5000
```

Open the URL in your web browser.

---

## 💡 Example

### Input

```text
Congratulations! You have won a free prize. Click here to claim it.
```

### Output

```text
🚨 Spam
```

Another example:

### Input

```text
Hey, are we meeting at 5 PM today?
```

### Output

```text
✅ Not Spam
```

---

## 🎯 Objective

The primary objective of this project is to develop an automated spam detection system capable of identifying unwanted or potentially harmful messages using deep learning and natural language processing techniques.

---

## 🔮 Future Scope

Future improvements could include:

* 📱 Mobile application integration
* 📊 Prediction confidence score
* 🧹 Advanced NLP preprocessing
* 🌍 Multilingual spam detection
* 📈 Model performance dashboard
* 🔄 Continuous model retraining
* ☁️ Cloud deployment
* 🔐 Detection of phishing and malicious messages

---

## 👨‍💻 Author

**Siddhi Kurhade**

B.Tech – Artificial Intelligence & Machine Learning

Dr. D. Y. Patil College of Engineering & Technology, Kolhapur

---

## ⭐ Project Highlights

**Domain:** Deep Learning / Natural Language Processing

**Model:** GRU (Gated Recurrent Unit)

**Framework:** Flask + TensorFlow/Keras

**Task:** Binary Text Classification

**Output:** Spam / Not Spam

---

## 📜 License

This project is developed for educational and academic purposes.
