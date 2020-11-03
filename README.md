# python-multiprocessing-generator
Easily process data from a generator in multicore and return another generator.

## Install

```bash
pip install git+https://github.com/lucadiliello/python-multiprocessing-generator --upgrade
```

## Example

```python
from multiprocessing_generator import multiprocessing_generator 

# define the function that will do the heavy work
# the first argument will be sourced from the generator list
# the others will be 'static' and passed directly from the call below
def heavy_work(main_argument, *args, **kwargs):
    return main_argument * 2

# input generator
test_list = range(100)

# eventual other arguments used by the `heavy_work` function
heavy_work_args = []
heavy_work_kwargs = {}

# call the generator
res = multiprocessing_generator(test_list, heavy_work, *heavy_work_args, **heavy_work_kwargs)

# consume the output
for r in res:
    print(r)
```
