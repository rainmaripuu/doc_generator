class DocGenInterface():
    def gen():
        pass

class pdf(DocGenInterface):
    def gen(self):
        print('generating .pdf file')

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