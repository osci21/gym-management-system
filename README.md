# Gym Management System

This is a basic Python-based command-line project I built to manage gym memberships and track customer data. It uses **Pandas** to handle all the backend record storage in a CSV file and **Matplotlib** to generate visual charts

---

## What it Does

* **View Records:** Loads the CSV file into a Pandas DataFrame and prints out a clean, organized table of all current members.
* **Add New Members:** Takes input for a new member (ID, Name, Age, Weight, Height, Membership Type, and Fee) and appends it dynamically to the dataset.
* **Delete Members:** Lets you search for a member by name and completely removes their record from the system.
* **Modify Details:** Allows you to select a specific member and update individual details like their current weight, membership tier, or fees.
* **Data Visualization:** Uses Matplotlib to instantly generate two types of bar graphs:
  1. A chart comparing **Member Names vs. Weights**.
  <img width="398" height="340" alt="image" src="https://github.com/user-attachments/assets/f38b5aac-f3b9-4b0e-b519-dba9ef78353c" />

  2. A chart analyzing **Member Names vs. Membership Fees**.
  <img width="398" height="340" alt="image" src="https://github.com/user-attachments/assets/4cc9960a-bf3d-4310-864c-726591a0703f" />

---

## Tech Stack
* **Language:** Python
* **Libraries Used:** Pandas & Matplotlib
* **Storage:** CSV (Comma-Separated Values)

---

## How to Run
1. Make sure you have Python, `pandas`, and `matplotlib` installed.
2. Download both `gym_management.py` and `gym_data.csv` into the exact same folder.
3. Open `gym_management.py` using **IDLE**.
4. Just press **F5** (or click *Run -> Run Module*) to launch the system interface.
