class DataHora:
    def __init__(self, ano, mes, dia, hora, min, seg, fuso=0):
        self.ano = ano
        self.mes = mes
        self.dia = dia
        self.hora = hora
        self.min = min
        self.seg = seg
        self.fuso = fuso
    def __add__(self, other):
        pass
    def __sub__(self, other):
        pass

def valida_data(data):
    pass

def converter_fuso(data, novo_fuso):
    pass

def diff_data(data1, data2):
    pass

import unittest

class testDataHora(unittest.TestCase):
    def setUp(self):
       self.dh1 = DataHora(ano=2019,mes=2,dia=30,hora=12,min=30,seg=12)
       self.dh2 = DataHora(ano=2020,mes=6,dia=31,hora=0,min=30,seg=12)
       self.dh3 = DataHora(ano=2023,mes=2,dia=29,hora=0,min=30,seg=12)
       self.dh4 = DataHora(ano=2020,mes=8,dia=31,hora=0,min=61,seg=12)
       self.dh5 = DataHora(ano=2020,mes=6,dia=30,hora=0,min=30,seg=61)
       self.dh6 = DataHora(ano=2020,mes=6,dia=30,hora=25,min=30,seg=61)
    
    def test_valida_data(self):
        self.assertFalse(valida_data(self.dh1))
        self.assertFalse(valida_data(self.dh2))
        self.assertFalse(valida_data(self.dh3))
        self.assertFalse(valida_data(self.dh4))
        self.assertFalse(valida_data(self.dh5))
        self.assertFalse(valida_data(self.dh6))
    
    def test_converter_fuso(self):
        pass

    def test_diff_data(self):
        pass

    def test_soma_datas(self):
        pass

    def test_subtracao_datas(self):
        pass

if __name__ == '__main__':
    unittest.main()