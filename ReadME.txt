# Automated OSINT Collection Tool

This tool provides a set of OSINT (Open Source Intelligence) collection modules that can help in gathering information from various sources like WHOIS, DNS, IP geolocation, directory fuzzing, Google Dorking, and email scraping. It is designed to automate the collection of public information that can be useful for penetration testing, cybersecurity research, or investigation.

## Features

- **IP Geolocation**: Retrieves geolocation information for a given IP address using IPinfo.io.
- **WHOIS Lookup**: Fetches WHOIS information for a given domain.
- **DNS Lookup**: Retrieves DNS records for a domain.
- **Directory Fuzzing & Document Finding**: Performs directory fuzzing to find hidden directories and files like `robots.txt`, `.git`, `.env`, etc.
- **Google Dorking**: Performs Google Dorking to search for vulnerable or exposed data using advanced Google search operators.
- **Email Scraping**: Extracts email addresses from a given URL.

## Installation

Before using the tool, you need to install the required dependencies. 

### Step 1: Clone the repository

```bash
git clone https://github.com/Ajay-Bommidi/OBNTATHLOS.git
cd OBNTATHLOS
Step 2: Install dependencies
Create a virtual environment (optional but recommended):

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
Then install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Step 3: Configuration
Modify the CONFIG dictionary in the script to set your IPinfo.io API key and output directory.
Step 4: Run the tool
Run the script:

bash
Copy code
python3 OBNTATHLOS.py
The tool will present an interactive menu to choose which OSINT operation to run.

Usage
Available options:
IPinfo.io Geolocation: Lookup geolocation for an IP address.
WHOIS Lookup: Get WHOIS information for a domain.
DNS Lookup: Get DNS records for a domain.
Directory Fuzzing & Document Finding: Perform directory fuzzing and find common files and directories.
Google Dorking: Run advanced Google dorks to find publicly exposed data.
Email Scraping: Scrape email addresses from a website.

Example Output
After running a WHOIS lookup, the tool will display WHOIS information for the provided domain.
Google Dorking results will display Google search URLs based on the selected dorks.
Directory fuzzing will reveal the discovered directories and documents if any are found.
