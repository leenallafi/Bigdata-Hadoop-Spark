# BigData-Hadoop-Spark


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


---

## 📦 Problem 1: Conversion Rate Calculation (Folder: `conversion-rate`)

### 📝 Problem Description
You are analyzing e-commerce logs from the "E-Shop" website to calculate the **conversion rate** of each item. The logs contain user actions such as `view`, `add_to_cart`, and `purchase`. The conversion rate is defined as:


conversion_rate(item) = number_of_purchases / number_of_views

Some items may be purchased without being viewed, and vice versa.

### 📂 Files
- `mapper.py`: Extracts item actions and emits `(item, action)` pairs.
- `reducer.py`: Aggregates actions for each item and calculates the conversion rate.

### ✅ Real-world Validation
Imagine also that you received confidential information from a warehouse employee suggesting 
that the item “TypeC_HDMI” is still available in abundance.

---

## 📦 Problem 2: Web Server Log Analysis (Folder: `weblog-analytics/`)

### 📝 Problem Description
Given a web server log file (`wserv_up.txt`), your task is to find how many times each web page was visited. Each line in the log represents a visit, with the page path formatted as `/file_X.html`.

### 📂 Files
- `mapper.py`: Extracts file paths from the log.
- `reducer.py`: Aggregates the number of visits for each page.

### ✅ Real-world Insight
It is rumored that `file_8.html` is useless to visitors, and thus expected to have **very low visit counts**, helping verify your results.

---




### 📝 Problem Description
You are analyzing e-commerce logs from the "E-Shop" website to calculate the **conversion rate** of each item. The logs contain user actions such as `view`, `add_to_cart`, and `purchase`. The conversion rate is defined as:


