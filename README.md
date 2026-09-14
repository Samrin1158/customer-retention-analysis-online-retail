# The Customers Who Disappear: Understanding Customer Loyalty and Churn Risk in Online Retail

## Project Overview

Customer retention is one of the major challenges in online retail. A customer may purchase repeatedly for a period of time and then gradually disappear from the business.

This project investigates customer loyalty, inactivity, potential churn risk, and retention behaviour using the Online Retail transaction dataset.

Rather than looking only at overall sales, the project analyses customers at an individual level using purchase recency, purchase frequency, and historical revenue.

### Key Questions:

1. How many customers have become inactive and how long have they been away?
2. How common are repeat purchases compared with one-time purchases?
3. Are high-value customers also becoming inactive?
4. What does customer cohort behaviour reveal about retention over time?

The final objective is to transform these findings into actionable customer-retention strategies.

---

## Story Hook

### The Customers Who Disappear

At first glance, customer loyalty appears relatively healthy: **72.39% of customers made repeat purchases**.

However, looking deeper reveals a more concerning pattern.

**40.83% of customers had not made a purchase for more than 180 days.**

Among the **1,176 high-value customers**, **208 (17.69%) were identified as at risk** based on prolonged inactivity.

These customers are associated with **£1,546,445.44 in historical revenue**.

The central story of this project is therefore not simply about customer churn. It is about identifying valuable customers before prolonged inactivity becomes permanent.

---

## Dataset

**Dataset:** Online Retail Dataset

The dataset contains transaction-level records from an online retail business.

### Main attributes

- `InvoiceNo` – Transaction/invoice identifier
- `StockCode` – Product identifier
- `Description` – Product description
- `Quantity` – Quantity purchased
- `InvoiceDate` – Date and time of transaction
- `UnitPrice` – Price per unit
- `CustomerID` – Customer identifier
- `Country` – Customer country
- `Revenue` – Transaction revenue derived during preprocessing

The cleaned dataset is stored in:

```text
data/processed/cleaned_retail.csv  
```

## Project Objectives

### The project focuses on:
- Cleaning and preprocessing transaction-level retail data
- Performing exploratory data analysis
- Creating customer-level behavioural metrics
- Measuring customer inactivity
- Identifying repeat and one-time customers
- Identifying high-value customers
- Detecting high-value customers who may be at risk
- Analysing customer retention using cohort analysis
- Developing actionable customer-retention recommendations

## Methodology

The analysis follows an end-to-end data analytics workflow.

### 1. Data Cleaning
The initial dataset was examined and cleaned by handling:
- Missing values
- Duplicate records
- Invalid transaction records
- Data type inconsistencies
- Transaction-level revenue calculation

### 2. Customer-Level Aggregation
Transaction-level data was aggregated to create one record per customer. The following metrics were derived:
- **Recency** – Number of days since the customer's most recent purchase
- **Frequency** – Number of unique orders/invoices
- **Monetary Value** – Total historical revenue generated
- **Total Quantity** – Total quantity purchased

### 3. Customer Segmentation
Customers were classified into:
- One-time customers
- Repeat customers
- High-value customers
- At-risk customers

For this analysis, customers with more than 90 days since their last purchase were classified as at risk. Customers with more than 180 days since their last purchase were treated as highly inactive for the inactivity analysis.

### 4. Cohort Analysis
Customers were grouped according to their first purchase month to investigate retention behaviour over time.

## Key Findings

### 1. A large inactive customer segment exists
- **40.83%** of customers had not made a purchase for more than 180 days.
- This indicates a substantial dormant customer segment requiring further retention analysis.

### 2. Repeat purchasing is common
- **72.39%** of customers made repeat purchases.
- The remaining **27.61%** made only one purchase.
- This suggests that the business has a substantial repeat-customer base, while the one-time segment represents an opportunity for conversion.

### 3. High-value customers are also at risk
There were 1,176 high-value customers in the analysis. Of these:
- **208 customers (17.69%)** were classified as at risk because they had more than 90 days since their last purchase.

### 4. At-risk customers represent substantial historical value
The 208 at-risk high-value customers are associated with:
- **£1,546,445.44** in historical revenue.
- This highlights the importance of prioritizing valuable inactive customers in retention campaigns.

### 5. Retention varies across customer cohorts
- Cohort analysis shows how customer retention changes across the months following the first purchase.
- This provides a more detailed view of customer behaviour than simply counting repeat purchases.

## Visualizations

