import math
import os
from PIL import Image
import sys

def calculateBrightness(r: int, g: int, b: int):
    brightness = (0.2126 * r + 0.7152 * g + 0.0722 * b)
    return brightness

def brightnessToAscii(brightness):
    rounded_brightness = math.floor(brightness)
    if rounded_brightness <= 255 and rounded_brightness >= 230:
        return " "
    elif rounded_brightness <= 229 and rounded_brightness >= 204:
        return "."
    elif rounded_brightness <= 203 and rounded_brightness >= 178:
        return ":"
    elif rounded_brightness <= 177 and rounded_brightness >= 152:
        return "-"
    elif rounded_brightness <= 151 and rounded_brightness >= 126:
        return "="
    elif rounded_brightness <= 125 and rounded_brightness >= 100:
        return "+"
    elif rounded_brightness <= 99 and rounded_brightness >= 74:
        return "*"
    elif rounded_brightness <= 73 and rounded_brightness >= 48:
        return "#"
    elif rounded_brightness <= 47 and rounded_brightness >= 22:
        return "%"
    elif rounded_brightness <= 21:
        return "@"
    
def writeLinesToFile(output_directory: str, lines: list, destination_path: str):    
    if os.path.exists(destination_path):
        os.remove(destination_path)

    file = open(destination_path, "x")
    file.writelines(lines)
    file.close()

def main():
    # get source file and output directory from args
    source_file = str(sys.argv[1])
    output_directory = str(sys.argv[2])

    if not os.path.exists(source_file):
        raise Exception("Source file doesn't exist")
    
    if not os.path.exists(output_directory):
        raise Exception("Ouput directory doesn't exist")
    
    # get output path
    file_name = os.path.basename(source_file)
    file_name = file_name.split(".")[0]
    file_name += ".txt"
    destination_path = os.path.join(output_directory, file_name)

    if os.path.exists(destination_path):
        delete_path = input("A similar file in the output exists, continuing will overwrite it, continue? (y/n):")
        if delete_path.lower() == 'n':
            print("Stopping script")
            return


    img = Image.open(source_file)
    pix = img.load()

    # get width and height to iterate through
    width, height = img.size
    print('width: ', width)
    print('height: ', height)

    # loop through every row of pixels making up image
    asciiLines = []
    for y in range(height):
        asciiStr = ""
        # loop through every pixel in row
        for x in range(width):
            # calculate brightness
            brightness = calculateBrightness(pix[x, y][0], pix[x, y][1], pix[x, y][2])
            # convert brightness to ascii value
            asciiValue = brightnessToAscii(brightness)
            # add ascii value to string
            asciiStr += asciiValue
        # write string of ascii values to file
        # currently just printing to console
        print(f"{y}: {asciiStr}")
        asciiStr += "\n"
        asciiLines.append(asciiStr)
        # clear string of ascii values for next iteration of loop
        asciiStr = ""

    # write ascii lines to file    
    writeLinesToFile(output_directory, asciiLines, destination_path)    

if __name__ == "__main__":
    main()




