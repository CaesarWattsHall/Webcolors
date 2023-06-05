# This program prompts the user to enter RGB values separated by commas. 
# It then converts the input string into a tuple of integers and passes it to the get_color_name function. 
# This function uses the rgb_to_name function from the webcolors library to get the name of the color. 
# If the RGB values do not correspond to a known color name, it returns “Unknown”. 
# Finally, the program prints the name of the color.
#
#
# By: Caesar R. Watts-Hall
# June 05, 2023

import webcolors

def get_color_name(rgb):
    try:
        color_name = webcolors.rgb_to_name(rgb)
    except ValueError:
        color_name = "Unknown"
    return color_name

rgb = input("Enter RGB values separated by commas (e.g. 255,0,0): ")
rgb = tuple(map(int, rgb.split(",")))
color_name = get_color_name(rgb)
print(f"The color is: {color_name}")
