import progressbar
import time

if __name__ == "__main__":

    bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
    for i in range(1000):
        time.sleep(0.1)
        bar.update(i)
