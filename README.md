# Prosthetic Identification from Patient Radiograph

This repository hosts all code, including exploratory datasets and codebases. 

### Problem
Prosthesis are powerful ways to improve quality of life for an aging population. Most of these need to be operated upon again after 5-10 years or their lifetime. This can be for prosthetic repair, replacement or simply to fix wear and tear. 


For this, the surgeon needs to know the correct prosthetic model and manufacturer. This is tough as there are over hundreds of models for each type of prosthetic. For instance, there are atleast 200+ knee prosthetic models which are possible. Identifying this manually, is not only tedious but also error prone.

## Core Technical Challenge
Identifying the correct prosthetic model make from patient xray

Each prosthetic model make is our *target label*

Data Constraint: Number of image samples per prosthetic model made is less than 3.

The data constraint effectively rules out most deep learning techniques which require a few thousand images per target label even for fine tuning.

## Proposed Solution

Build an image processing pipeline with two main components: 
- Localisation - to extract the prosthetic model outline (countours/edges/polygon matches) 
- Feature Extraction - use a feature extraction suite as SIFT, VGG16 or similar 
- Classification - in the feature space, find the top 5 most similar models from your database
  - Alternatively: Use template matching techniques here to collapse last 2 steps into one

### Understanding Prosthetics
- https://orthoinfo.aaos.org/en/treatment/revision-total-knee-replacement
- http://www.medicalexpo.com/medical-manufacturer/knee-prosthesis-4095.html
- https://www.peerwell.co/blog/2016/10/03/different-types-of-knee-replacement-implants/

The five most commonly used Knee arthroplasty / replacement implants are: PFC Sigma, AGC Biomet, Nexgen, Genesis 2, and Triathlon

- http://www.orthopaediclist.com/category/implants-3.html
- http://www.orthopaediclist.com/category/implant-identification.html
- http://whichorthopaedicimplant.com/
- https://www.realself.com/question/find-type-implant-x-ray-help

Dental Implant:

- http://whatimplantisthat.com/
- http://osseosource.com/dental-implants/


#### Links: 
- [Stanford MURA Dataset of Radiographs](https://stanfordmlgroup.github.io/competitions/mura/)
- [HOG+Linear VSVM with Hard Negative Mining](https://www.pyimagesearch.com/2014/11/10/histogram-oriented-gradients-object-detection/) is useful for localization

## Prior Work
- [Logo Grab Patent](https://patents.google.com/patent/US20160162758A1/en)
- [DSIFT Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6180045) on simaltaneous localisation and classification without training
- [An Enhanced Tibia Fracture Detection Tool Using Image Processing and Classification Fusion Techniques in X-Ray Images](https://pdfs.semanticscholar.org/be15/0af5f4f55d8ca25127b729b97cc461ce7c25.pdf)
- [FingerNet: Deep learning-based robust finger joint detection from radiographs](https://ieeexplore.ieee.org/document/7348440/)
- [Development of an analysis system of the X-rays of bones for prosthesis placement](https://ieeexplore.ieee.org/document/900433/)
