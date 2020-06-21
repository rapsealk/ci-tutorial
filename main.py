#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import numpy as np


def is_qualified(scores):
    """
    다섯 과목의 점수를 전달받아 시험 합격 여부를 결정합니다.
    * 합격 조건:
        1. 모든 과목의 평균이 60점 이상이어야 한다.
    """
    return np.mean(scores) >= 60


if __name__ == "__main__":
    pass
