
# BigData-Hadoop-Spark


This repository contains two real-world data analysis problems, solved using both:
- **Hadoop MapReduce (Python + Streaming)**
- **Apache Spark (PySpark)**

These problems simulate tasks a data engineer or analyst may encounter when working with large-scale log files from e-commerce platforms and web servers.

---

## 📁 Folder Structure

\`\`\`plaintext
hadoop/
├── conversion-rate/
│   ├── mapper.py
│   └── reducer.py
└── weblog-analytics/
    ├── mapper.py
    └── reducer.py

spark/
├── conversion_rate_spark.py
└── weblog_analytics_spark.py
\`\`\`

---

## 🧩 Problem 1: E-Commerce Conversion Rate

### 📌 Scenario
An e-commerce company, **E-Shop**, records user activities such as \`view\`, \`add_to_cart\`, and \`purchase\`. The management team wants to know the **conversion rate** for each product — a metric defined as:

\`\`\`
conversion_rate = number_of_purchases / number_of_views
\`\`\`

> 💡 A tip from a warehouse employee suggests that \`TypeC_HDMI\` is overstocked, likely due to a **low conversion rate** — this acts as a real-world validator for your result.

---

## 🧩 Problem 2: Web Server Log Analytics

### 📌 Scenario
You are provided with a server log file (\`wserv_up.txt\`) from a website. Each line represents a user request to a web page such as \`/file_2.html\`, \`/file_8.html\`, etc.

Your task is to:
- Count how many times each file (web page) was visited.
- Identify the most and least visited pages.

> 💡 It\'s rumored that \`file_8.html\` is useless to users and is rarely visited — this provides a useful hint to verify your output.

---

## 🛠️ Hadoop Implementation (Folder: \`hadoop/\`)

This folder uses the **MapReduce programming model**, written in Python and designed for **Hadoop Streaming**.

### 🔹 \`conversion-rate/\`
- \`mapper.py\`: Emits \`(item, action)\` for each log entry.
- \`reducer.py\`: Counts views and purchases, then computes conversion rates per item.

### 🔹 \`weblog-analytics/\`
- \`mapper.py\`: Extracts the web page (e.g., \`/file_3.html\`) from each line.
- \`reducer.py\`: Aggregates visits and outputs the total per page.

---

## ⚡ Spark Implementation (Folder: \`spark/\`)

This folder contains the **Apache Spark** (PySpark) versions of the same two problems, suitable for distributed computing with large datasets.

### 🔹 \`conversion_rate_spark.py\`
- Reads the e-commerce log file.
- Parses each line and aggregates view/purchase counts using RDD or DataFrame operations.
- Computes and displays the conversion rate for each item.

### 🔹 \`weblog_analytics_spark.py\`
- Reads the web server log file.
- Extracts file paths and counts occurrences using Spark transformations.
- Displays sorted counts of page visits.

---




