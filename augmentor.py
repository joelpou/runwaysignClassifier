import Augmentor

inputDir = '/home/pepelepoe/Documents/fgvc-aircraft-2013b/data/images'
# outputDir = u'/home/pepelepoe/Code/aircraftClassifier/data/output'
saveFormat = 'PNG'

# p = Augmentor.Pipeline(source_directory = inputDir, output_directory = outputDir, save_format=saveFormat)
p = Augmentor.Pipeline(source_directory = inputDir, save_format=saveFormat)
p.resize(probability=1.0, width=64, height=64, resample_filter='BICUBIC')
p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)
p.sample(10000)

p.process()
