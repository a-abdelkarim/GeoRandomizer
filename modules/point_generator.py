import numpy as np
import random
from shapely.geometry import Polygon, Point, mapping
import json
import geojson

from .generator import Generator


class PointGenerator(Generator):
    """Extract points from polygons"""
    in_file_path: str
    out_file_name: str
    points_numbers: int
    
    def __str__(self):
        return "Extractor Class"
    
    def random_points_within(self, poly):
        min_x, min_y, max_x, max_y = poly.bounds

        points = []

        while len(points) < self._nof:
            random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
            if (random_point.within(poly)):
                points.append(random_point)

        return points
    
    def _generate_features(self):
        # define json object
        if self._is_valid_feature():
            json_object = self._read_json_file()
            points_features = []
            for f in json_object["features"]:
                poly = Polygon(f["geometry"]["coordinates"][0])
                points = self.random_points_within(poly)
                print("######################")
                print(points)
                for point in points:
                    point_feature = json.dumps(mapping(point))
                    point_feature = json.loads(point_feature.replace("'",'"'))
                    # point_feature = geojson.Feature(geometry=point_feature['coordinates'])
                    point_feature = {
                                "type": "Feature",
                                "properties": {},
                                "geometry": {
                                    "type": "Point",
                                    "coordinates": point_feature["coordinates"]
                                }
                    }
                    print(point_feature)
                    points_features.append(point_feature)
            return points_features
        return False
    
    def generate(self):
        feature_collection = self._create_feature_collection()
        return self._write_json_file(feature_collection)
            


def main():
    file_path = "data/in/infile.json"
    out_name = "data/out/out.json"
    points_number = 2000
    extractor: PointGenerator = PointGenerator(file_path, out_name, points_number)
    print(extractor.generate())



    
if __name__ == "__main__":
    main()       