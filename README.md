# Real-Time Bitcoin Dashboard
![GitHub last commit](https://img.shields.io/github/last-commit/Sahar-rad/Real-Time-Bitcoin-Dashboard)
![GitHub issues](https://img.shields.io/github/issues/Sahar-rad/Real-Time-Bitcoin-Dashboard)
![GitHub forks](https://img.shields.io/github/forks/Sahar-rad/Real-Time-Bitcoin-Dashboard)
![GitHub stars](https://img.shields.io/github/stars/Sahar-rad/Real-Time-Bitcoin-Dashboard)
![GitHub license](https://img.shields.io/github/license/Sahar-rad/Real-Time-Bitcoin-Dashboard)


### Overview

The Real-Time Bitcoin Dashboard addresses the need for real-time cryptocurrency price tracking and analysis. It leverages Microsoft Fabric and Power BI to create a seamless pipeline that retrieves, processes, and visualizes Bitcoin price data. 

This project is designed for cryptocurrency analysts, traders, and enthusiasts who need:
- Instant access to live Bitcoin price data.
- Comprehensive analytics to understand price trends.
- A reliable solution for decision-making based on real-time data insights.


## Power BI Visualizations
The dashboard provides:
1. Real-time tracking of Bitcoin prices.
2. Visual analytics of minimum, maximum, average, and current rates.
3. Weekly and daily breakdowns of Bitcoin price trends.

## Features
Real-time retrieval and processing of Bitcoin price data from an API.
Integration with Microsoft Fabric for efficient data ingestion and processing.
Real-time analytics and visualization using Event Hub and Power BI.
Automatic scheduling of data retrieval due to API request limitations.
Managed fields in Power BI for seamless integration without manual measure creation.
Interactive dashboard providing insights such as:
Current, minimum, maximum, and average Bitcoin rates.
Weekly and daily trend analysis of Bitcoin prices.
Real-time performance tracking.


## Preview
![Dashboard Preview](images/dashboard.png)

### Power BI File
The `DirectLakeSemanticModel.pbix` file contains the Power BI dashboard for real-time Bitcoin price analytics. To open this file:
1. Download the `.pbix` file to your local machine.
2. Open it using Microsoft Power BI Desktop.

### Data Flow
The following sections illustrate the data flow and transformations in the project.

---

#### **1. Source Data (API Data Preview)**
The data is retrieved from an external API providing real-time Bitcoin price information.

![Source Data Preview](images/source_data.png)

---

#### **2. Event Stream**
The real-time data is streamed using Azure Event Hub and processed through Event Stream for further transformations.

![Event Stream Flow](images/event_stream_flow.png)

---

#### **3. Destination Data (Lakehouse)**
The processed data is stored in the Lakehouse. This includes aggregated metrics like `Minimum Rate`, `Maximum Rate`, and `Average Rate`, along with calculated fields such as `Day`, `Month`, and `Week`.

![Destination Data Preview](images/destination_data.png)



