import pandas as pd
df=pd.read_excel(r"C:\Users\Lenovo\Downloads\NFHS_5_Factsheets_Data.xls")

columns_to_retain = {
    'States/UTs': 'State',
    'Area': 'Area',  
    
    # Obesity Columns
    'Women (age 15-49 years) who are overweight or obese (BMI ≥25.0 kg/m2)21 (%)': 'Obesity_Women',
    'Men (age 15-49 years) who are overweight or obese (BMI ≥25.0 kg/m2) (%)': 'Obesity_Men',
    
    # Anaemia Columns
    'Children age 6-59 months who are anaemic (<11.0 g/dl)22 (%)': 'Anaemia_Children',
    'All women age 15-49 years who are anaemic22 (%)': 'Anaemia_Women',
    
    # High Blood Sugar Columns
    'Women age 15 years and above wih high or very high (>140 mg/dl) Blood sugar level or taking medicine to control blood sugar level23 (%)': 'High_Blood_Sugar_Women',
    'Men age 15 years and above wih high or very high (>140 mg/dl) Blood sugar level  or taking medicine to control blood sugar level23 (%)': 'High_Blood_Sugar_Men',
    
    # Hypertension Columns
    'Women age 15 years and above wih Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)': 'Hypertension_Women',
    'Men age 15 years and above wih Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)': 'Hypertension_Men'
}

filtered_df = df[list(columns_to_retain.keys())].rename(columns=columns_to_retain)


cleaned_df = filtered_df.copy()

numeric_columns = [col for col in cleaned_df.columns if col not in ['State', 'Area']]

for col in numeric_columns:
    cleaned_df[col] = pd.to_numeric(cleaned_df[col], errors='coerce')


print(cleaned_df.dtypes)

print(cleaned_df.head())

cleaned_df['Gender_Obesity_Gap'] = cleaned_df['Obesity_Women'] - cleaned_df['Obesity_Men']

print(cleaned_df[['State', 'Obesity_Women', 'Obesity_Men', 'Gender_Obesity_Gap']].head())