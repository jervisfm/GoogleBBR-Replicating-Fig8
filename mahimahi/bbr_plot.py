#!/usr/bin/python
"""Module for creating all of the plots after the data has been gathered."""
from bbr_logging import debug_print, debug_print_verbose, debug_print_error
import csv
import matplotlib
from matplotlib import pyplot as plt


# Flag to control whether interactive plots should be shown.
SHOW_INTERACTIVE_PLOTS = False

def make_figure_8_plot(logfile):
    """Generate high quality plot of data to reproduce figure 8.

    The logfile is a CSV of the format [congestion_control, loss_rate, goodput, rtt, bandwidth]
    """
    cubic = {"loss": [], "goodput": []}
    bbr = {"loss": [], "goodput": []}
    xmark_ticks = []

    # For available options on plot() method, see: https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
    # We prefer to use explicit keyword syntax to help code readability.

    # Create a figure.
    fig_width = 8
    fig_height = 5
    fig, axes = plt.subplots(figsize=(fig_width, fig_height))

    # Add a subplot for CUBIC/BBR plots. See
    # https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.subplot
    # bbr_fig = fig.add_subplot(111)
    # cubic_fig = fig.add_subplot(111)

    with open(logfile, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()  # skip header row
        for (cc, loss, goodput, rtt, bandwidth) in reader:
            loss_percent = float(loss) * 100
            xmark_ticks.append(loss_percent)

            if cc == 'cubic':
                cubic['loss'].append(loss_percent)
                cubic['goodput'].append(goodput)
            elif cc == 'bbr':
                bbr['loss'].append(loss_percent)
                bbr['goodput'].append(goodput)

            else:
                debug_print_error("This shouldn't happen.")
    debug_print_verbose("CUBIC: %s" % cubic)
    debug_print_verbose("BBR: %s" % bbr)

    matplotlib.rcParams.update({'figure.autolayout': True})

    plt.plot(cubic['loss'], cubic['goodput'], color='blue', linestyle='solid', marker='o',
             markersize=7, label='CUBIC')

    plt.plot(bbr['loss'], bbr['goodput'], color='red', linestyle='solid', marker='x',
             markersize=7, label='BBR')

    plt.xscale('log')

    xmark_ticks = sorted([x for x in set(xmark_ticks)])  # deduplicate
    xmark_ticks.remove(25.0)
    xmark_ticks.remove(15.0)
    xmark_ticks.remove(40.0)

    # For each loss percent, set a mark on x-axis.
    axes.set_xticks(xmark_ticks)

    # Make the X-Axis label look vertical to make them more readable.
    axes.set_xticklabels(axes.xaxis.get_majorticklabels(),
                         rotation=90, fontsize=14)

    # Format the Y-Axis too
    axes.set_yticklabels(axes.yaxis.get_majorticklabels(), fontsize=14)

    axes.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    axes.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

    # Plot Graph tile and axis labels.
    # plt.title("ReBBR: Comparing CUBIC and BBR performance on lossy links")
    plt.ylabel("Goodput (Mbps)", size=20)
    plt.xlabel("Loss Rate (%) - Log Scale", size=20)

    # Plot Graph legend
    plt.legend(loc='upper right', fontsize=20)
    plt.tight_layout()

    # Save the figure first.
    plt.savefig("figure8.png")
    # May be show the figure interactively
    if SHOW_INTERACTIVE_PLOTS:
        plt.show()


def main():
    debug_print_verbose('Generating Plots')
    make_figure_8_plot('data/figure8_experiment.csv')
    #make_experiment1_plot('data/experiment1.csv')
    #make_experiment2_plot('data/experiment2.csv')
    #make_experiment3_plot('data/expeirment3.csv')

    # TODO(jmuindi): Add plot for experiment 4 (testing against verizon cellular link)
    # when we have data collection for it.
                          

if __name__ == '__main__':
    main()
