#!/usr/bin/python3

import pandas as pd
import matplotlib as plt
import numpy as np

#read the absorption wavelengths (in nanometers) dataset for various organic dyes
fulldata = pd.read_csv("Benchmarking_Dataset.csv", index_col ="Source").T

#define the terms: experimental, functionals and errors
functionals= fulldata[[column for column in fulldata.columns if column!="Experimental"]].astype(float)
experimental =  fulldata["Experimental"].astype(float)
errors = pd.DataFrame(index=functionals.index, columns=functionals.columns)

#calculate the original absorption wavelength error dataset for all the functionals w.r.t experimental
for f in functionals:
    error = abs(functionals[f]- experimental)
    errors.loc[:,f] = error
    errors.to_csv("Original_Absolute_Error_Dataset.csv")