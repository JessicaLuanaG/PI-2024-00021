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

def diff_data(data1, data2) -> DataHora:
    return DataHora(0, 0, 0, 0, 0, 0)

import unittest

class testDataHora(unittest.TestCase):
    def setUp(self):
       #Datas inválidas
       self.dh1 = DataHora(ano=2019,mes=2,dia=30,hora=12,min=30,seg=12)
       self.dh2 = DataHora(ano=2020,mes=6,dia=31,hora=0,min=30,seg=12)
       self.dh3 = DataHora(ano=2023,mes=2,dia=29,hora=0,min=30,seg=12)
       self.dh4 = DataHora(ano=2020,mes=8,dia=31,hora=0,min=61,seg=12)
       self.dh5 = DataHora(ano=2020,mes=6,dia=30,hora=0,min=30,seg=61)
       self.dh6 = DataHora(ano=2020,mes=6,dia=30,hora=25,min=30,seg=61)
       #Fazer o setup também de datas válidas, dá para pegar do histórico de commits
       self.dh7 = DataHora(ano=2020,mes=6,dia=30,hora=0,min=0,seg=0, fuso=0)
       self.dh8 = DataHora(ano=2020,mes=6,dia=29,hora=0,min=0,seg=0, fuso=0)
       self.dh9 = DataHora(ano=2026,mes=6,dia=29,hora=0,min=0,seg=0, fuso=0)
       self.dh10 = DataHora(ano=2026,mes=10,dia=29,hora=0,min=0,seg=0, fuso=0) 
       self.dh11 = DataHora(ano=2026,mes=10,dia=29,hora=12,min=0,seg=0, fuso=0)  
       self.dh12 = DataHora(ano=2026,mes=10,dia=29,hora=0,min=25,seg=0, fuso=0)     
    

    def test_valida_data(self):
        self.assertFalse(valida_data(self.dh1))
        self.assertFalse(valida_data(self.dh2))
        self.assertFalse(valida_data(self.dh3))
        self.assertFalse(valida_data(self.dh4))
        self.assertFalse(valida_data(self.dh5))
        self.assertFalse(valida_data(self.dh6))
        self.assertTrue(valida_data(self.dh7))
        self.assertTrue(valida_data(self.dh8))
        self.assertTrue(valida_data(self.dh9))
        self.assertTrue(valida_data(self.dh10))
        self.assertTrue(valida_data(self.dh11))
        self.assertTrue(valida_data(self.dh12))
    
    def test_converter_fuso(self):
        self.assertEqual(converter_fuso(self.dh7, -3), DataHora(ano=2020,mes=6,dia=29,hora=21,min=0,seg=0))
        self.assertEqual(converter_fuso(self.dh7, +5), DataHora(ano=2020,mes=6,dia=29,hora=5,min=0,seg=0))
        self.assertEqual(converter_fuso(self.dh7, -1), DataHora(ano=2020,mes=6,dia=29,hora=23,min=0,seg=0))
        self.assertEqual(converter_fuso(self.dh7, 0), DataHora(ano=2020,mes=6,dia=29,hora=0,min=0,seg=0))
        self.assertEqual(converter_fuso(self.dh7, +4), DataHora(ano=2020,mes=6,dia=29,hora=4,min=0,seg=0))
    
    def test_diff_data(self):
        self.assertEqual(diff_data(self.dh7, self.dh8), DataHora(ano=0, mes=0, dia=1, hora=0, min=0, seg=0))
        self.assertEqual(diff_data(self.dh8, self.dh9), DataHora(ano=6, mes=0, dia=0, hora=0, min=0, seg=0))
        self.assertEqual(diff_data(self.dh9, self.dh10), DataHora(ano=0, mes=4, dia=0, hora=0, min=0, seg=0))
        self.assertEqual(diff_data(self.dh10, self.dh11), DataHora(ano=0, mes=0, dia=0, hora=12, min=0, seg=0))
        self.assertEqual(diff_data(self.dh11, self.dh12), DataHora(ano=0, mes=0, dia=0, hora=0, min=25, seg=0))
    
    def test_soma_datas(self):
        self.assertEqual(self.dh10 + self.dh11, DataHora(ano=2153, mes=8, dia=28, hora=12, min=0, seg=0))
        self.assertEqual(self.dh7 + self.dh11, DataHora(ano=2047, mes=4, dia=30, hora=12, min=0, seg=0))
        self.assertEqual(self.dh9 + self.dh10, DataHora(ano=2053, mes=4, dia=28, hora=0, min=0, seg=0))
        self.assertEqual(self.dh11 + self.dh12, DataHora(ano=2058, mes=8, dia=28, hora=12, min=25, seg=0))
        self.assertEqual(self.dh8 + self.dh12, DataHora(ano=2047, mes=7, dia=27, hora=0, min=25, seg=0))
    def test_subtracao_datas(self):
        self.assertEqual(self.dh11 - self.dh10, DataHora(ano=0, mes=0, dia=0, hora=12, min=0, seg=0))

if __name__ == '__main__':
    unittest.main()