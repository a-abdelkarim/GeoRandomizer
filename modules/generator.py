from abc import ABC, abstractmethod
import json
import geojson


class Generator(ABC):
    
    def __init__(self, in_file: str, out_file: str, number_of_features: int) -> None:
        self._i_file = in_file
        self._o_file = out_file
        self._nof = number_of_features
        
    def _read_json_file(self):
        file = open(self._i_file)
        json_object = json.load(file)
        return json_object
    
    def _is_valid_json(self):
        """Check if json file"""
        if self._i_file.lower().endswith(".json") or self._i_file.lower().endswith(".geojson"):
            return True
        print("[ERROR]: This is not a Valid Json")     
        return False
    
    def _is_valid_feature(self):
        # Check if valid json object
        if self._is_valid_json():
            # define json object
            json_object = self._read_json_file()
            if json_object["type"] == "FeatureCollection" and json_object["features"]:
                return True
        print("[ERROR]: This is not a Valid Feature")
        return False
    
    def _create_feature_collection(self):
        points_features = self._generate_features()
        featureCollection = geojson.FeatureCollection(points_features)
        return featureCollection
    
    def _write_json_file(self, feature_collection: dict):
        with open(self._o_file, 'w') as json_file:
            json.dump(feature_collection, json_file, indent=4)
        return self._o_file
        
    @abstractmethod
    def _generate_features():
        pass
    
    @abstractmethod
    def generate(self):
        pass