# 🌍 Rest Countries Data Fetcher

This project fetches country data from the **REST Countries API**, processes it, and saves the results into both **JSON** and **CSV** formats.

---

## 🚀 Features

* Fetches data from a public API
* Implements **retry strategy** for reliability
* Handles **timeouts and request errors**
* Extracts and formats:

  * Country name (common & official)
  * Capital city
  * Languages
  * Population
  * Currency (name & symbol)
* Saves data into:

  * `restcountries.json`
  * `restcountries.csv`

---

## 🛠️ Technologies Used

* Python
* `requests`
* `json`
* `csv`
* `urllib3` (Retry strategy)

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/restcountries-fetcher.git
cd restcountries-fetcher
```

2. Install dependencies:

```bash
pip install requests
```

---

## ▶️ Usage

Run the script:

```bash
python your_script_name.py
```

---

## ⚙️ How It Works

1. A session is created using `requests.Session()`
2. A retry strategy is applied:

   * Retries failed requests up to 3 times
   * Handles common server errors (500, 502, 503, etc.)
3. Data is fetched from:

```
https://restcountries.com/v3.1/all?fields=name,capital,languages,population,currencies
```

4. The script safely extracts:

   * Nested JSON fields
   * Optional/missing values (fallback to `"N/A"`)

5. Processed data is stored in a list of dictionaries

6. Output files are generated:

   * JSON (structured format)
   * CSV (tabular format)

---

## 📁 Output Example

### JSON

```json
{
  "name": "Serbia",
  "official": "Republic of Serbia",
  "currency_name": "Serbian dinar",
  "currency_symbol": "дин.",
  "languages": "Serbian",
  "capital": "Belgrade",
  "population": 6908224
}
```

### CSV

```
name,official,currency_name,currency_symbol,languages,capital,population
Serbia,Republic of Serbia,Serbian dinar,дин.,Serbian,Belgrade,6908224
```

---

## ⚠️ Error Handling

* Handles request timeouts (`timeout=5`)
* Retries failed requests automatically
* Uses try/except blocks for:

  * Data parsing
  * File writing



## 📄 License

This project is open-source and free to use.

---

## 👨‍💻 Author

Created for learning and practicing API handling in Python.
