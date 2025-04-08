import pandas as pd
from sklearn.model_selection import train_test_split

# 1. Загрузка и очистка данных
def load_and_clean_data():
    df = pd.read_csv('gameandgrade.csv')
    
    # Очистка столбца percentage (как в clear.py)
    def clean_percentage(value):
        cleaned = ''.join(filter(lambda x: x.isdigit() or x == '.', str(value)))
        if cleaned.count('.') > 1:
            cleaned = cleaned.replace('.', '', cleaned.count('.') - 1)
        return float(cleaned) / 100 if cleaned else None
    
    df['percentage'] = df['percentage'].apply(clean_percentage)
    return df

# 2. Разделение данных
def split_data(df):
    # Выбираем признаки (X) и целевую переменную (y)
    # Пример: предсказываем оценку (Grade) на основе игровых привычек и других параметров
    X = df[['Playing Hours', 'Parent Revenue', 'Father Education', 'Mother Education']]
    y = df['Grade']
    
    # Разделяем данные на обучающую (80%) и тестовую (20%) выборки
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, 
        test_size=0.2, 
        random_state=42  # для воспроизводимости
    )
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    df = load_and_clean_data()
    X_train, X_test, y_train, y_test = split_data(df)
    
    # Проверка размеров выборок
    print(f"Обучающая выборка: {X_train.shape}")
    print(f"Тестовая выборка: {X_test.shape}")
