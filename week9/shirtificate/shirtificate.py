from fpdf import FPDF

class PDF(FPDF):
    # instantiating FPDF object and creating a page
    def __init__(self, name):
        self.name = name
        self._pdf = FPDF()
        self._pdf.add_page()

    # heading function to create title of page
    def header(self):
        self._pdf.set_font("helvetica", "B", 40)
        self._pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

    # main function to insert image and text
    def main(self):
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=47.5, y=140, text=f"{self.name} took CS50")

    # save function to save pdf
    def save(self):
        self._pdf.output("shirtificate.pdf")

def main():
    # taking user name
    name = input("Name: ")

    # instantiating PDF object and creating pdf
    pdf = PDF(name)
    pdf.header()
    pdf.main()
    pdf.save()

if __name__ == "__main__":
    main()
