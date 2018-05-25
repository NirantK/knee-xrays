# Prosthetic Identification from Patient Radiograph

This repository hosts all code, including exploratory datasets and codebases. 

## Problem
Orthopaedic Transplants are powerful ways to improve quality of life for an aging population. Most of these transplants need to be operated upon again after 5-10 years or their lifetime. This can be for prosthetic repair, replacement or simply to fix wear and tear. 


For this, the surgeon needs to know the correct prosthetic model and manufacturer. This is tough as there are over hundreds of models for each type of prosthetic. For instance, there are atleast 200+ knee prosthetic models which are possible. Identifying this manually, is not only tedious but also

### Core Technical Challenge
Identifying the correct prosthetic model make from patient xray

Data Constraint: Number of image samples per prosthetic model made is less than 3

## Proposed Solution

Build an image processing pipeline with two main components: 
- Localisation - to extract the prosthetic model outline (countours/edges/polygon matches) 
- Feature Extraction - use a feature extraction suite as SIFT, VGG16 or similar 
- Classification - in the feature space, find the top 5 most similar models from your database
  - Alternatively: Use template matching techniques here to collapse last 2 steps into one
