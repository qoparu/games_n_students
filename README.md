# 👾 Games and Students 👾

**Project Goal:**  
To explore how gaming habits affect students' academic performance.

---

## Project Steps

**1. Data Cleaning**  
- **Issue:**  
  The `percentage` column contains incorrect values such as `"7750,00%"`. These will be corrected to the proper format, e.g., `77.5%` or `77.50`.

---

**2. Correlation Analysis** 

What we are looking for?

Strong correlations (values close to 1 or -1).

For example, a negative correlation between Playing House and Grade may mean that the more a student plays, the lower the grades.
- **Objective:**  
  Identify relationships between variables, such as how gaming habits influence academic success.
![Correlation Heatmap](correlation_heatmap.png)

If **Playing Hours** and **Grade** have a correlation of **-0.65**, it means that the more time a student spends playing, the *lower* their academic grades tend to be.

If **Mother Education** and **Grade** correlate at **0.8**, this indicates a *strong relationship* between the mother's level of education and the student's academic performance.

---

**3. Data Splitting**  
- **Objective:**  
  Prepare data for machine learning by dividing it into training and testing sets.

---

**4. Model Training**  
- **Method:**  
  Train a model (e.g., linear regression) and assess its accuracy using the coefficient of determination \( R^2 \).

# Predictive Modeling (Regression, Classification, Clustering)

## Goal
Build models to predict student performance and group students based on behavior and demographics.

## Tools
- **Python**
- **scikit-learn**
- **pandas**
- **matplotlib**
- **seaborn**

---

### 1. Regression: Predict Student Grade (`regression.py`)
**Purpose:** Predict numerical grades (Grade) based on gaming habits, parental income, and education levels.  
**Model:** Linear Regression  

#### Key Features:
- Playing Hours  
- Parent Revenue  
- Father Education  
- Mother Education  

#### Insights:
- Negative correlation between Playing Hours and Grade.  
- Parental education and income positively influence grades.  

---

### 2. Classification: Categorize Academic Performance (`classification.py`)
**Purpose:** Classify students into performance groups (High/Medium/Low) based on grades.  
**Model:** Random Forest Classifier  

#### Thresholds:
- **High:** Grade ≥ 80  
- **Medium:** 60 ≤ Grade < 80  
- **Low:** Grade < 60  

---

### 3. Clustering: Identify Student Groups (`clustering.py`)
**Purpose:** Uncover hidden patterns (e.g., "Gamers", "High Achievers") using unsupervised learning.  
**Model:** K-Means Clustering  

#### Features:
- Playing Hours  
- Parent Revenue  
- Grade  

![Results](rcc.png)

---

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your_repository/games_n_students.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the data analysis:
   ```bash
   python analysis.py
   ```

---