The project contains four main visualizations.

### 1. Customer Inactivity
- Shows the distribution of customers based on the number of days since their last purchase.

### 2. High-Value Customers: Active vs At Risk
- Compares active and at-risk customers within the high-value segment.

### 3. Customer Value vs. Inactivity
A scatter plot showing the relationship between:
- Days since last purchase
- Historical customer revenue
- Number of orders
- High-value classification

### 4. Customer Retention by First Purchase Cohort
- A cohort heatmap showing customer retention behaviour across different first-purchase cohorts.

## Business Recommendations

### 1. Prioritize high-value at-risk customers
- The 208 high-value at-risk customers should receive priority in retention and win-back campaigns because they have historically generated substantial revenue.

### 2. Introduce personalized win-back campaigns
- Inactive customers can be targeted using their previous purchasing behaviour, product interests, and purchase frequency.

### 3. Encourage one-time customers to make a second purchase
- The **27.61%** one-time customer segment represents an opportunity to encourage repeat purchases through follow-up communication and personalized product recommendations.

### 4. Differentiate retention strategies
- High-value inactive customers should receive higher-priority interventions, while lower-value inactive customers can be managed through automated, lower-cost campaigns.

### 5. Monitor retention using cohort analysis
- Cohort analysis can be used regularly to determine whether newer customer groups are becoming more or less likely to return.

## Limitations

- The dataset does not contain an explicit churn label. Therefore, inactivity is used as an indicator of potential churn rather than confirmed churn.
- The 90-day threshold used to identify at-risk customers is an analytical assumption and may not represent the retailer's actual definition of churn.
- Historical revenue associated with at-risk customers represents past transaction value and should not be interpreted as guaranteed future revenue loss.
- The analysis identifies behavioural patterns and associations but does not establish causation.
- Factors such as promotions, product availability, marketing campaigns, and customer demographics are not available in the dataset and may influence customer behaviour.

## Repository Structure

## Repository Structure

```text
online-retail-customer-story/
│
├── data/
│   └── raw/
│       └── online_retail_II.xlsx
│
├── notebooks/
│   ├── Data Cleaning Notebook
│   ├── 02_eda_visualization.ipynb
│   └── 03_customer_retention_story.ipynb
│
├── src/
│   └── data_cleaning.py
│
visuals/
├── customer_inactivity.png
├── high_value_at_risk.png
├── customer_value_vs_inactivity.png
└── cohort_retention_heatmap.png
│
├── reports/
│   └── online-retail-customer-story.pptx
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Technologies Used
- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git
- GitHub

## Project Workflow

```text
Raw Transaction Data
        ↓
Data Cleaning & Preprocessing
        ↓
Exploratory Data Analysis
        ↓
Customer-Level Aggregation
        ↓
Customer Segmentation
        ↓
Inactivity & Risk Analysis
        ↓
Cohort Retention Analysis
        ↓
Data Storytelling
        ↓
Actionable Recommendations
```

## Group Project & My Contribution

**Group Project | MSc Big Data Analytics | CIA 2**

This project was completed as a group as part of the MSc Big Data Analytics CIA 2 assessment on **Data Storytelling and Exploratory Data Analysis**.

### My Contribution

My primary responsibility was the **customer retention and risk analysis** component of the project.

I worked on:

- Customer-level behavioural analysis
- Customer inactivity and recency analysis
- Repeat vs one-time customer analysis
- High-value customer identification
- High-value at-risk customer analysis
- Cohort retention analysis
- Customer value vs inactivity visualization
- Advanced data visualizations
- Insight generation and interpretation
- Customer-retention recommendations
- Data storytelling and presentation narrative
- Presentation deck development
- Scriptwriting
- Final video production

### Key Analysis Developed

My analysis focused on answering:

> **Which customers are disappearing, and which of those customers are important enough for the business to prioritize?**

The analysis identified:

- **40.83%** of customers inactive for more than 180 days
- **72.39%** repeat customers
- **1,176** high-value customers
- **208** high-value customers classified as at risk
- **17.69%** of high-value customers classified as at risk
- **£1,546,445.44** in historical revenue associated with these high-value at-risk customers

The findings were translated into customer-retention recommendations and presented through a data storytelling approach.
## Project Outcome

This project demonstrates how transaction-level online retail data can be transformed into customer-level insights that support data-driven retention strategies.

**The key message is:**
> Not every inactive customer is equally important. Identifying valuable customers before they disappear can help businesses prioritize their retention efforts.




















