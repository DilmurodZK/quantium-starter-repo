# Quantium Starter Repository

## 📌 Project Overview
This project is part of the **Quantium Data Analytics Virtual Internship (Forage)**.  
The goal was to analyze retail transaction data, identify sales uplift in trial stores compared to control stores, and provide actionable business recommendations.

## 📊 Results
- Cleaned and analyzed large transaction datasets
- Built metrics to evaluate trial vs control stores
- Visualized sales uplift and customer behavior using Plotly/Dash
- Delivered insights to support marketing decisions

## 🎯 Skills Demonstrated
- Data cleaning & preprocessing with Pandas
- Exploratory Data Analysis (EDA)
- Business-oriented data storytelling
- Automated testing with Pytest
- CI/CD with GitHub Actions

## ⚙️ Setup Instructions

### 1. Clone the repository
```
git clone https://github.com/DilmurodZK/quantium-starter-repo.git
cd quantium-starter-repo
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🧪 Running Tests

All tests are automated using **pytest**.  
To run them locally:

```bash
./run_tests.sh
```

If all tests pass, you will see:
```
✅ All tests passed!
```

---

## 🚀 Continuous Integration (CI)

This project is configured to work with **GitHub Actions**.  
Every push or pull request will automatically:

1. Set up Python environment  
2. Install dependencies  
3. Run `run_tests.sh`  
4. Report test results  

This ensures code quality and reproducibility.

---

## 📊 Tools & Libraries

- [Dash](https://dash.plotly.com/) – Interactive dashboards  
- [Pandas](https://pandas.pydata.org/) – Data analysis  
- [Plotly](https://plotly.com/python/) – Data visualization  
- [Pytest](https://docs.pytest.org/) – Testing framework  
- [Selenium](https://www.selenium.dev/) – UI testing (with ChromeDriver/GeckoDriver)  

---

## 👨‍💻 Author

**DilmurodZK**  
PhD Candidate & Backend Developer  
Focused on analytics, backend engineering, and CI/CD automation.  

---

## 📜 License

This project is provided as part of the Quantium starter program.  
Feel free to use and adapt for learning purposes.
