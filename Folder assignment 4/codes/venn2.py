
from matplotlib_venn import venn3
from matplotlib import pyplot as plt

venn3(subsets=(100,100,40,100,40,40,20),set_labels=('Event A','Event B','Event C')) 
 
 #assuming all events equally probabale according to the probabality level in 11 class .so equal weightage 
 
 
plt.show()