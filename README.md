# 📊 BigData-Hadoop-Spark

This repository contains two main categories of data analytics solutions:

- **Hadoop**: Solutions using Python MapReduce with Hadoop Streaming for scalable log and activity analysis.
- **Spark**: Scalable machine learning and clustering projects using PySpark for classification and unsupervised learning.

---



## 📁 Folder Structure

BigData-Hadoop-Spark/ ├── hadoop/ │ ├── conversion-rate/ │ │ ├── mapper.py │ │ └── reducer.py │ └── weblog-analytics/ │ ├── mapper.py │ └── reducer.py └── spark/ ├── human_activity_classification_spark.py └── cybersecurity_clustering_spark.py


---

## 🛠 Hadoop MapReduce Solutions (`hadoop`)

### 📦 `conversion-rate`
#### 🧩 Problem: E-Commerce Conversion Rate

You are analyzing logs from the “E-Shop” website to calculate the **conversion rate** of each item. User actions include `view`, `add_to_cart`, and `purchase`.

📌 **Formula**:  
`conversion_rate(item) = number_of_purchases / number_of_views`

Some purchases might occur without views, and vice versa.

#### 📂 Files:
- `mapper.py`: Emits `(item, action)` pairs.
- `reducer.py`: Aggregates actions and computes conversion rates.

✅ **Real-World Insight**:  
A warehouse rumor says **"TypeC_HDMI"** is abundantly available, so it should show a low conversion rate, validating your results.

---

### 📦 `weblog-analytics`
#### 🧩 Problem: Web Page Visit Frequency

Given a web server log file, determine which web pages are most and least visited. Each line is a user request for a page like `/file_X.html`.

#### 📂 Files:
- `mapper.py`: Extracts web page visits from log lines.
- `reducer.py`: Counts total visits per page.

✅ **Real-World Insight**:  
It's rumored that `/file_8.html` is unimportant, so it should have a low number of visits, serving as a sanity check.

---

## ⚡ Spark Solutions (`spark`)

### 🔹 `human_activity_classification_spark.py`
#### 🧩 Problem: Human Activity Recognition (HAR)

Using the `HAR_3000.csv` dataset, recognize physical activities using sensor data from wearable devices.

#### 💡 Steps:
1. Read the dataset into a Spark DataFrame.
2. Use `StringIndexer` to encode `Activity`.
3. Prepare features for **Logistic Regression**.
4. Train/Test split (80/20, seed=3).
5. Apply **10-fold cross-validation** with Logistic Regression.
6. Evaluate using **accuracy, precision, recall, F1-score**.
7. Apply **Random Forest** with grid search:
   - Trees: `[10, 15, 20, 25]`
   - Max depth: `[3, 5, 7, 9]`
8. Extract the top **50 important features**.
9. Train Logistic Regression on reduced features.
10. Compare performance before and after feature selection.

---

### 🔹 `cybersecurity_clustering_spark.py`
#### 🧩 Problem: Cybersecurity Threat Clustering

Analyze `ben_inf_allFeatures_balanced_FS01.csv`, a dataset with features related to cybersecurity and network activity.

#### 💡 Steps:
1. Load the dataset with Spark.
2. Prepare features for clustering.
3. Apply **KMeans** clustering with `k` in `[2–10]`.
4. Compute **Silhouette Score** for each value of k.
5. Visualize or compare scores to find optimal **k**.
6. Use findings to help detect abnormal or suspicious behavior patterns.

---




