
# 🗂️ RTC Land Records Tracker

This is a Django-based full-stack application that extracts and analyzes property ownership and crop season data from RTC (Record of Rights, Tenancy, and Crops) documents. The project uses OCR, LLM API integration, and web scraping to automate the processing of land records.

---

## 🚀 Features

- 🔍 **OCR with Tesseract** – Extract Kannada text from scanned RTC images.
- 🧠 **LLM Integration** – Use Gemini Pro to extract ownership and crop season details from raw OCR output.
- 🌐 **Web Scraping** – Automate data extraction of missing RTC years from the Karnataka Land Records portal using Selenium.
- 📊 (Upcoming) **Web Interface** – Unified web UI for uploading, processing, and displaying extracted data.

---

## 🛠️ Tech Stack

| Component      | Tool / Library              |
|----------------|-----------------------------|
| Backend        | Django, PostgreSQL          |
| OCR            | Tesseract, Pillow, OpenCV   |
| LLM Integration| Gemini Pro API              |
| Web Scraping   | Selenium, ChromeDriver      |
| Frontend (Planned) | HTML, CSS, JS (TBD)     |


---

## 🖼️ Sample Flow

1. Upload RTC image → OCR extracts Kannada text  
2. OCR output sent to LLM → Structured ownership & crop info returned  
3. If year is missing → Scraping fetches missing data from official site  

---

## 📝 To Do

- [</] OCR Extraction  
- [</] LLM Integration  
- [</] Basic Web Scraper  
- [ ] Web UI Integration  
- [ ] Display data in browser  

---

## 🙏 Acknowledgements

Thanks to **TitleWize** for the opportunity to work on this project. Through this assessment, I got to explore and learn about OCR, LLMs, and web scraping — all of which were new to me. This has been a great hands-on learning experience.
