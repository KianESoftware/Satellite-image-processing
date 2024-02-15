import sentinelhub
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from sentinelhub import SHConfig, SentinelHubRequest, DataCollection, BBox, bbox_to_dimensions, constants, MimeType
import matplotlib


config = SHConfig()
config.sh_client_id = "sh-ef5a8a93-0fa7-4cd1-b392-4d058f3d611d"
config.sh_client_secret = "df2iMfx7g8qcpDngaMvmi2LFdb3WW2n4"
config.sh_token_url = "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"
config.sh_base_url = "https://sh.dataspace.copernicus.eu"

resolution = 10

bbox = BBox(bbox=[
  28.90825,
  40.066512,
  29.066584,
  40.14319
], crs=sentinelhub.CRS.WGS84)
betsiboka_size = bbox_to_dimensions(bbox, resolution=resolution)
print(f"Image shape at {resolution} m resolution: {betsiboka_size} pixels")


evalscript_true_color = """
    //VERSION=3

    function setup() {
        return {
            input: [{
                bands: ["B04", "B03", "B02"]
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

request_true_color = SentinelHubRequest(
    data_folder= r"C:\Users\kiann\PycharmProjects\MyBestProject",
    evalscript=evalscript_true_color,
    input_data=[
        SentinelHubRequest.input_data(
            data_collection=DataCollection.SENTINEL2_L2A.define_from(
                "s2l2a", service_url=config.sh_base_url
            ),
            time_interval=("2023-08-12", "2023-12-29"),
        )
    ],
    responses=[SentinelHubRequest.output_response("default", MimeType.PNG)],
    bbox=bbox,
    size=betsiboka_size,
    config=config,
)

true_color_imgs = request_true_color.get_data(save_data=True)

print(
    f"Returned data is of type = {type(true_color_imgs)} and length {len(true_color_imgs)}."
)
print(
    f"Single element in the list is of type {type(true_color_imgs[-1])} and has shape {true_color_imgs[-1].shape}"
)

image = true_color_imgs[0]
print(f"Image type: {image.dtype}")
