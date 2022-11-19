import urllib.request
import json
import random


class IngenuityImage:
    def __init__(self, json_url):
        self.json_url = json_url
        self.json_data = None
        self.selected_image = None

    def get_json(self):
        json_data = None
        with urllib.request.urlopen(self.json_url) as url:
            json_response = url.read()
            json_data = json.loads(json_response)
        self.json_data = json_data

    def pick_random_from_data(self):
        max_number = len(self.json_data['images'])
        photo_number = random.randint(0, max_number-1)
        self.selected_image = photo_number

    def get_image_url(self):
        if not self.json_data:
            self.get_json()
        if not self.selected_image:
            self.pick_random_from_data()
        
        return self.json_data['images'][self.selected_image]['image_files']['small']

if __name__ == "__main__":
    FEED_URL = "https://mars.nasa.gov/rss/api/?feed=raw_images&category=mars2020,ingenuity&feedtype=json&ver=1.2&num=100&page=0&&order=sol+desc&&search=|FRONT_HAZCAM_LEFT_A|FRONT_HAZCAM_LEFT_B|NAVCAM_LEFT|FRONT_HAZCAM_RIGHT_A|FRONT_HAZCAM_RIGHT_B&&&condition_2=2022-09-09T11:06:54.000Z:date_received:gte&condition_3=553,552,526,513:sol:in&"
    ingenuityImage = IngenuityImage(FEED_URL)
    url = ingenuityImage.get_image_url()
    print(url)


