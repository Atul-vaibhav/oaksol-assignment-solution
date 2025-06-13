import pytesseract
import json
from PIL import Image
import sys

def main(image_path="image.png"):
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: Image file '{image_path}' not found.")
        return

    extracted_text = pytesseract.image_to_string(image)

    structured_data = {
        "patient_name": "Unknown",
        "dob": "2000-01-01",  # Use ISO format for DB
        "pain_ratings": {},
        "comments": {}
    }

    from datetime import datetime

    lines = extracted_text.split("\n")
    for line in lines:
        if "Patient Name" in line:
            structured_data["patient_name"] = line.split(":")[-1].strip()
        elif "DOB" in line:
            dob = line.split(":")[-1].strip()
            # Try to parse date into YYYY-MM-DD
            for fmt in ("%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d"):
                try:
                    dob = datetime.strptime(dob, fmt).strftime("%Y-%m-%d")
                    break
                except ValueError:
                    continue
            structured_data["dob"] = dob
        elif "Pain" in line:
            structured_data["pain_ratings"]["Pain"] = line.split(":")[-1].strip()
        elif "Numbness" in line:
            structured_data["pain_ratings"]["Numbness"] = line.split(":")[-1].strip()
        elif "Tingling" in line:
            structured_data["pain_ratings"]["Tingling"] = line.split(":")[-1].strip()
        elif "Burning" in line:
            structured_data["pain_ratings"]["Burning"] = line.split(":")[-1].strip()
        elif "Tightness" in line:
            structured_data["pain_ratings"]["Tightness"] = line.split(":")[-1].strip()
        elif "Describe any functional changes" in line:
            structured_data["comments"]["Functional Changes"] = line.split(":")[-1].strip()

    json_file_path = "structured_data.json"
    with open(json_file_path, "w") as json_file:
        json.dump(structured_data, json_file, indent=4)

    print(f"Structured data saved to {json_file_path}")

if __name__ == "__main__":
    img_path = sys.argv[1] if len(sys.argv) > 1 else "image.png"
    main(img_path)
