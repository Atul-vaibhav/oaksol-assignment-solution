<!--
<meta name="description" content="Smart AI model for predicting weather using ML techniques">
<meta name="keywords" content="weather forecast, AI model, temperature prediction, humidity, GitHub project">
-->

# OCR to MySQL Data Pipeline

## Overview
This project extracts text from images using OCR (Tesseract), structures the extracted data into JSON format, and stores it into a MySQL database.

## Technologies Used
- Python
- OpenCV
- Tesseract OCR
- MySQL
- JSON



## Setup Instructions
### 1. Install Dependencies
Ensure you have Python installed. Install required libraries:
```sh
pip install pytesseract opencv-python mysql-connector-python
```
Install Tesseract OCR and add it to the system PATH:
- Windows: [Download Here](https://github.com/UB-Mannheim/tesseract/wiki)
- Linux:
  ```sh
  sudo apt install tesseract-ocr
  ```

### 2. Run OCR Script
To extract text and structure it as JSON:
```sh
python extract_and_structure_image.py
```

### 3. Setup MySQL Database
Create the database and tables using:
```sh
mysql -u root -p < sql/schema.sql
```

### 4. Insert Extracted Data
Run the MySQL storage script:
```sh
python store_to_mysql.py
```

## Sample JSON Output
```json
{
  "Patient Name": "John Doe",
  "DOB": "01/05/1980",
  "Pain Level": 6,
  "Comments": "Not good"
}
```

## Contributing
Feel free to fork and improve the project. Submit a pull request for any enhancements.

## License
This project is licensed under the MIT License.

