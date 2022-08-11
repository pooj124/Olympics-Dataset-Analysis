# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC ## Overview
# MAGIC 
# MAGIC This notebook will show you how to create and query a table or DataFrame that you uploaded to DBFS. [DBFS](https://docs.databricks.com/user-guide/dbfs-databricks-file-system.html) is a Databricks File System that allows you to store data for querying inside of Databricks. This notebook assumes that you have a file already inside of DBFS that you would like to read from.
# MAGIC 
# MAGIC This notebook is written in **Python** so the default cell type is Python. However, you can use different languages by using the `%LANGUAGE` syntax. Python, Scala, SQL, and R are all supported.

# COMMAND ----------

# MAGIC %sql
# MAGIC create database if not exists Capstone;
# MAGIC use Capstone;

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists athlete_events
# MAGIC using csv 
# MAGIC options(
# MAGIC     header "true",
# MAGIC     path "/FileStore/tables/athlete_events.csv",
# MAGIC     inferschema "True"
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists regions
# MAGIC using csv 
# MAGIC options(
# MAGIC     header "true",
# MAGIC     path "/FileStore/tables/noc_regions.csv",
# MAGIC     inferschema "True"
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC show tables;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from athlete_events;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from regions

# COMMAND ----------

# MAGIC %sql
# MAGIC --counting number of males and females in total
# MAGIC select Sex, count(Sex) as gender_count
# MAGIC from athlete_events
# MAGIC group by Sex;

# COMMAND ----------

# MAGIC %sql 
# MAGIC --Observing the datatypes of columns
# MAGIC desc table athlete_events;

# COMMAND ----------

# MAGIC %sql
# MAGIC select Sex, min(Age), max(Age)
# MAGIC from athlete_events
# MAGIC group by Sex;

# COMMAND ----------

# MAGIC %sql
# MAGIC --Observing the total number of medals won by a team
# MAGIC select Team,count(*)
# MAGIC from athlete_events
# MAGIC where Medal <> 'NA'
# MAGIC group by Team
# MAGIC order by count(*)desc;

# COMMAND ----------

# MAGIC %sql
# MAGIC --Country with most number of players
# MAGIC select Team, count(*)
# MAGIC FROM athlete_events
# MAGIC where Name <> 'NA'
# MAGIC group by Team
# MAGIC order by count(*) desc;

# COMMAND ----------

# MAGIC %sql
# MAGIC --Which country won more medals by sport

# COMMAND ----------


