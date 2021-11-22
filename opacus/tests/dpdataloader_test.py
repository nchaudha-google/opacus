import unittest
from typing import Optional

import torch
import torch.nn as nn
from opacus import PrivacyEngine
from opacus.data_loader import DPDataLoader, switch_generator
from opacus.grad_sample import GradSampleModule
from opacus.optimizers import DPOptimizer
from torch.utils.data import DataLoader, TensorDataset, Sampler


class DPDataLoaderTest(unittest.TestCase):
    def setUp(self):
        self.data_size = 10
        self.dimension = 7
        self.num_classes = 11

    # def test_collate_classes(self):
    #     x = torch.randn(self.data_size, self.dimension)
    #     y = torch.randint(low=0, high=self.num_classes, size=(self.data_size,))
        
    #     dataset = TensorDataset(x, y)
    #     data_loader = DPDataLoader(dataset, sample_rate=1e-5)

    #     x_b, y_b = next(iter(data_loader))
    #     self.assertEqual(x_b.size(0), 0)
    #     self.assertEqual(y_b.size(0), 0)


    def test_collate_tensor(self):
        x = torch.randn(self.data_size, self.dimension)
        
        dataset = TensorDataset(x)
        data_loader = DPDataLoader(dataset, sample_rate=1e-5)

        s = next(iter(data_loader))
        print(s)
        self.assertEqual(s.size(0), 0)
