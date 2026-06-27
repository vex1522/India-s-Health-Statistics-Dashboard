

import matplotlib.pyplot as plt
import numpy as np

%matplotlib inline


correlation_cols = ['Anaemia_Children', 'Obesity_Women', 'Obesity_Men']
correlation_matrix = cleaned_df[correlation_cols].corr(method='pearson')

print("--- Task 1: Correlation Matrix ---")
print(correlation_matrix)
print("\n" + "="*50 + "\n")



hypertension_df = cleaned_df.dropna(subset=['Hypertension_Women', 'Hypertension_Men']).copy()


hypertension_df = hypertension_df[hypertension_df['Area'] == 'Total']

hypertension_df['Combined_Avg'] = (hypertension_df['Hypertension_Women'] + hypertension_df['Hypertension_Men']) / 2
top_10_hypertension = hypertension_df.nlargest(10, 'Combined_Avg')

x_indices = np.arange(len(top_10_hypertension))
bar_width = 0.35

plt.figure(figsize=(12, 6))
plt.bar(x_indices - bar_width/2, top_10_hypertension['Hypertension_Women'], bar_width, label='Women', color='#ff7f0e', alpha=0.85)
plt.bar(x_indices + bar_width/2, top_10_hypertension['Hypertension_Men'], bar_width, label='Men', color='#1f77b4', alpha=0.85)

plt.xlabel('States / Union Territories', fontsize=12, fontweight='bold')
plt.ylabel('Hypertension Prevalence (%)', fontsize=12, fontweight='bold')
plt.title('Top 10 States with the Highest Rates of Hypertension (Men vs Women)', fontsize=14, fontweight='bold', pad=15)
plt.xticks(x_indices, top_10_hypertension['State'], rotation=45, ha='right', fontsize=10)
plt.legend(title='Gender', fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('task2_hypertension_bar_chart.png', dpi=300)
plt.show()

scatter_data = cleaned_df.dropna(subset=['Anaemia_Women', 'Obesity_Women']).copy()

def generate_abbreviation(state_name):
    words = str(state_name).replace('&', '').replace('and', '').split()
    if len(words) >= 2:
        return "".join([w[0] for w in words[:3]]).upper()
    return str(state_name)[:3].upper()

scatter_data['Abbr'] = scatter_data['State'].apply(generate_abbreviation)

plt.figure(figsize=(11, 8))
plt.scatter(scatter_data['Anaemia_Women'], scatter_data['Obesity_Women'], 
            color='#9467bd', alpha=0.8, edgecolors='black', s=120, label='States')

for idx, row in scatter_data.iterrows():
    plt.annotate(
        row['Abbr'], 
        (row['Anaemia_Women'], row['Obesity_Women']),
        textcoords="offset points", 
        xytext=(0, 7), 
        ha='center', 
        fontsize=9, 
        fontweight='bold',
        color='#333333'
    )

plt.xlabel('Percentage of Anaemic Women (%)', fontsize=12, fontweight='bold')
plt.ylabel('Percentage of Obese Women (%)', fontsize=12, fontweight='bold')
plt.title('Regional Health Clusters: Anaemia vs. Obesity in Women', fontsize=14, fontweight='bold', pad=15)
plt.grid(True, linestyle='--', alpha=0.5)

plt.axvline(scatter_data['Anaemia_Women'].median(), color='gray', linestyle=':', alpha=0.7)
plt.axhline(scatter_data['Obesity_Women'].median(), color='gray', linestyle=':', alpha=0.7)

plt.tight_layout()
plt.savefig('task3_anaemia_vs_obesity_scatter.png', dpi=300)
plt.show()