from fpdf import FPDF


def gen():
    with open('tekst.txt', 'r') as file:
        content = file.read()
        return content
#        print(content)


def pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Calibri', size = 15)
    for line in gen():
        pdf.cell(200, 10, txt = line, ln = 1, align = 'C')
    pdf.output('something.pdf')

if __name__ == '__main__':
    pdf()

'''
class DocGenInterface():
    def gen():
        with open('tekst.txt', r) as file:
            content = file.read()
            print(content)


class pdf(DocGenInterface):
    def gen(self):
        print(f'generating .pdf file')

class word(DocGenInterface):
    def gen(self):
        print('generating .doc file')

class DocGenFacotry():
    @staticmethod
    def get_gen(gen_str):
        method = {
            'word': word(),
            'pdf': pdf()
        }
        gen = method.get(gen_str)
        if gen == None:
            assert 0, f'Cannot convert to <{gen_str}> format'
        else:
            return gen


if __name__ == '__main__':
    g = DocGenFacotry()
    option = input('Enter document format: ')
    gen_option = g.get_gen(option)
    gen_option.gen()

'''