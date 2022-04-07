#!/usr/bin/env python

import argparse

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main(args):
    sns.set_theme(style="whitegrid")
    data = pd.read_csv(args.dataset)
    if args.xmax == None and args.ymax == None:
        plot = sns.scatterplot(x=args.xvar, y=args.yvar, data=data)
    elif args.ymax != None:
        plot = sns.scatterplot(x=args.xvar, y=args.yvar, data=data)
        plot.set_ylim(args.ymin, args.ymax)
    elif args.xmax != None:
        plot = sns.scatterplot(x=args.xvar, y=args.yvar, data=data)
        plot.set_xlim(args.xmin, args.xmax)
    else:
        plot = sns.scatterplot(x=args.xvar, y=args.yvar, data=data)
        plot.set_xlim(args.xmin, args.xmax)
        plot.set_ylim(args.ymin, args.ymax)

    plt.tight_layout()
    plt.savefig(args.output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset')
    parser.add_argument('-x', '--xvar')
    parser.add_argument('--xmin', type=float, default=0.0)
    parser.add_argument('--xmax', type=float)
    parser.add_argument('-y', '--yvar')
    parser.add_argument('--ymin', type=float, default=0.0)
    parser.add_argument('--ymax', type=float)
    parser.add_argument('-o', '--output', default="plot.pdf")
    args = parser.parse_args()
    main(args)
