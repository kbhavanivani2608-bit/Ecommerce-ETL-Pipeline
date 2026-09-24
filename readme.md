# E-commerce Sales ETL Pipeline

## 📌 Project Overview

This project implements an ETL (Extract, Transform, Load) pipeline for e-commerce sales data.

The pipeline reads raw sales data from a CSV file, removes duplicate records using Python and Pandas, and loads the cleaned data into a MySQL database.

It also uses SQL queries to analyze sales by category, product, customer, and date.

## 🔄 ETL Process

CSV Dataset
    ↓
Extract
    ↓
Python + Pandas
    ↓
Transform
(Remove Duplicate Records)
    ↓
Load
    ↓
MySQL Database
    ↓
SQL Analysis

## 🛠️ Technologies Used

- Python
- Pandas
- MySQL
- SQL
- mysql-connector-python
- python-dotenv
- Git
- GitHub
- VS Code

## 📂 Project Structure

```text
Ecommerce-ETL-Pipeline/
│
├── data/
│   └── orders.csv
│
├── etl/
│   └── etl_pipeline.py
│
├── .gitignore
└── README.md