from matplotlib_venn import venn2
from matplotlib import pyplot as plt

venn2(subsets=(100,100,30),set_labels=('Event A','Event B')) 
 
plt.show()
