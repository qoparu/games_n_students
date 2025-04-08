import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Создание категорий для Grade
def create_grade_groups(grade):
    if grade >= 80:
        return 'высокая'
    elif 60 <= grade < 80:
        return 'средняя'
    else:
        return 'низкая'

# Подготовка данных
df = load_data()  # используем функцию из предыдущего шага
df['Grade Group'] = df['Grade'].apply(create_grade_groups)

X = df[['Playing Hours', 'Mother Education']]
y = df['Grade Group']

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

# Обучение модели
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Прогноз и оценка
y_pred = clf.predict(X_test)
print(f"Точность: {accuracy_score(y_test, y_pred):.2f}")

# Важность признаков
for feature, importance in zip(X.columns, clf.feature_importances_):
    print(f"{feature}: {importance:.2f}")
