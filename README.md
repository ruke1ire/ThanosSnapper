# ThanosSnapper

![gif](https://github.com/ruke1ire/ThanosSnapper/blob/main/movie.gif "Thanos Snapper")

*"Independent rgb with division (refer to Usage)" with division = 10 was used for colored videos. Greyscale video also used division = 10.*

---

This project was created to fulfill my curiosity after a shower thought/hypothesis that:

> Moving objects from a stationary video can be erased by simply displaying the most frequently occuring pixel value for each pixel, or in other words, displaying the mode of the pixel value for each pixel.

## Usage

There are 3 implementations, each performing similar tasks but with small differences.

1. Black and white with division
    * Run the following command to get a black and white output (saves time)
    ~~~
    $ python3 background_extractor_bw_division.py <input video path/name> <output video path/name> <number of divisions> 
    ~~~
2. Independent rgb with division
    * Run the following command to get a RGB output 
    ~~~
    $ python3 background_extractor_rgb_division.py <input video path/name> <output video path/name> <number of divisions>
    ~~~
3. Dependent rgb with division
    * Run the following command to get a RGB output (most accurate but slow)
    ~~~
    $ python3 background_extractor_rgb_dependent_division.py <input video path/name> <output video path/name> <number of divisions>
    ~~~

**Dependencies**
- numpy 4.2.0
- opencv2 1.19.1

**NOTES**
- Currently the commands only work for 360,640 resolution videos. 
    - You can change the resolution by tweaking the values in *frameSize*, etc.

## Terms

- *Independent* : The mode for each channel (RGB) are calculated separately. Therefore the output pixel displays the combination of an RGB tuple found by getting the mode for each of the individual color channels.
- *Depndent* : The mode for each channel (RGB) are dependent to each other. Therefore the mode of an RGB tuple is calculated for each pixel.
- *Division* : The number of division to make for each channel. Each of the color channels will display resolutions of 256/division. Division = 1 for max resolution.

## Discussion

**Advantages**
- Easy concept to understand
- Fast rendering (independent)

**Disadvantages**
- Restricted to stationary videos
- Using full color resolution can prevent moving objects from disappearing

