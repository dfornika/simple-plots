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
        if args.binwidth != None:
            plot = sns.histplot(x=args.xvar, data=data, binwidth=args.binwidth)
        else:
            plot = sns.histplot(x=args.xvar, data=data)
    elif args.ymax != None:
        plot = sns.histplot(x=args.xvar, data=data)
        plot.set_ylim(args.ymin, args.ymax)
    elif args.xmax != None:
        if args.binwidth != None:
            plot = sns.histplot(x=args.xvar, data=data, binwidth=args.binwidth)
        else:
            plot = sns.histplot(x=args.xvar, data=data)
        plot.set_xlim(args.xmin, args.xmax)
    else:
        plot = sns.histplot(x=args.xvar, data=data)
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
    parser.add_argument('--ymin', type=float, default=0.0)
    parser.add_argument('--ymax', type=float)
    parser.add_argument('--binwidth', type=float)
    parser.add_argument('-o', '--output', default="plot.pdf")
    args = parser.parse_args()
    main(args)
