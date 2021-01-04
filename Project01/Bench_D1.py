#!/usr/bin/python3

import pandas as pd
import matplotlib as plt
import numpy as np

fulldata = pd.read_csv("Benchmarking_Dataset.csv", index_col="Source")
print(fulldata)
