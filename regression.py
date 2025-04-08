import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Загрузка и очистка данных
def load_data():
    df = pd.read_csv('gameandgrade.csv')
   def clean_percentage(value):
        cleaned = ''.join(filter(lambda x: x.isdigit() or x == '.', str(value)))
        if cleaned.count('.') > 1:
            cleaned = cleaned.replace('.', '', cleaned.count('.') - 1)
        return float(cleaned) / 100 if cleaned else None
    
    df['percentage'] = df['percentage'].apply(clean_percentage)
    return df

# prepating the data
df = load_data()
X = df[['Playing Hours', 'Parent Revenue', 'Father Education', 'Mother Education']]
y = df['Grade']

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели
model = LinearRegression()
model.fit(X_train, y_train)

# Прогноз и оценка
y_pred = model.predict(X_test)
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
print(f"R²: {r2_score(y_test, y_pred):.2f}")

# Пример интерпретации коэффициентов
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef:.2f}")
