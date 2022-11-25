from texttable import Texttable
import cv2
import numpy as np
import matplotlib.pyplot as plt

start = 88 #last 2 digits of the first image
images = [f"IMG_07{start+i}.jpg" for i in range(10)]
total_pixels = 3024*4032

avg_pixel_values = []
pixel_values = []

for img in images:
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    
    #calculating individual pixel
    pixel = image[1552, 1958]
    pixel_values.append(pixel)

    #calculating average intensity of all the pixels
    pixels = image[0:3024, 0:4032].tolist()
    flat_pixels = [
        value for sublist in pixels for value in sublist if value != 0]
    avg = sum(flat_pixels)/total_pixels
    print(f"avg: {avg}")
    avg_pixel_values.append(avg)

#data calculations
angles = [i*10 for i in range(10)]
normalized_value = [(value - min(pixel_values))/(max(pixel_values) -
                                           min(pixel_values)) for value in pixel_values]
normalized_avg = [(value - min(avg_pixel_values))/(max(avg_pixel_values) -
                                           min(avg_pixel_values)) for value in avg_pixel_values]

#output data in tabular format
t = Texttable()
rows = [[angle, pixel_values[idx], normalized_value[idx], avg_pixel_values[idx], normalized_avg[idx]]
        for (idx, angle) in enumerate(angles)]

rows.insert(0, ["θ", "Intensity Estimate (Pixel Value))","Normalized(I0-I90)", "Average Intensity Value", "Normalized Average"])
t.add_rows(rows)
print(t.draw())

#plot data
plt.xlabel("Degree")
plt.ylabel("Normalized Intensity")
plt.xticks(np.arange(0, 100, 10))
plt.scatter(angles, normalized_value, label='Pixel')
plt.scatter(angles, normalized_avg, label='Average')
plt.legend()
plt.show()


