from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # Add parent page
    pdf.add_page()

    # Set the Header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row["Topic"], align="L", ln=1)
    pdf.line(10,22,200,22)

    # Create lines on page

    for i in range(32,265,10):
        pdf.line(10, i, 200, i)

    # Set the Footer
    pdf.ln(275)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # Add a number of pages as stated in the CSV file
    for i in range(row["Pages"]-1):
        pdf.add_page()

        for num in range(32, 265, 10):
            pdf.line(10, num, 200, num)

        # Set the Footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")