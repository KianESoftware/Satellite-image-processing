# Satellite-image-processing
Querying, Accessing, downloading satellite images using APIs and performing basic processing operations using OpenCV. 

in this repository SentinelHub Process API is used to access and retrieve Sentinel2-L2A RGB images.Next basic image processing operations are applied using OpenCV. All steps are explained step by step. 

1) Accessing and downloading the satellite image
   
   1.1 importing libraries
   
   1.2 determining the area of interest
   
   1.3 Configuring the eval script

   1.4 Making Request

   1.5 Downloading Data
   
3) Perform image processing

 

### 1.1) importing libraries

```
import sentinelhub
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from sentinelhub import SHConfig, SentinelHubRequest, DataCollection, BBox, bbox_to_dimensions, constants, MimeType
import matplotlib
```


### 1.2) Determining the area on interest 

```
bbox = BBox(bbox=[
  -93.757492,
  34.502784,
  -93.45514,
  34.728822
], crs=sentinelhub.CRS.WGS84)
betsiboka_size = bbox_to_dimensions(bbox, resolution=resolution)
print(f"Image shape at {resolution} m resolution: {betsiboka_size} pixels")
```

### 1.3) Configuring the eval script 

```
evalscript_true_color = """
    //VERSION=3

    function setup() {
        return {
            input: [{
                bands: ["B04", "B03", "B02"]  # determining the bands R(Red = B04) G(Green=B03) B(Blue=B02)
            }],
            output: {
                bands: 3
            }
        };
    }

    function evaluatePixel(sample) {
        return [3*sample.B04, 3*sample.B03, 3*sample.B02];
    }
"""
```

### 1.4) Making Request

```
request_true_color = SentinelHubRequest(
    data_folder= r"path/to/your/directory", # provide the path you want to save the downloaded image
    evalscript=evalscript_true_color,
    input_data=[
        SentinelHubRequest.input_data(
            data_collection=DataCollection.SENTINEL2_L2A.define_from(
                "s2l2a", service_url=config.sh_base_url
            ),
            time_interval=("2023-08-12", "2024-01-29"),     # provide time interval 
        )
    ],
    responses=[SentinelHubRequest.output_response("default", MimeType.PNG)],           # provide the format of the data
    bbox=bbox,
    size=betsiboka_size,
    config=config,
)
```

### 1.5) Downloading the Data 

```
true_color_imgs = request_true_color.get_data(save_data=True)
```


<img src="https://github.com/KianESoftware/Satellite-image-processing/blob/main/images/example1.png" height="350" width="500"  >


# Basic Image Processing

In this section basic image processing is performed.

```
image_gray = cv2.imread("example1.png",1)
```

```
print("shape is",image_gray.shape,"\n")
print(image_gray)
plt.imshow(image_gray,cmap="gray")
```
<img src="https://github.com/KianESoftware/Satellite-image-processing/blob/main/images/gray.png" height="350" width="500"  >

```
image_color = cv2.imread("example1.png",1)
```
```
print("shape is",image_color.shape,"\n")
print(image_color)
plt.imshow(image_color)
```
OpenCV uses BGR color space instead of RGB so the image does not seem as we expect 

<img src="https://github.com/KianESoftware/Satellite-image-processing/blob/main/images/colorfalse.png" height="350" width="500"  >

to convert it to RGB color space we will use the following script 

```
image_color_corrected = cv2.cvtColor(image_color2, cv2.COLOR_BGR2RGB)
plt.imshow(image_color_corrected)
```
<img src="https://github.com/KianESoftware/Satellite-image-processing/blob/main/images/corrected_colorful.png" height="350" width="500"  >
