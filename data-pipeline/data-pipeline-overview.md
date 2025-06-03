# Data Pipeline Overview

This document describes the data flow and integration logic used in the project to enable campaign attribution, CRM syncing, and dashboarding.

## 🔁 Flow Components:
1. **Source**: HubSpot/Salesforce CRM data + website tracking + email performance
2. **ETL Layer**: n8n workflows or Make.com scenarios to clean, enrich, and transform
3. **Storage**: Google Sheets or SQL DB (depending on client)
4. **BI Layer**: Power BI or Tableau with custom DAX/SQL queries

## 📊 Pipeline Objectives:
- Normalize lead data
- Map campaign attribution to conversion events
- Create unified reporting tables for dashboards

## ⚙️ Tools Used:
- n8n (for webhook triggers and transformations)
- Make.com (for integrations and delays)
- HubSpot API / Salesforce API
- SQL (cleaning, joining, deduplication)