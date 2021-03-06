# -*- coding: utf-8 -*-
import os
import sys
import copy
import random
import numpy as np
import torch
from torchvision import transforms
from .datasets import register_dataset
import utils


@register_dataset('Portrait')
class Portrait:
    """
    Portrait Dataset class
    """

    def __init__(self, name, img_dir, LDS_type, is_target):
        self.name = name
        self.img_dir = img_dir
        self.LDS_type = LDS_type
        self.is_target = is_target

    def get_data(self):
        mean, std = 0.5, 0.5
        normalize_transform = transforms.Normalize((mean,), (std,))

        self.train_transforms = transforms.Compose([
            transforms.Resize((256, 256)),
            transforms.RandomCrop((224, 224)),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            normalize_transform
        ])

        self.test_transforms = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            normalize_transform
        ])

        train_path = os.path.join('data/Portrait/txt/', '1901_1950.txt')
        test_path = os.path.join('data/Portrait/txt/', '1951_2000.txt')

        train_dataset = utils.ImageList(open(train_path).readlines(), self.img_dir)
        val_dataset = utils.ImageList(open(test_path).readlines(), self.img_dir)
        test_dataset = utils.ImageList(open(test_path).readlines(), self.img_dir)
        self.num_classes = 2

        train_dataset.targets, val_dataset.targets, test_dataset.targets = torch.from_numpy(train_dataset.labels), \
                                                                           torch.from_numpy(val_dataset.labels), \
                                                                           torch.from_numpy(test_dataset.labels)
        return self.num_classes, train_dataset, val_dataset, test_dataset, self.train_transforms, self.test_transforms
