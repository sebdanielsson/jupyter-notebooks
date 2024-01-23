# GIK2Q3 - Group 1 - Assignment 1

## Group members

- Jesper Andersson
- Jeanette Bergström
- Sebastian Danielsson
- Mikael Eriksson
- Marcus Lowén
- Emelie Persson

## How to run

### Add a dataset

In our run we used the 1.7 GB dataset from Gutenberg database.  <https://zenodo.org/records/3360392>

Place the text files in a directory called `dataset` placed adjacent to the `serial.py` and `parallel.py` files.

### Run the scripts

In a bash shell run the following commands:

```bash
time python3 serial.py
time python3 parallel.py
```

In a powershell run the following commands:

```powershell
(Measure-Command {python serial.py}).TotalSeconds
(Measure-Command {python parallel.py}).TotalSeconds
```

## Results

### Serial

```bash
$ time python3 serial.py
        Word   Count
0        The  854150
1    Project  197245
2  Gutenberg   55869
3     eBook,    2758
4     Within    3266
python3 serial.py  47.00s user 1.44s system 98% cpu 48.992 total
```

### Parallel

```bash
$ time python3 parallel.py
        Word   Count
0        The  854150
1    Project  197245
2  Gutenberg   55869
3     eBook,    2758
4     Within    3266
python3 parallel.py  72.40s user 5.60s system 274% cpu 28.428 total
```

## Discussion

By running the scripts using the `time` command we can see that the parallel script is about ***72% faster*** than the serial script. The parallel script is faster because it uses multiple threads to count the words in the text files. The serial script uses only one thread to count the words in the text files.

Initially we used a much smaller dataset and the parallel script was about as fast as the serial script. This is might be because the overhead of creating the threads didn't pay off when the dataset was small since the full run was about 1 second. When we used the larger dataset the parallel script was much faster than the serial script as we can see in the results above.
