#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import unittest

import numpy as np

from main import is_qualified


class Test(unittest.TestCase):

    def test_qualification(self):
        # 평균 70점이므로 시험에 합격한다.
        scores = np.array([80, 30, 80, 90, 70])
        self.assertTrue(is_qualified(scores))
        # 평균 20점이므로 시험에 불합격한다.
        scores = np.array([20, 30, 40, 10, 0])
        self.assertFalse(is_qualified(scores))


if __name__ == "__main__":
    unittest.main()
