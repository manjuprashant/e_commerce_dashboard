# 🛒 E-Commerce Dashboard – Power BI

## 📌 Project Overview

This project is an **E-Commerce Sales and Performance Dashboard** developed using **Microsoft Power BI**.

The dashboard analyzes sales, revenue, profit, orders, customers, products, and purchasing trends. It includes interactive slicers and drill-through pages that allow users to explore product-level and customer-level performance.

This project was developed as **Task–4: E-Commerce Dashboard**.

---

## 🎯 Project Objectives

The main objectives of this project are:

* Load and prepare ecommerce order and product data
* Create revenue and profit measures
* Calculate return rate where return data is available
* Analyze monthly sales trends
* Identify top-performing products
* Analyze customer distribution
* Track profit trends
* Add interactive slicers
* Create product drill-through analysis
* Create customer drill-through analysis
* Publish the Power BI report

---

## 📂 Dataset

The project uses the **Superstore Retail Analytics** dataset.

### Dataset Source

[Superstore Retail Analytics – GitHub](https://github.com/virajbhutada/bi-projects-collection/tree/main/Superstore%20Retail%20Analytics)

The cleaned dataset used in the Power BI report is:

```text
cleaned_ecommerce
```

### Main Data Fields

The dataset contains information related to:

* Orders
* Customers
* Products
* Categories
* Regions
* Sales
* Quantity
* Profit
* Dates

> **Note:** Some fields from the original dataset may have been renamed or removed during the cleaning process. The Power BI report uses the fields available in the cleaned `cleaned_ecommerce` dataset.

---

# 🧹 Data Preparation

The dataset was prepared using **Power Query in Power BI**.

The main data preparation steps included:

* Removing unnecessary columns
* Checking missing values
* Checking duplicate records
* Correcting data types
* Formatting date columns
* Preparing sales and profit fields
* Preparing customer and product fields
* Creating the final `cleaned_ecommerce` table

---

# 🗓️ Date Table

A separate Date table was created to support time-based analysis.

The Date table contains:

* Date
* Year
* Month
* Month Number
* Year Month
* Year Month Number

The Date table is related to the ecommerce data using the order date.

```text
DateTable[Date]
       │
       │ 1 : *
       ▼
cleaned_ecommerce[Order Date]
```

The `Year Month` field is used for monthly sales and profit trend charts.

---

# 📊 DAX Measures

The following measures were created for the dashboard.

### Total Revenue

```DAX
Total Revenue =
SUM(cleaned_ecommerce[Sales])
```

### Total Profit

```DAX
Total Profit =
SUM(cleaned_ecommerce[Profit])
```

### Total Quantity

```DAX
Total Quantity =
SUM(cleaned_ecommerce[Quantity])
```

### Total Orders

The order-count calculation uses the available order identifier in the cleaned dataset.

```DAX
Total Orders =
DISTINCTCOUNT(cleaned_ecommerce[Order ID])
```

### Total Customers

```DAX
Total Customers =
DISTINCTCOUNT(cleaned_ecommerce[Customer ID])
```

### Profit Margin

```DAX
Profit Margin =
DIVIDE(
    [Total Profit],
    [Total Revenue],
    0
)
```

### Return Rate

If return information is available in the cleaned dataset:

```DAX
Returned Orders =
CALCULATE(
    DISTINCTCOUNT(cleaned_ecommerce[Order ID]),
    cleaned_ecommerce[Returns] = "Yes"
)
```

```DAX
Return Rate =
DIVIDE(
    [Returned Orders],
    [Total Orders],
    0
)
```

---

# 📈 Dashboard Pages

The report contains **3 main Power BI pages**.

## 1️⃣ E-Commerce Dashboard

The main dashboard provides an overall view of ecommerce performance.

### KPI Cards

* 💰 Total Revenue
* 📈 Total Profit
* 📦 Total Orders
* 👥 Total Customers
* 🔄 Return Rate

### Visualizations

* Monthly Sales Trend
* Top 10 Products
* Customer Distribution
* Profit Trend

### Interactive Slicers

* Year
* Region
* Category
* Segment

---

## 2️⃣ Product Details

The Product Details page is a **drill-through page**.

Users can right-click a product from the main dashboard and select:

```text
Drill through → Product Details
```

### Information displayed

* Product Revenue
* Product Profit
* Product Orders
* Product Quantity
* Product Sales Trend
* Order Details

### Order Details

The table is designed to display fields such as:

| Order ID          | Date | Customer | Sales | Quantity | Profit | Returns       |
| ----------------- | ---- | -------- | ----: | -------: | -----: | ------------- |
| Order information | Date | Customer | Sales |      Qty | Profit | Return status |

Return information is displayed only when available in the cleaned dataset.

---

## 3️⃣ Customer Details

The Customer Details page is another **drill-through page**.

Users can select a customer and drill through to view detailed customer performance.

### Information displayed

* Customer Revenue
* Customer Profit
* Customer Orders
* Customer Quantity
* Customer Sales Trend
* Purchase Details

### Purchase Details

The table contains fields such as:

| Product             | Category | Sales | Quantity | Profit | Returns       |
| ------------------- | -------- | ----: | -------: | -----: | ------------- |
| Product information | Category | Sales |      Qty | Profit | Return status |

---

# 🎛️ Interactive Features

The dashboard includes interactive slicers for:

```text
Year
Region
Category
Segment
```

Selecting a slicer dynamically updates the dashboard visuals and KPI cards.

The report also includes:

* Product drill-through
* Customer drill-through
* Back buttons
* Interactive charts
* Dynamic filtering

---

# 📊 Main Dashboard Layout

The main dashboard contains:

```text
┌──────────────────────────────────────────────────────────────┐
│                 E-COMMERCE DASHBOARD                         │
├──────────┬──────────┬──────────┬──────────┬─────────────────┤
│ Revenue  │  Profit  │  Orders  │ Customers│  Return Rate    │
├──────────┴──────────┴──────────┴──────────┴─────────────────┤
│                                                              │
│                  MONTHLY SALES TREND                         │
│                                                              │
├──────────────────────────────┬───────────────────────────────┤
│       TOP 10 PRODUCTS        │   CUSTOMER DISTRIBUTION      │
│                              │                               │
├──────────────────────────────┴───────────────────────────────┤
│                       PROFIT TREND                            │
├──────────────────────────────────────────────────────────────┤
│ Year │ Region │ Category │ Segment                           │
└──────────────────────────────────────────────────────────────┘
```

---

# 🔍 Key Business Insights

The dashboard can be used to identify:

* Overall revenue performance
* Overall profitability
* Monthly sales changes
* Top revenue-generating products
* Customer segment distribution
* Profit trends over time
* Product-level performance
* Customer-level purchasing behavior
* Return performance where return data is available
* Regional and category performance

---

# 🛠️ Tools & Technologies

| Tool               | Purpose                             |
| ------------------ | ----------------------------------- |
| Microsoft Power BI | Dashboard development               |
| Power Query        | Data cleaning and transformation    |
| DAX                | Measures and calculations           |
| GitHub             | Project version control and sharing |
| CSV                | Cleaned dataset                     |

---

# 📁 Repository Structure

```text
E-commerce-Dashboard/
│
├── README.md
│
├── Dataset/
│   └── cleaned_ecommerce.csv
│
├── PowerBI/
│   └── Ecommerce_Dashboard.pbix
│
├── Screenshots/
│   ├── 01_Main_Dashboard.png
│   ├── 02_Product_Details.png
│   ├── 03_Customer_Details.png
│   ├── 04_Data_Model.png
│   └── 05_Published_Report.png
│
└── Documentation/
    └── Project_Report.pdf
```

---

# 📸 Dashboard Screenshots

## Main Dashboard

Add your screenshot here:

```text
Screenshots/01_Main_Dashboard.png
```

## Product Details

Add your screenshot here:

```text
Screenshots/02_Product_Details.png
```

## Customer Details

Add your screenshot here:

```text
Screenshots/03_Customer_Details.png
```

## Data Model

Add your screenshot here:

```text
Screenshots/04_Data_Model.png
```

## Published Report

Add your screenshot here:

```text
Screenshots/05_Published_Report.png
```

---

# 🚀 How to Use

### Step 1 – Download the repository

Clone or download this GitHub repository.

### Step 2 – Open the Power BI file

Open:

```text
PowerBI/Ecommerce_Dashboard.pbix
```

using Microsoft Power BI Desktop.

### Step 3 – Check the data source

Make sure the `cleaned_ecommerce` dataset is available and the data source path is correct.

### Step 4 – Explore the dashboard

Use the slicers to filter the report by:

* Year
* Region
* Category
* Segment

### Step 5 – Use Drill-through

Right-click a product or customer and select the appropriate drill-through page.

---

# ☁️ Power BI Publishing

The completed report was published to **Power BI Service**.

The published report can be shared using an appropriate Power BI workspace or report link, depending on access permissions.

### Power BI Report Link

Add your published report link here:

```text
[View Power BI Report](PASTE_YOUR_POWER_BI_LINK_HERE)
```

---

# 📦 Project Deliverables

The final project contains:

* [x] Cleaned ecommerce dataset
* [x] Power BI `.pbix` file
* [x] Main E-commerce Dashboard
* [x] Product Details drill-through page
* [x] Customer Details drill-through page
* [x] Revenue measures
* [x] Profit measures
* [x] Return rate where return data is available
* [x] Monthly sales chart
* [x] Top product visualization
* [x] Customer distribution
* [x] Profit trend
* [x] Interactive slicers
* [x] Drill-through functionality
* [x] Published Power BI report
* [x] Project documentation

---

# 📝 Conclusion

The E-Commerce Dashboard provides an interactive solution for analyzing ecommerce sales and profitability using Power BI.

The project demonstrates practical skills in:

* Data cleaning
* Data transformation
* Data modeling
* DAX
* KPI creation
* Data visualization
* Interactive dashboard design
* Drill-through analysis
* Power BI publishing

The final dashboard enables users to move from high-level business performance to detailed product and customer analysis in an interactive and user-friendly manner.

---

## 👤 Author

**Your Name**

### Project

**Task–4: E-Commerce Dashboard**

### Technology

**Microsoft Power BI**

---

## 📄 License

This project is created for educational and portfolio purposes.

The dataset remains subject to the terms and conditions of its original source.
