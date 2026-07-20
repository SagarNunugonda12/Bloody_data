# Chapter 5 Lab Report: CSV vs JSON Analysis

### 1. Which format is better for APIs?
**JSON** is much better for web APIs. APIs typically communicate structured or complex nested objects (like a user who has multiple shipping addresses). JSON naturally supports array lists and nested schemas, making it the industry standard communication format for software services.

### 2. Which format is better for analytics?
**CSV** is better compared to JSON because it features significantly lower storage footprint overhead. Because CSV only writes column headings *once* at the top of the file, it saves a lot of storage compared to JSON which repeats keys `{"Name": "..."}` for millions of rows. 
*(Note: Later we will learn that column-based formats like Parquet outperform both for analytics!)*

### 3. Which format would you choose for a dashboard and why?
**CSV (or flat tabular structures)**. Dashboarding engines like Power BI, Tableau, or Excel expect columns and rows to build charts efficiently. If you give a dashboard engine raw JSON, it forces the engine to run heavy conversion workflows to flatten out the objects before rendering data.