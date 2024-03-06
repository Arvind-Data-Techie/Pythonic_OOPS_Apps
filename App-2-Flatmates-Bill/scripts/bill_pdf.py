from fpdf import FPDF
import os
pdf = FPDF(orientation='P',unit='pt',format='A4')

image_path = os.path.join(os.path.dirname(__file__), '..', 'files', 'house.png')

class Pdfreport:
    """
    Object to generate pdf, and host the URL
    """

    def __init__(self, filename):
        self.filename = filename

    def generate_pdf(self, flatmate1, flatmate2, bill):
        pdf.add_page()

        pdf.image(image_path,w=30,h=30)
        pdf.set_font('Times', size=20, style="B")
        pdf.cell(w=0, h=60, txt='Flatmate Bill', border=1, align='C', ln=1)

        pdf.set_font('Times', size=10, style="B")
        pdf.cell(w=80, h=50, txt="Total Bill :", border=0)
        pdf.cell(w=50, h=50, txt=str(bill.amount)+'$', border=0, ln=1)

        pdf.set_font('Times', size=10, style="B")
        pdf.cell(w=80, h=20, txt="Month :", border=0)
        pdf.cell(w=50, h=20, txt=str(bill.period), border=0, ln=1)

        pdf.set_font('Times', size=10)
        pdf.cell(w=80, h=45, txt='Arvind Stay :  ', border=0)
        pdf.cell(w=50, h=45, txt=str(flatmate1.days_in_house)+' days', border=0, ln=1)

        pdf.cell(w=80, h=-15, txt='Roshini Stay :', border=0)
        pdf.cell(w=50, h=-15, txt=str(flatmate2.days_in_house)+' days', border=0, ln=1)

        pdf.cell(w=80, h=65, txt='Arvind Bill :', border=0)
        pdf.cell(w=15, h=65, txt=str(round(flatmate1.pay_bill(bill,flatmate2),2))+'$', border=0, ln=1)


        pdf.cell(w=80, h=-35, txt='Roshini Bill :', border=0)
        pdf.cell(w=15, h=-35, txt=str(round(flatmate2.pay_bill(bill,flatmate1),2))+'$', border=0)
        pdf.output(self.filename, 'F')