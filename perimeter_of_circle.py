#!/usr/bin/env python3

# Created by Donggeun Lim
# Created on November 2020
# This program calculates the area and perimeter of a circle
# with radius 15mm

import math


def main():
    print("If a circle has a radius of 15mm:")
    print("")
    print("Area is {}mm²".format(math.pi*15**2))
    print("perimeter is {}mm".format(2*math.pi*15))


if __name__ == "__main__":
    main()
