## Motivation

This repo is in response to Scott Alexander's post titled [Some Unintuitive Properties of Polygenic Disorders](https://www.astralcodexten.com/p/some-unintuitive-properties-of-polygenic). In this post, Scott points out some limitations of the model he uses:
> A better model would have to take into account that people’s children aren’t clones of themselves, and that children’s environment is correlated with their parents’.

The model in this repo addresses both points. This isn't novel work, but a variation of the model we use at Orchid to [estimate disease risk reduction using embryo screening](https://portal.orchidhealth.com/risk-calculator),    

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