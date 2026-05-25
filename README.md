
# University Computer Science Projects Portfolio

Welcome to this repository showcasing a diverse collection of university projects. Each project targets a different paradigm or aspect of computer science, ranging from functional programming and machine learning to network security and interactive applications.

## Table of Contents

1. [Functional & Logical Programming (FLP) Assignment](https://www.google.com/search?q=%231-functional--logical-programming-flp-assignment)
2. [Multilayer Perceptron (MLP) Regressor](https://www.google.com/search?q=%232-multilayer-perceptron-mlp-regressor)
3. [Stock Price Dataset Analysis](https://www.google.com/search?q=%233-stock-price-dataset-analysis)
4. [Quiz Game](https://www.google.com/search?q=%234-quiz-game)
5. [Network Scanner with Scapy](https://www.google.com/search?q=%235-network-scanner-with-scapy)

---

## 1. Functional & Logical Programming (FLP) Assignment

This project simulates the creation, processing, and analysis of a system log file, demonstrating how the same data problem can be approached from both Functional and Logical paradigms.

### Core Workflow

* **Log File Generation:** Automatically generates a fake log file containing 1,000 entries. Each entry includes a timestamp, a log level (`INFO`, `ERROR`, `WARNING`, or `DEBUG`), and a context-specific message.
* **Data Extraction & Processing:** Parses the generated log file to calculate:
* The total number of log entries per hour (24-hour breakdown).
* The total number of entries for each log level.
* The average length of log messages.


* **Data Visualization:** Plots the extracted statistics using bar charts (activity by hour), a pie chart (distribution of log levels), and a histogram (distribution of message lengths).

### Paradigm Perspectives

#### 🔹 Functional Programming Perspective

The program processes data through a stateless workflow, emphasizing:

* **Pure Functions:** Tasks like generating messages and parsing lines have predictable outputs and zero side effects.
* **Data Transformation:** Data flows through mappings and transformations rather than altering structures in-place.
* **Immutability:** Log entries and counters are created fresh at each stage instead of mutating a global state.
* **Composability:** Reusable functions are chained together from file I/O to final visualization.

#### 🔹 Logical Programming Perspective

Alternatively, the log analyzer can be conceptualized through formal logic:

* **Collection of Facts:** Every log line is treated as a structured fact within a database.
* **Rule-Based Reasoning:** Logic rules can be defined to infer system anomalies (e.g., flagging sudden spikes in `ERROR` levels).
* **Declarative Intent:** Focuses on *what* conditions to find (e.g., *"Find all hours where warnings exceed 50"*) rather than step-by-step math implementation.

---

## 2. Multilayer Perceptron (MLP) Regressor

This project demonstrates how a Neural Network can approximate complex, non-linear functions using the `MLPRegressor` class from `scikit-learn`.

### Implementation Details

* **Data Generation:** Creates synthetic training data based on a noisy sine wave ($y = \sin(X) + \text{noise}$) where $X$ ranges from 0 to 5.
* **Model Architecture:** A Multilayer Perceptron consisting of **two hidden layers** (100 neurons in the first layer, 50 neurons in the second layer) configured to train for a maximum of 1,000 iterations.
* **Training & Prediction:** The model iteratively adjusts its internal weights to minimize the error between predictions and the true target values. Once trained, it predicts values across a smooth continuum ($x_{\text{new}}$ from 0.0 to 5.0).
* **Visualization:** Generates a plot overlaying the original noisy training points against the smooth regression line learned by the model to evaluate its accuracy.

---

## 3. Stock Price Dataset Analysis

Building upon the concepts explored in the MLP regression model, this project applies neural network-driven regression to a real-world scenario: analyzing and forecasting trends within a sample stock price dataset.

---

## 4. Quiz Game

> 🎮 *Just for fun!* An interactive, text-based terminal quiz game designed as a lighthearted application of basic programming constructs, conditional logic, and user input handling.

---

## 5. Network Scanner with Scapy

A surface-level networking script that utilizes the **Scapy** library to discover active devices on a local network and pull hardware vendor insights.

### Architecture & Mechanics

#### 1. Vendor Resolution (`get_vendor`)

* Takes a MAC address as an input and targets the external MAC Vendors API (`https://api.macvendors.com/`).
* Issues an HTTP GET request to fetch the hardware vendor. Returns `"Unknown"` if the API is unreachable or the MAC address is unrecognized.

#### 2. Network Scanning (`scan_network`)

* Constructs and broadcasts **ARP (Address Resolution Protocol)** request packets across a specified IP range in CIDR notation (Default: `192.168.100.1/24`).
* Uses Scapy's `srp()` function to send packets and listen for responses with a 2-second timeout window.
* Active devices respond with their MAC addresses, which are paired with the IP address and matched to a vendor name.

### Sample Output Format

The results are displayed in a clean, tabular structure directly within the console:

| IP Address | MAC Address | Vendor Name |
| --- | --- | --- |
| `192.168.100.1` | `00:1A:2B:3C:4D:5E` | Cisco Systems |
| `192.168.100.15` | `AA:BB:CC:11:22:33` | Apple Inc. |
| `192.168.100.102` | `4E:55:63:A1:B2:C3` | Unknown |
