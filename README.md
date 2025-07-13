# BuildingConnected Login Bot

A simple Python automation script using Selenium to log into [BuildingConnected](https://app.buildingconnected.com), handle session cleanup, and support manual MFA input.

---

## Features

- Automated login/logout
- Incognito browser mode
- verification code support
- Clears cookies/localStorage/sessionStorage
- Error screenshots on failure

---

## Setup

1. **Install dependencies**:
   
   pip install selenium webdriver-manager(I used try except to handle this)
   
   
2. Create Crentials.py:

     Email = "your_email@example.com"
     password = "your_password"

      please change your Crentials in this script.


3. Run the script:

  python BuildingConnect.py   
