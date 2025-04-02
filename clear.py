import pandas as pd

# Загрузка данных
df = pd.read_csv('gameandgrade.csv')

# Функция для очистки строки с процентом
def clean_percentage(value):
    # Удаляем все нецифровые символы, кроме точек
    cleaned = ''.join(filter(lambda x: x.isdigit() or x == '.', str(value)))
    # Заменяем множественные точки на одну
    if cleaned.count('.') > 1:
        cleaned = cleaned.replace('.', '', cleaned.count('.') - 1)
    # Если строка пустая, вернем NaN
    return float(cleaned) / 100 if cleaned else None

# Применяем функцию к столбцу
df['percentage'] = df['percentage'].apply(clean_percentage)

print("Результат:")
print(df['percentage'].head())
