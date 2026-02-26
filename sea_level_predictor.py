import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(15, 10))

    # Scatter plot with Year on x-axis and CSIRO Adjusted Sea Level on y-axis
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # First line of best fit (using all the data from 1880 to the most recent year)
    slope, intercept, r, p, se = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create line of best fit based on the slope and intercept
    years_extended = range(1880, 2051)  # Extend the years to 2050
    sea_level_line = [slope * year + intercept for year in years_extended]
    ax.plot(years_extended, sea_level_line, label='Best Fit Line (1880-2050)', color='blue')

    # Second line of best fit (using data from the year 2000 to the most recent year)
    df_2000_onwards = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_2000, p_2000, se_2000 = linregress(df_2000_onwards['Year'], df_2000_onwards['CSIRO Adjusted Sea Level'])
    
    # Create second line of best fit for years from 2000 to 2050
    years_2000_extended = range(2000, 2051)  # Extend the years from 2000 to 2050
    sea_level_line_2000 = [slope_2000 * year + intercept_2000 for year in years_2000_extended]
    ax.plot(years_2000_extended, sea_level_line_2000, label='Best Fit Line (2000-2050)', color='red')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Add legend
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()