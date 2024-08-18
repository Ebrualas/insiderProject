# Insider QA Automation Project

## Overview

This project automates testing for the Insider website using Python and Selenium. The test cases cover various functionalities on the Insider website, including navigation, job filtering, and role view actions.

## Test Scenarios

1. **Verify Home Page**: Visit [Insider Home Page](https://useinsider.com/) and check if it opens correctly.
2. **Navigate to Careers Page**: Select the "Company" menu in the navigation bar, then select "Careers". Verify that the Careers page, including Locations, Teams, and Life at Insider blocks, are visible.
3. **Job Filtering**: Navigate to [Quality Assurance Jobs](https://useinsider.com/careers/quality-assurance/), click "See all QA jobs", filter jobs by Location: "Istanbul, Turkey", and Department: "Quality Assurance". Check that the jobs list is present.
4. **Verify Job Details**: Ensure all jobs in the list have the Position "Quality Assurance", Department "Quality Assurance", and Location "Istanbul, Turkey".
5. **Check Role View**: Click the "View Role" button and verify that it redirects to the Lever Application form page.

## Requirements

- Python 3.7 or higher
- Selenium 4.x
- ChromeDriver (matching your Chrome version)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Ebrualas/insiderProject.git
   cd insiderProject
