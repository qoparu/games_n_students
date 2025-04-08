import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Подготовка данных
df = load_data()
X = df[['Playing Hours', 'Parent Revenue', 'Grade']]

# Масштабирование
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Кластеризация (3 кластера)
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Визуализация
plt.figure(figsize=(10, 6))
plt.scatter(df['Playing Hours'], df['Grade'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Playing Hours')
plt.ylabel('Grade')
plt.title('Кластеры учеников')
plt.show()

# Анализ кластеров
cluster_stats = df.groupby('Cluster').mean()
print(cluster_stats)
