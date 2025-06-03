# CRM Automation Workflows

This document outlines the CRM workflows designed and deployed for this AI-powered MarTech platform. The workflows were adapted depending on the client's stack (HubSpot or Salesforce).

## 🎯 Objectives:
- Automate lead nurturing and follow-up sequences
- Align CRM stages with marketing triggers and scoring
- Enable dynamic segmentation based on engagement

## 💡 Example Workflow (HubSpot):
1. **Trigger**: New lead fills out landing page form
2. **If**: Lead score ≥ 60 → Assign to SDR and enter sales pipeline
3. **If**: Lead score < 60 → Enter 5-email nurturing sequence
4. **After 10 days**: Recalculate score based on behavior
5. **If engagement threshold met** → Exit nurture and assign to sales

## 🧩 Salesforce Equivalent:
- Integrated with Pardot for campaign scoring
- Used custom objects to track campaign attribution
- Enabled field mapping to sync with reporting dashboards

## 🔄 Tools Used:
- HubSpot Workflows & Sequences
- Salesforce Flow / Process Builder
- Lead Scoring Rules
- Email Automation