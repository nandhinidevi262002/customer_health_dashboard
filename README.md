# Customer Health Scoring & Segmentation Dashboard

A data-driven solution to monitor and evaluate customer health using engagement metrics, built with **Streamlit** for interactive web visualization and **Power BI** for advanced business intelligence. This project enables Customer Success teams to proactively manage customer relationships and reduce churn risk.

---

## Project Objective

To develop a robust customer health model and visualize key metrics through dashboards, enabling data-driven decision-making for customer success initiatives.

---

## Dataset Overview

The dataset includes the following key customer metrics:

- Usage Frequency
- Logins in the Last 30 Days
- Support Ticket Responses
- Feature Adoption Rate
- Customer Success Manager (CSM) Engagement Score

---

## Health Score Model

A weighted scoring model was created to quantify customer health:

| Metric                   | Weight (%) |
|--------------------------|------------|
| Usage Frequency          | 25%        |
| Logins (30 Days)         | 20%        |
| Support Ticket Responses | 15%        |
| Feature Adoption Rate    | 25%        |
| CSM Engagement Score     | 15%        |

Each customer is assigned a **Health Score (0–100)** and categorized as:

| Score Range | Status   |
|-------------|----------|
| >= 75       | Healthy  |
| 50 – 74     | At-Risk  |
| 0 – 49      | Critical |

---

## Segmentation & Analysis

Utilizing pivot tables and filters, customers are segmented by:

- Industry
- Subscription Plan
- Health Status

This helps identify patterns and prioritize accounts based on risk level and strategic importance.

---

## Dashboards

### Streamlit Dashboard

An interactive web app built using **Streamlit**, offering:

- Health score distribution
- Critical accounts overview
- Industry and plan filters
- Dynamic charts and tables

### Requirements

- Python 3.8 or higher  
- Streamlit  
- Pandas, Plotly, and other dependencies (see `requirements.txt`)  
- Power BI Desktop (for `.pbix` file)

### Setup

Install Python dependencies:

```bash
pip install -r requirements.txt
````

Run the Streamlit app locally with:

```bash
streamlit run app.py
````
### Live Demo

Explore the interactive customer health dashboard live here:  
🔗 [Customer Health Dashboard - Streamlit App](https://customer-health-dashboard.streamlit.app/)


### Power BI Dashboard

A comprehensive Power BI report providing:

* Overview of health metrics
* Drill-down analysis by customer segments
* Identification of top critical accounts
* CSM performance impact insights

Open the Power BI file (`assignment.pbix`) using Power BI Desktop.

---

## Case Scenario: A key customer has shifted from a “Healthy” to a “Critical” health status.

**Recommended Actions for the Customer Success Management (CSM) Team:**

### Conduct a Root Cause Analysis:
The first step is to analyze the underlying reasons for the drop. This includes reviewing product usage metrics, support ticket history, login frequency, and engagement data. Identifying any sudden changes or declining trends in these areas is critical.

### Initiate Immediate Customer Outreach:
A CSM should proactively schedule a call with the customer to understand their current challenges. This conversation should be empathetic, solution-oriented, and focused on regaining the customer's trust and satisfaction.

### Develop a Customized Success Plan:
Based on the feedback and data, the CSM should create a tailored action plan. This may include additional training, onboarding support for new features, enhanced communication, or product customizations that align with the customer’s goals.

### Increase Internal Collaboration:
The situation should be escalated internally, involving product, support, and account management teams. This ensures a coordinated response and helps in resolving cross-functional issues that may be impacting the customer’s experience.

### Enhance Engagement Efforts:
Strategies such as personalized feature recommendations, success stories, and usage incentives can be deployed to re-engage the customer. If applicable, offering temporary access to premium features or early access programs may also add value.

### Monitor and Follow Up Regularly:
Set up periodic health checks and monitor progress closely through the health dashboard. Continuous follow-ups over the next 30–60 days can help ensure the situation improves and demonstrates commitment from the CSM team.

**Conclusion:**  
A decline from “Healthy” to “Critical” is a significant indicator of customer dissatisfaction or disengagement. Taking prompt, data-driven, and personalized actions not only helps retain the customer but also reinforces the company’s commitment to their success.

---

## Project Structure

```bash
customer_health_dashboard/
├── app.py                         # Streamlit application
├── Power BI/
│   ├── assignment.pbix            # Power BI report file
│   └── customer_health_dashboard_demo/  # Power BI demo assets 
├── dataset/
│   ├── customer_metrics.xlsx      # Cleaned dataset
│   └── intern_assignment/         # Supplementary files
├── README.md                      # Project documentation

````

---

## Let's Collaborate!  

Feel free to open issues or submit pull requests. Contributions, suggestions, and feedback are always welcome!  

- [LinkedIn](https://www.linkedin.com/in/nandhinidevi2605)
- [Personal Website](https://github.com/nandhinidevi262002)
- [Email](nandhinidevis2023@gmail.com)

---

## Star the Repo  

If you find this repository helpful, don't forget to give it a ⭐️ and share it with the community!
