import unittest
from Model import IrisModel, IrisSpecies


class TestIrisModel(unittest.TestCase):
   def test_model_initialization(self):
       new_model = IrisModel()
       self.assertIn('iris_model.joblib',new_model.model_fname_)
