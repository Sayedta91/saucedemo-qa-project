# SauceDemo QA Testing Project

## Project Overview
The goal of this testing project was to check the main features of the application and identify any functional or usability issues through structured manual and automated testing.

Tested areas include:

- Login functionality
- Product inventory page
- Cart functionality
- Checkout process

Application: SauceDemo
Testing Type: Manual Testing & Test Automation
Tools: Excel, PDF
Browser: Firefox (Latest Version)
Operating System: Windows 10

## Test Scope

In Scope:
- Login functionality
- Product inventory page
- Add to cart / Remove from cart
- Cart persistence
- Checkout process

Out of Scope:
- Payment processing
- Performance testing
- Security testing

---

## Test Deliverables

This repository includes:

Test Plan
- Testing objectives
- Scope
- Test scenarios
- Environment details
- Entry & exit criteria
- Risks and mitigation

Test Cases
- Detailed test case documentation
- Test steps
- Expected results
- Actual results
- Pass/Fail status

Bug Reports
- Defects identified during execution
- Severity classification
- Reproduction steps

---

## Automation Framework

I used Playwright, following the Page Object Model (POM) design pattern

Login Tests
- Valid login
- Invalid login
- Locked out user
- Missing username
- Missing password

Inventory Tests
- Product count validation
- Sort A-Z / Z-A
- Price sort low-high / high-low
- Sorting persistence after refresh

Cart Tests
- Add item to cart
- Remove item from cart
- Cart retains items after navigation

Checkout Tests
- Checkout flow starts successfully
- Valid checkout information
- Empty field validation
- Missing last name validation
- Missing postal code validation
- Order completion

---
## Project Structure
```bash
project/

pages/
├── login_page.py
├── inventory_page.py
├── cart_page.py
└── checkout_page.py

tests/
├── test_login.py
├── test_inventory.py
├── test_cart.py
└── test_checkout.py

conftest.py
requirements.txt
```


## Test Summary


| Metric | Result |
| ------------- | ------------- |
| Total Test Cases | 20  |
| Passed | 17  |
| Failed  | 3  |

Key Issues Found
- Product sorting issues
- Minor UI inconsistencies
- User experience issues in inventory/cart flow

## Test Approach

Testing was performed manually using predefined test cases and exploratory testing.

Testing types included:
- Functional Testing
- UI Testing
- Exploratory Testing
- Regression Testing

--- 

## Setup & Run

Install Dependencies:

``` pip install -r requirements.txt ```

Install Playwright browsers

``` playwright install ```

Run tests

``` pytest -v```


Author

Tariq Sayed


