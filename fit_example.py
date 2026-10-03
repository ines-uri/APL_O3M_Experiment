# # Sample Python code to run the fit_black_box Python code relatively easily

import fit_black_box as bb

# First, define the function you want to fit. Here it's a linear function.
# It is critical that the independant variable ("t") is first in the list of function variables.

def linear(t, m, b):
    return m*t + b


# Now load the data from the file. The file should be in the same directory as this Python code.
# Some chance you will need an absolute path: "C:\\Users\\Brian\\Python\\mydata_fake.txt"

filename="/Users/inesuriarte/Desktop/data7.txt"
x, y, xerr, yerr = bb.load_data(filename)

# This time, let's use every single possible option available to bb.plot_fit()

init_guess = (1.0, 0.0) # guess for the best fit parameters
font_size = 20
xlabel = "Weighted air mass"
ylabel = "ln(321.27_signal)"

# Now we make the plot, displayed on screen and saved in the directory, and print the best fit values
bb.plot_fit(linear, x, y, xerr, yerr, init_guess=init_guess, font_size=font_size,
            xlabel=xlabel, ylabel=ylabel)

# Note: for sinusoidal functions, guessing the period correctly with init_guess is critical

# Fit the same data with an exponential function

#bb.plot_fit(expon, x, y, xerr, yerr)

