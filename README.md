# python-multiprocessing-generator
Easily process data from a generator in multicore and return another generator.

Example

```python

from multiprocessing_generator import multiprocessor_generator 

def heavy_work(main_argument, *args, **kwargs):
    return main_argument * 2

test_list = range(100)

heavy_work_args = []
heavy_work_kwargs = {}

res = multiprocessor_generator(test_list, heavy_work, *heavy_work_args, **heavy_work_kwargs)

for r in res:
    print(r)
```