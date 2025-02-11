# Investment Evaluator

## Overview
The **Investment Evaluator** is a Python-based financial analysis toolkit that provides essential tools for evaluating equity investments, fixed-income securities, and risk-return metrics. It includes implementations of key financial formulas used in investment analysis, helping users assess returns, valuation, and risks.

## Features
### 1. **Equity Evaluator** (`equity_evaluator.py`)
- Calculates total return on a stock (capital gains + dividends).
- Implements valuation models:
  - **Dividend Discount Model (DDM)**
  - **Gordon Growth Model**
- Computes fundamental stock metrics:
  - **Price-to-Earnings (P/E) Ratio**
  - **Earnings Yield**
  - **Dividend Yield**
- Evaluates **Net Present Value (NPV)** of cash flows.

### 2. **Fixed-Income Evaluator** (`fi_evaluator.py`)
- Calculates:
  - **Effective Annual Rate (EAR)**
  - **Annuity Compound and Discount Factors**
  - **Bond Prices and Treasury Bill Yields**
  - **Perpetuity Prices**
  - **Annual Percentage Rate (APR) for Treasury Bills**

### 3. **Risk & Return Evaluator** (`risk_return.py`)
- Computes:
  - **Return on Security** (including cash flows)
  - **Geometric and Arithmetic Mean Returns**
  - **Volatility (Standard Deviation) and Annualized Volatility**

## Installation
Ensure you have Python installed, then install dependencies:
```bash
pip install statsmodels
```

## Usage
Import the relevant module and use its methods:
```python
from equity_evaluator import EquityEvaluator

# Calculate total return on a stock
return_percentage = EquityEvaluator.return_on_stock(100, 120, 5)
print(f"Total Return: {return_percentage}%")
```

## License
This project is licensed under the MIT License.

