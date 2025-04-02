import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных
df = pd.read_csv('gameandgrade.csv')

# Предобработка столбца percentage (как в предыдущих шагах)
def clean_percentage(value):
    cleaned = ''.join(filter(lambda x: x.isdigit() or x == '.', str(value)))
    if cleaned.count('.') > 1:
        cleaned = cleaned.replace('.', '', cleaned.count('.') - 1)
    return float(cleaned) / 100 if cleaned else None

df['percentage'] = df['percentage'].apply(clean_percentage)

# Построение тепловой карты
correlation_matrix = df.corr(numeric_only=True)  # numeric_only=True игнорирует нечисловые колонки
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation map')
plt.savefig('correlation_heatmap.png')
plt.show()
