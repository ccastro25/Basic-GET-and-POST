# Local Stores Price Comparison

## Overview
This project involves scraping local stores to compare prices. The front-end is built with HTML, CSS, and JavaScript. Python is used for web scraping and writing data to a MySQL database, with Node.js serving as middleware. The project is transitioning from Selenium to Playwright for web scraping.

## Technologies Used
- **Front-End**: HTML, CSS, JavaScript
- **Back-End**: Python (web scraping)
- **Database**: MySQL
- **Middleware**: Node.js
- **Web Scraping**: Transitioning from Selenium to Playwright

## Instructions

### Web Scraping and Database Integration
- **Python**: Used to scrape sites and store data in MySQL.
- **Node.js Middleware**: Refer to [Node.js and Express framework](https://www.tutorialspoint.com/nodejs/nodejs_express_framework.htm) for handling POST and GET requests.

### Database Configuration
- **MySQL Connection**: Utilize the [mysql2 package](https://www.npmjs.com/package/mysql2) instead of `mysql`. Learn more about the issues with `mysql` [here](https://stackoverflow.com/questions/50093144/mysql-8-0-client-does-not-support-authentication-protocol-requested-by-server/56509065#56509065).

### Front-End Development
- **CSS Reference**: Check out this [CSS example](https://codepen.io/chriscoyier/pen/vWEMWw) for inspiration.
- **JSON to HTML Table**: Follow this [guide on converting JSON data to HTML tables using JavaScript/jQuery](https://www.tutorialspoint.com/how-to-convert-json-data-to-a-html-table-using-javascript-jquery).

## Conclusion
This project demonstrates a comprehensive approach to scraping and comparing local store prices, leveraging a full-stack solution with modern web development technologies.
