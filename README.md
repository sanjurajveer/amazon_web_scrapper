# Amazon Web Scraper

This project is a Python-based web scraper designed to extract product details (title and price) from Amazon product pages. The data is stored in a CSV file for further analysis or tracking purposes.

## Features

- Extracts the product title and price from an Amazon product page.
- Handles dynamic changes in the website structure with error handling.
- Stores the scraped data in a CSV file with timestamps.

## Prerequisites

Ensure the following libraries are installed:

- `beautifulsoup4`
- `requests`
- `pandas`
- `datetime`
- `smtplib` (optional for email notifications)

You can install the required libraries using pip:
```bash
pip install beautifulsoup4 requests pandas
```

## How It Works

1. **Connect to Amazon Website**
   - The scraper connects to the specified Amazon product page using the `requests` library.

2. **Parse the HTML Content**
   - Utilizes `BeautifulSoup` to parse and navigate the HTML structure to find specific elements such as product title and price.

3. **Extract Data**
   - Extracts the product title and price by locating specific HTML tags and attributes.

4. **Store Data**
   - Saves the extracted data to a CSV file with headers (`Title`, `Price`, `Date`).

5. **Track Changes** (Future Feature)
   - The data stored in the CSV file can be used to track price changes over time.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/amazon-web-scraper.git
   ```

2. Navigate to the project directory:
   ```bash
   cd amazon-web-scraper
   ```

3. Run the scraper:
   ```bash
   python scraper.py
   ```

4. The output will be saved to `AmazonWebScraperDataset.csv` in the project directory.

## Example Output

After running the scraper, the following data is stored in `AmazonWebScraperDataset.csv`:

| Title                 | Price   | Date       |
|-----------------------|---------|------------|
| Example Product Title | $99.99  | 2024-12-29 |

## Notes

- Ensure that the URL corresponds to a valid Amazon product page.
- Be cautious of Amazon's anti-scraping measures. Use headers to mimic browser requests.
- The User-Agent header can be added to enhance reliability.

## Future Enhancements

- Automate price tracking over time with periodic execution.
- Notify users via email when prices drop.
- Expand support for scraping additional product details.

## License

This project is licensed under the MIT License. Feel free to use and modify it for personal or commercial purposes.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes.

---

Happy Scraping! If you have any questions, feel free to reach out.

