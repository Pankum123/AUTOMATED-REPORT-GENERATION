import csv
from fpdf import FPDF

# Step 1: Read data from a CSV file
def read_data(file_path):
    data = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Step 2: Analyze the data (example: find average value of a column)
def analyze_data(data, column_name):
    values = [float(row[column_name]) for row in data if row[column_name]]
    avg = sum(values) / len(values) if values else 0
    total = sum(values)
    count = len(values)
    min_value = min(values) if values else 0
    max_value = max(values) if values else 0
    return {
        "average": avg,
        "total": total,
        "count": count,
        "min": min_value,
        "max": max_value
    }

# Step 3: Generate a PDF Report
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Data Analysis Report', ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, title, ln=True)
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def generate_pdf_report(analysis_result, output_path):
    pdf = PDFReport()
    pdf.add_page()
    pdf.chapter_title('Analysis Summary')
    body = (f"Total Records: {analysis_result['count']}\n"
            f"Sum of Values: {analysis_result['total']:.2f}\n"
            f"Average Value: {analysis_result['average']:.2f}\n"
            f"Minimum Value: {analysis_result['min']:.2f}\n"
            f"Maximum Value: {analysis_result['max']:.2f}")
    pdf.chapter_body(body)
    pdf.output(output_path)

# Step 4: Main function
def main():
    file_path = 'data.csv'  # Input CSV file
    output_path = 'report.pdf'  # Output PDF file
    column_to_analyze = 'Amount'  # Column to analyze

    data = read_data(file_path)
    analysis_result = analyze_data(data, column_to_analyze)
    generate_pdf_report(analysis_result, output_path)
    print("PDF Report generated successfully as 'report.pdf'!")

if __name__ == "__main__":
    main()
