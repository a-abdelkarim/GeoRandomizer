from point_generator import PointGenerator


def GeneratorFactory(generator_type='point', file_path, out_name, features_number):
    generators = dict(
        point = PointGenerator(file_path, out_name, features_number)
    )
    return generators[generator_type]