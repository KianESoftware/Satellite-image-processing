import sentinelhub
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from sentinelhub import SHConfig, SentinelHubRequest, DataCollection, BBox, bbox_to_dimensions, constants, MimeType
import matplotlib
from datetime import datetime, timedelta

config = SHConfig()
config.sh_client_id = "sh-ef5a8a93-0fa7-4cd1-b392-4d058f3d611d"
config.sh_client_secret = "df2iMfx7g8qcpDngaMvmi2LFdb3WW2n4"
config.sh_token_url = "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"
config.sh_base_url = "https://sh.dataspace.copernicus.eu"



class SatelliteImages:

    def __init__(self,eval_script,start_date,end_date,area_of_interest,directory):


        self.eval_script = eval_script
        self.start_date= start_date
        self.end_date = end_date
        self.area_of_interst = area_of_interest
        self.directory = directory


    def test(self):

        print(self.area_of_interst)
        print("---------------------------------------------------/n")
        print(self.start_date)
        print(self.end_date)

        start = datetime(self.start_date[0],self.start_date[1],self.start_date[2])
        end = datetime(self.end_date[0],self.end_date[1],self.end_date[2])
        weeks_between = (end-start).days // 7
        print(weeks_between)

        reference_time= start
        time_intervals=[]
        while reference_time <= end:
            print(reference_time.strftime('%Y-%m-%d'))
            time_intervals.append(reference_time.strftime('%Y-%m-%d'))
            reference_time += timedelta(weeks=1)

        print(weeks_between)
        print(time_intervals)
        return time_intervals


    def get_image(self):

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
                return [5*sample.B04, 5*sample.B03, 5*sample.B02];
            }
        """

        start = datetime(self.start_date[0], self.start_date[1], self.start_date[2])
        end = datetime(self.end_date[0], self.end_date[1], self.end_date[2])

        reference_time= start
        time_intervals=[]
        while reference_time < end:
            print(reference_time.strftime('%Y-%m-%d'))
            time_intervals.append(reference_time.strftime('%Y-%m-%d'))
            reference_time += timedelta(weeks=1)

        for j in range(len(time_intervals)) :
            request_true_color = SentinelHubRequest(
                data_folder=self.directory,
                evalscript=evalscript_true_color,
                input_data=[
                    SentinelHubRequest.input_data(
                        data_collection=DataCollection.SENTINEL2_L2A.define_from(
                            "s2l2a", service_url=config.sh_base_url
                        ),
                        time_interval=(time_intervals[j],time_intervals[j+1])
                    )],
                responses=[SentinelHubRequest.output_response("default", MimeType.PNG)],
                bbox=BBox(bbox=self.area_of_interst, crs=sentinelhub.CRS.WGS84),
                #size=bbox_to_dimensions(bbox, resolution=resolution),
                config=config,)

            true_color_imgs = request_true_color.get_data(save_data=True)

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
                return [5*sample.B04, 5*sample.B03, 5*sample.B02];
            }
        """
obj1 = SatelliteImages(start_date=(2023,5,1),end_date=(2023,9,19),area_of_interest=[
  17.948898,
  46.480743,
  19.411181,
  47.421893
],directory=r'C:\Users\kiann\PycharmProjects\MyBestProject\github4',eval_script=evalscript_true_color)


obj1.test()
obj1.get_image()

