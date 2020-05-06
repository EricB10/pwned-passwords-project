import numpy as np
import pandas as pd

import math
import hashlib

import pickle


# Function to return the SHA-1 hash of a string
def SHA_1(string):
    return hashlib.sha1(string.encode()).hexdigest().upper()