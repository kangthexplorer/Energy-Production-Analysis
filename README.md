# Wind and Solar Energy Production Analysis

## Overview
This project analyzes **wind and solar energy production patterns** using historical hourly data.  
The goal is to understand how both renewable energy sources behave across **time, days, months, and seasons**, and how they complement each other.

The analysis is performed using **pandas** for data manipulation and **matplotlib** for visualization.

## Objective
- Analyze hourly energy production trends
- Compare wind and solar energy behavior
- Identify daily, monthly, and seasonal patterns
- Evaluate reliability and variability of each source
- Understand the benefits of combining wind and solar energy

## Tools Used
- Python  
- pandas  
- matplotlib  

## Data Preparation
The following pre-processing steps were performed:
- Converted the `Date` column to datetime format
- Created an `Hour` column from `Start_Hour`
- Checked for missing and invalid values
- Grouped and reshaped data for analysis

## Exploratory Data Analysis
### 1. Total Energy Production by Source
   **Question: Which energy source produces more energy overall?**
   - Wind energy contributes more total energy than solar
   - Solar production is limited to daylight hours

### 2. Hourly Energy Production Pattern
   **Question: How does energy production vary throughout the day?**
   - Solar energy production is zero during night hours
   - Solar output peaks around midday
   - Wind energy is available throughout the day and night
   - Wind shows greater consistency than solar

### 3. Day-wise Production Analysis
   **Question: Does production vary across days of the week?**
   - Solar production remains fairly consistent across days
   - Wind production shows minor variation
   - No strong weekday or weekend dependency observed

### 4. Monthly Energy Production Trends
   **Question: How does energy production change across months?**
   - Solar energy production is highest in summer months
   - Wind energy increases during winter and monsoon months
   - Clear seasonal complementary is observed

### 5. Seasonal Energy Production
   **Question: How do seasons affect energy generation?**
   - Solar dominates during summer
   - Wind performs better in winter and fall
   - Seasonal differences support hybrid renewable systems

### 6. Reliability and Variability
   **Question: Which energy source is more consistent?**
   - Wind energy shows lower variability
   - Solar energy is more variable due to dependence on sunlight

### 7. Combined Energy Analysis
   **Question: How does total renewable energy behave?**
   - Combined wind and solar production reduces sharp drops
   - Hybrid systems improve overall energy stability

### Key Findings
- Solar energy is most effective for meeting daytime peak demand
- Wind energy provides a stable baseline supply
- Wind and solar complement each other both daily and seasonally
- A combined renewable energy system improves reliability

## Conclusion
- This analysis shows that wind and solar energy are highly complementary renewable sources.
- While solar energy is limited to daylight hours, wind energy provides consistent production throughout the day and night.
- Combining both sources results in a more reliable and balanced energy system.
