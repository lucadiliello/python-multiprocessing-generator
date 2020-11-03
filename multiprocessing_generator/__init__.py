import multiprocessing as mp

NCORE = mp.cpu_count()

# mainly taken by: https://stackoverflow.com/questions/43078980/python-multiprocessing-with-generator
def multiprocessing_generator(input_generator, heavy_function, *heavy_function_args, **heavy_function_kwargs):

    def gen_to_queue(input_q, lines):
        # This function simply consume our generator and write it to the input queue
        for line in lines:
            input_q.put(line)
        for _ in range(NCORE):    # Once generator is consumed, send end-signal
            input_q.put(None)

    def process(input_q, output_q):
        while True:
            line = input_q.get()
            if line is None:
                output_q.put(None)
                break
            res = heavy_function(line, *heavy_function_args, **heavy_function_kwargs)
            output_q.put(res)

    input_q = mp.Queue(maxsize=NCORE * 2)
    output_q = mp.Queue(maxsize=NCORE * 2)

    gen_pool = mp.Pool(1, initializer=gen_to_queue, initargs=(input_q, input_generator))
    pool = mp.Pool(NCORE, initializer=process, initargs=(input_q, output_q))

    finished_workers = 0
    while True:
        line = output_q.get()
        if line is None:
            finished_workers += 1
            if finished_workers == NCORE:
                break
        else:
            yield line
