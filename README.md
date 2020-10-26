# ThanosSnapper

![gif](https://github.com/ruke1ire/ThanosSnapper/blob/main/movie.gif "Thanos Snapper")

This project was created to fulfill my curiosity after a shower thought/hypothesis that:

> Moving objects from a stationary video can be erased by simply displaying the most frequently occuring pixel value for each pixel, or in other words, displaying the mode of the pixel value for each pixel.

### Usage

There are 3 implementations, each performing similar tasks but with small differences.

1. black and white with division
    * Run the following command to get a black and white output (saves time)
    ~~~
    $ python3 background_extractor_bw_division.py <input video path/name> <output video path/name> <number of divisions> 
    ~~~
2. independent rgb with division
    * Run the following command to get a RGB output
    ~~~
    $ python3 background_extractor_rgb_division.py <input video path/name> <output video path/name> <number of divisions>
    ~~~
3. dependent rgb with division
    * Run the following command to get a RGB output
    ~~~
    $ python3 background_extractor_rgb_dependent_division.py <input video path/name> <output video path/name> <number of divisions>
    ~~~

### Specifics

- *Independent* : The mode for each channel (RGB) are calculated separately.
- *Depndent* : The mode for each channel (RGB) are dependent to each other.
- *Division* : The number of division to make for each channel. Each channel will resolution of 256/division. Division = 1 means true color.
