# Bigdata-Hadoop-Spark
# bigdata-hadoop-spark

This repository contains two MapReduce solutions built using Python for Hadoop Streaming. Each problem demonstrates the use of the MapReduce programming model to solve real-world data analysis tasks involving e-commerce and web server logs.

---

## 📁 Folder Structure

hadoop/
├── conversion-rate/
│   ├── mapper.py
│   └── reducer.py
└── weblog-analytics/
    ├── mapper.py
    └── reducer.py

---

## 📦 Problem 1: Conversion Rate Calculation (Folder: `conversion-rate/`)

### 📝 Problem Description
You are analyzing e-commerce logs from the "E-Shop" website to calculate the **conversion rate** of each item. The logs contain user actions such as `view`, `add_to_cart`, and `purchase`. The conversion rate is defined as:


