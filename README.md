#  Comprehensive Analysis of the Polish Housing Market Using Otodom Data

##  Overview
This project delivers an in-depth analysis of Poland’s housing market using data sourced from **Otodom.pl**, a leading real estate platform in the country. The goal is to explore patterns and insights in property listings across major Polish cities, focusing on both rental and purchase markets.

---

##  Key Objectives

This analysis answers a wide range of real estate-related questions, including:

- Average rental prices for 1–4 room apartments across major cities  
- Suburbs in **Warsaw** where apartments match specific size and price criteria  
- What apartment sizes can be expected at different price ranges in various cities  
- The **most expensive** listings per city, with ad title, cost, size, and suburb  
- Ratio of **private vs business ads** on Otodom  
- Average **sale prices** for apartments sized between 50–70 m2 in major cities  
- Rental pricing patterns in **Warsaw suburbs**, grouped by surface area:
  - 0–50 m2
  - 50–100 m2
  - 100+ m2  
- Top 3 **luxury neighborhoods** in Warsaw (listings over 2M PLN)  
- Top 5 most **budget-friendly neighborhoods** for families looking for 40–60 m2 apartments  
- Suburbs with the **highest and lowest number** of private ads in Warsaw  
- Comparative analysis of **rental vs sale prices** in key cities  

---

## 🛠 Technologies Used

- **Snowflake** – For data storage, transformation, and advanced querying  
- **Google Sheets API** – Used to translate property descriptions from Polish to English  
- **Python (Geopy)** – Converted geographic coordinates (latitude/longitude) to readable street addresses  

---

##  Data Preparation & Transformation

Several preprocessing steps were performed to prepare the dataset for analysis:

- Converted raw JSON data to a structured CSV format  
- Translated property descriptions using the **Google Sheets API**  
- Geocoded latitude/longitude data into physical addresses with **geopy**  

![Average rental prices for 1–4 room apartments across major cities  ](sql-real-estate-analysis/images/avg-rent.png)
---

##  How to Use

This project includes  **SQL query files** (for hands-on analytics). You can:

- Browse the SQL scripts provided in the `/scripts/` folder  
- Replicate the queries in your own Snowflake workspace  
- Modify the queries to suit custom exploration or reporting  

---

##  Insights & Impact

The final output offers valuable insights for:
- **Homebuyers** comparing cities and neighborhoods  
- **Renters** looking for budget-specific or luxury listings  
- **Real estate analysts** examining trends in Polish housing supply and demand  

---

##  Conclusion

By combining cloud data warehousing, geolocation services, and translation APIs, this project provides a holistic view of real estate dynamics in Poland. Whether you're a renter, buyer, investor, or data enthusiast, this analysis serves as a detailed reference to better understand the housing market landscape.
