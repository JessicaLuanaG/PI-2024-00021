class DataHora:
    pass

import unittest

class testDataHora(unittest.TestCase):
    
   def setUp(self):
       self.dh1 = DataHora(ano=2019,mes=2,dia=28,hora=12,min=30,seg=12)
       self.dh2 = DataHora(ano=2020,mes=8,dia=5,hora=0,min=30,seg=12)
       self.dh3 = DataHora(ano=1976,mes=2,dia=29,hora=0,min=30,seg=12)
       self.dh4 = DataHora(ano=2020,mes=8,dia=31,hora=0,min=30,seg=12)
       self.dh5 = DataHora(ano=2020,mes=6,dia=30,hora=0,min=30,seg=12)

    def test_data_hora_fevereiro(self):
        self.assertEqual(self.retorna_data(self.dh1(), 2019,2,28,12,30,12))
        
    def test_data_hora_normal(self):
        self.assertEqual(self.retorna_data(self.dh2(), 2020,8,5,0,30,12))

    def test_data_hora_bissexto(self):
        self.assertEqual(self.retorna_data(self.dh3(), 1976,2,29,0,30,12))
        
    def test_data_hora_ultimo_dia_agosto(self):
        self.assertEqual(self.retorna_data(self.dh4(), 2020,8,31,0,30,12))
        
    def test_data_hora_ultimo_dia_junho(self):
        self.assertEqual(self.retorna_data(self.dh5(), 2020,6,30,0,30,12))
        
    
    
    
    
   
