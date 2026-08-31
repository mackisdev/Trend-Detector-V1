# Trend Detector Version 1:

  This project's purpose is to track keywords within the top 50 titles for the top 50 videos on YouTube.
The reason I decided to make this project is that I am immersed in the idea of making tools that can
increase productivity within a creator's workflow. This tool is a prototype that will be improved upon,
and it'll be mainly used by content creators and SEO analysts. 
  This trend detector is able to read the content from YouTube's API, YouTube Data API v3. I will be specifically
tracking the top 50 titles and parsing them into a snapshot. The snapshot contains the timestamp the snapshot
was taken from and the separated words alongside their counts. These snapshots will be recorded every hour
to ensure that there isn't redundancy in the amount of data I am pulling, and so I can give the algorithm
the proper time to shift. Afterward, I will average the counts of the previous iteration of each specific word. If the
latest iteration of a word is 2 times the average, and it appeared over 5 times in the data, it will alert that this
is a trending topic.

## Limitations and Version 2 Roadmap:
  The limitations of this project are that at this moment, using 'mostPopular' can be a lagging indicator because it 
captures videos that are already very popular, 50 videos may be a small sample size, and it averages out the entire history
instead of only a window. This specific issue can cause the program to slow down if it is run over a long period of time
due to the massive amounts of information to average out.
