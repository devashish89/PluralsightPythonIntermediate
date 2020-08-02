from urllib.request import urlopen
import cv2

response = urlopen("https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic")
data = response.read()
print(data.decode())

img = cv2.imread("ManagePackages.JPG")
cv2.imshow("Pip Commands", img)
cv2.waitKey(0)
cv2.destroyAllWindows()