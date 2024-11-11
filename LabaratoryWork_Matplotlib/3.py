import pandas as pd
import matplotlib.pyplot as plt

file_path = 'students.csv'  


df = pd.read_csv(file_path, delimiter=';', header=None, names=['Преподаватель', 'Группа', 'Оценка'])

df['Оценка'] = df['Оценка'].astype(int)



plt.figure(figsize=(8, 6))
df.groupby(['Преподаватель', 'Оценка']).size().unstack().plot(kind='bar', stacked=True)
plt.title('Распределение оценок по преподавателям')
plt.xlabel('Преподаватель')
plt.ylabel('Количество студентов')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
df.groupby(['Группа', 'Оценка']).size().unstack().plot(kind='bar', stacked=True)
plt.title('Распределение оценок по группам')
plt.xlabel('Группа')
plt.ylabel('Количество студентов')
plt.tight_layout()
plt.show()

