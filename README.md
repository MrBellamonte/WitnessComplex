# Witness Complex

## Installation 

```bash
git clone https://github.com/MrBellamonte/WitnessComplex
cd WitnessComplex
pip --no-cache-dir install -r requirements.txt
python setup.py install
```

## Usage

The module has two functionalities
- Computation of filtration values for all landmark pairs (i.e. the entire 1-skeleton)
- Computation of a simplicial complex (computes a simplex_tree from ghudi)

Note: The computation of the simplicial complex is rather inefficient at this point.

### Example

```python
import torch

from witnesscomplex.simplicial_complex import WitnessComplex

witnesses = torch.randn((100,2))
landmarks = witnesses[:20,:]

#computation of filtration values of 1-simplicies (recommended if that is the only thing needed)
wc1 = WitnessComplex(landmarks,witnesses)
wc1.compute_metric_optimized(n_jobs=2)


# computation of a simplicial complex (only recommended if more then 1-simplicies are needed or one is interested in a persistence diagram)
wc2 = WitnessComplex(landmarks,witnesses)
wc2.compute_simplicial_complex(d_max=2,create_simplex_tree=True,create_metric=True,n_jobs=2)
simplex_tree = wc2.simplex_tree #how to retrieve the simplex_tree
wc2.get_diagram(show=True,path_to_save=None) # allows to directly plot a persistence diagram
```
