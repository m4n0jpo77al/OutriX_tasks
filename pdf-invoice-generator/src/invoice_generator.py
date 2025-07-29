from fpdf import FPDF
from datetime import datetime
import os

class InvoiceGenerator:
    def __init__(self, client_name, invoice_number, items):
        self.client_name = client_name
        self.invoice_number = invoice_number
        self.items = items
        self.pdf = FPDF()
        self.total = 0

    def generate_invoice(self):
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)

        # Header
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(200, 10, "INVOICE", ln=True, align="C")

        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(100, 10, f"Client: {self.client_name}", ln=True)
        self.pdf.cell(100, 10, f"Invoice #: {self.invoice_number}", ln=True)
        self.pdf.cell(100, 10, f"Date: {datetime.now().strftime('%d-%m-%Y')}", ln=True)

        # Table headers
        self.pdf.ln(10)
        self.pdf.set_fill_color(220, 220, 220)
        self.pdf.cell(80, 10, "Description", 1, 0, 'C', True)
        self.pdf.cell(30, 10, "Qty", 1, 0, 'C', True)
        self.pdf.cell(40, 10, "Unit Price", 1, 0, 'C', True)
        self.pdf.cell(40, 10, "Total", 1, 1, 'C', True)

        # Table rows
        for item in self.items:
            total_price = item["qty"] * item["unit_price"]
            self.total += total_price
            self.pdf.cell(80, 10, item["description"], 1)
            self.pdf.cell(30, 10, str(item["qty"]), 1)
            self.pdf.cell(40, 10, f"Rs.{item['unit_price']:.2f}", 1)
            self.pdf.cell(40, 10, f"Rs.{total_price:.2f}", 1, 1)

        # Total
        self.pdf.ln(5)
        self.pdf.set_font("Arial", 'B', 12)
        self.pdf.cell(150, 10, "Grand Total", 1)
        self.pdf.cell(40, 10, f"Rs.{self.total:.2f}", 1, 1)

        # Save PDF
        os.makedirs("../invoices", exist_ok=True)
        filename = f"../invoices/{self.invoice_number}_{self.client_name.replace(' ', '_')}.pdf"
        self.pdf.output(filename)
        print(f"\n✅ Invoice saved as: {filename}")


# Get input from user
if __name__ == "__main__":
    print("📋 PDF Invoice Generator")

    client_name = input("Enter client name: ")
    invoice_number = input("Enter invoice number: ")
    
    items = []
    num_items = int(input("How many items? "))

    for i in range(num_items):
        print(f"\nItem {i + 1}:")
        description = input("  Description: ")
        qty = int(input("  Quantity: "))
        unit_price = float(input("  Unit Price (Rs.): "))
        items.append({
            "description": description,
            "qty": qty,
            "unit_price": unit_price
        })

    # Generate invoice
    generator = InvoiceGenerator(client_name, invoice_number, items)
    generator.generate_invoice()
