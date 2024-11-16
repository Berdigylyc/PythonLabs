import pandas as pd
import matplotlib.pyplot as plt

file_path = 'students_info.xlsx'
df_excel = pd.read_excel(file_path)
html_file_path = 'results_ejudge.html'
df_html = pd.read_html(html_file_path)[0]

df = pd.merge(df_html[['User', 'G', 'H', 'Solved']], df_excel[['login', 'group_faculty', 'group_out']],
               left_on='User', right_on='login', how='left')

df_group_faculty = df.groupby('group_faculty')['Solved'].mean()
df_group_faculty.plot(kind='bar', figsize=(10, 6))
plt.title('The average of solved problems by faculty groups')
plt.xlabel('Faculty groups')
plt.ylabel('Solved problems (average)')
plt.xticks(rotation=90)
plt.savefig('01.png')
plt.show()

df_group_out = df.groupby('group_out')['Solved'].mean()
df_group_out.plot(kind='bar', figsize=(10, 6))
plt.title('The average of solved problems by informatics groups')
plt.xlabel('Informatics groups')
plt.ylabel('Solved problems (average)')
plt.xticks(rotation=90)
plt.savefig('02.png')
plt.show()

df_selected = df[(df['G'] > 20) | (df['H'] > 20)]
result = df_selected[['User','G','H','group_faculty', 'group_out']].drop_duplicates()
print(result)
