# 🔩 L-Bracket Static Load Analysis

### Finite Element Analysis + Python Post-Processing

A complete structural analysis of an **L-shaped mounting bracket** under static loading.  
This project combines **CAD modeling**, **ANSYS FEA**, and **Python (NumPy)** post-processing to evaluate stress, deformation, and failure behavior.

---

## 📌 Project Overview

An L-bracket is a common mechanical component used for mounting and support.  
This study investigates how the bracket behaves under increasing downward loads, identifying:

- Maximum stress locations  
- Onset of plastic deformation  
- Approximate failure load  
- Safety factors under different loading conditions

---

## 🛠️ Tools Used

| Stage              | Software / Library      |
|--------------------|-------------------------|
| CAD Modeling       | SolidWorks              |
| FEA Simulation     | ANSYS Mechanical        |
| Post-Processing    | Python + NumPy          |
| Data Export        | CSV / TXT               |
| Version Control    | GitHub                  |

---

## 🔍 Analysis Performed

- Linear Static Structural Analysis  
- Non-Linear Analysis (Large Deflection + Plasticity)  
- Multiple Load Cases: 250 N, 500 N, 750 N, 950 N, 2000 N  
- Stress & Total Deformation evaluation  
- Safety Factor calculation  
- Plastic zone identification  
- Failure load estimation

---

## 📊 Key Findings

| Load (N) | Max Stress (MPa) | Behavior                  |
|----------|------------------|---------------------------|
| 250      | \~99              | Elastic                   |
| 500      | \~198             | Elastic                   |
| 750      | \~228–297         | Plasticity starts         |
| 2000     | \~480             | Near failure              |

**Estimated Failure Load:** ≈ **1650 N**

---

## 🐍 Python Post-Processing

The script `numpy_postprocess.py` automatically:

- Reads exported stress & deformation data  
- Calculates Max, Min & Mean values  
- Determines plastic deformation start point  
- Estimates failure load  
- Generates a clean `results.txt` report

---

## 🚀 How to Run

1. Export stress and deformation results from ANSYS as CSV/TXT  
2. Place the files in the same folder as the script  
3. Run:

```bash
python numpy_postprocess.py
