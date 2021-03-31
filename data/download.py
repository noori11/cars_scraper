


def save_pdf(self, response):
        if 'PDF' in self.datatype:
            with open(f'{self.virksomhed}_aarsapport_{self.datatype}_{self.perioder}.pdf', 'wb') as f:
                f.write(response.body)  
        else:
            with open(f'{self.virksomhed}_aarsapport_{self.datatype}_{self.perioder}.xml', 'wb') as f:
                f.write(response.body)
