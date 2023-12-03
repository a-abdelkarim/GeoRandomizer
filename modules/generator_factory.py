from .point_generator import PointGenerator


def GeneratorFactory(generator_type='point', file_path=None, out_name=None, features_number=None):
    generators = dict(
        point = PointGenerator(file_path, out_name, features_number)
    )
    return generators[generator_type]