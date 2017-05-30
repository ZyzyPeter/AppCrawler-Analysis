import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.pyplot import plot

fr1=pd.DataFrame({
    'a':list('abcd'),
    'b':list('afgb')
})
fr2=pd.DataFrame({
    'b':list('ab'),
    'c':[1,2]
})
print pd.merge(fr1,fr2)