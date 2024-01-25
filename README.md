## Setup

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Commands

To estimate the chance you will develop schizophrenia if your identical twin has been diagnosed, run:
```bash
python twin_est.py
```
Similarly, to estimate the number of children who will develop schizophrenia if neither of their parents have been diagnosed, run:
```bash
python next_gen_est.py
```
You can run the simulations using different parameters. To see the options, add `--help` to the end of the command. E.g.,
```bash
python twin_est.py --help
```