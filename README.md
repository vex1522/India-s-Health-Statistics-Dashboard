An interactive Python data analytics pipeline using the National Family Health Survey (NFHS-5) dataset to investigate regional health imbalances and demographic disparities across India.

The project evaluates chronic health risks, tests the "double burden of malnutrition" (coexistence of anaemia and obesity), and visualizes major public health risk zones through interactive GIS mapping.

🚀 Key Features
Data Sanitization & Engineering: Ingests raw NFHS binary Excel sheets (.xls), resolves structural data issues (coercing placeholder hyphens - to numeric floats), separates segmented survey demographics (Urban/Rural/Total), and engineers target variables like the Gender Obesity Gap.

Statistical Insights: Evaluates Pearson product-moment correlation coefficients to test health hypotheses across varying demographic splits.

Exploratory Visualizations: Builds static, grouped bar charts comparing unique state-level cardiovascular risks and generates annotated scatter plots mapping overlapping multi-morbidity clusters.

Interactive GIS Dashboard: Integrates public state boundary GeoJSON data with Folium to plot responsive choropleths combined with custom, dynamic HTML summary popups anchored at state capitals.

📁 Project Directory Structure
Plaintext
├── data/
│   └── NFHS_5_Factsheets_Data.xls          # Raw National Family Health Survey spreadsheet
├── notebooks/
│   └── public_health_analysis.ipynb        # Data preparation, EDA, and map compilation pipeline
├── outputs/
│   ├── task2_hypertension_bar_chart.png    # Top 10 states grouped hypertension bar chart
│   ├── task3_anaemia_vs_obesity_scatter.png # Regional multi-morbidity scatter plot
│   └── india_public_health_dashboard.html  # Standalone interactive map dashboard file
├── README.md
└── requirements.txt                        # Dependency registry
🔧 Installation & Usage
1. Clone the Repository & Install Dependencies
Ensure you have Python installed, then run:

Bash
git clone https://github.com/YOUR_USERNAME/NFHS5-Public-Health-Analytics.git
cd NFHS5-Public-Health-Analytics
pip install pandas matplotlib folium requests xlrd
2. Execute the Analytics Workflow
Place the raw NFHS_5_Factsheets_Data.xls sheet in the data/ directory.

Open and run the primary notebook cells to clean data, run statistical tests, and output diagnostic plots:

Bash
jupyter notebook notebooks/public_health_analysis.ipynb
To view the final interactive spatial layer dashboard, open the generated outputs/india_public_health_dashboard.html file directly inside any web browser.

📊 Sample Visual Analytics
Note: Replace the placeholder asset paths below with your saved output images once your updated script runs.

Grouped Demographics Risk Analysis
Visualizes unique, aggregated regional variations while filtering out structural row repetitions.

Health Multi-Morbidity Quadrants
Maps out regional clustering trends, leveraging clean state abbreviations to reduce visual text overlap.
