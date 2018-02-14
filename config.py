class Config(object):
	""" 
	Common Configuration
	"""
	pass

class DevelopmentConfig(Config):
	"""
	Configuration for development environment
	"""
	DEBUG = True

class ProductionConfig(Config):
	"""
	Configuration for development environment
	"""
	DEBUG = False

app_config = {
	'development' : DevelopmentConfig,
	'production' : ProductionConfig
}