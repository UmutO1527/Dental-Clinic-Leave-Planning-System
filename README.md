# Dental-Clinic-Leave-Planning-System
An AI-powered leave planning and patient demand forecasting system for dental clinics. This project predicts daily patient intensity using historical clinic data and calculates how many employees can safely take leave without disrupting operations.


## Features

* Predicts daily patient count using **Random Forest Regression**
* Converts dates into machine learning features automatically
* Considers:

  * Weekdays
  * Seasonal patterns
  * Public holidays
  * Religious holidays
  * Days remaining until holidays
* Calculates:

  * Required staff count
  * Maximum leave approvals
  * Safety staffing margin
* Built with:

  * Python
  * Pandas
  * NumPy
  * Scikit-learn

---

## Project Structure

```bash
dental-leave-system/
│
├── dent_dataset.csv
├── main.py
├── requirements.txt
└── README.md
```

---

## How It Works

The model is trained using two years of historical patient data.

The system extracts time-based features such as:

* Day of year
* Day of week
* Month
* Holiday information

A `RandomForestRegressor` then predicts the expected patient count for a selected date.

Finally, the system calculates:

```text
Maximum Leave Capacity =
Total Staff
- Required Staff
- Safety Margin
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/UmutO1527/Dental-Clinic-Leave-Planning-System.git
cd Dental-Clinic-Leave-Planning-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Requirements

```txt
pandas
numpy
scikit-learn
```

---

## Usage

Run the project:

```bash
python main.py
```

Example input:

```text
Date (Y-M-D): 2026-07-15
```

Example output:

```text
--------------------------------------------------
Target Date: 2026-07-15
Predicted Patient Count: 128
Required Staff in Clinic: 10 (Including safety margin)
MAXIMUM APPROVED LEAVE: 0 staff member(s)
--------------------------------------------------
```

---

## Machine Learning Model

The project uses:

```python
RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
```

Why Random Forest?

* Handles seasonal behavior well
* Learns nonlinear patterns
* Robust against noisy data
* Works effectively on tabular datasets

---

## Future Improvements

* Web dashboard with Flask or FastAPI
* Real-time holiday API integration
* Deep learning forecasting models
* Automatic shift scheduling
* Employee-specific leave optimization
* Visualization dashboards
* Multi-clinic support

---

## Example Use Cases

* Dental clinics
* Hospitals
* Small healthcare centers
* Seasonal businesses
* Workforce planning systems

---

## License

MIT License

---

## Author

Developed by Umut
AI & Engineering Student focused on machine learning systems and intelligent automation.
