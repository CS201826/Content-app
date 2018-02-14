# Import packages
from flask import abort, Flask, render_template
import boto3
import os
from config import app_config

# Create DynamoDb instance
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

def create_app(config_name):
	# Create application instance
	app = Flask(__name__, instance_relative_config=True)

	# Load config based on environment
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')

	try:
		# Create DynamoDb table articles
		table = dynamodb.create_table(
		    TableName='articles',
		    KeySchema=[
		        {
		            'AttributeName': 'article_id',
		            'KeyType': 'HASH'
		        }
		    ],
		    AttributeDefinitions=[
		        {
		            'AttributeName': 'article_id',
		            'AttributeType': 'S'
		        }

		    ],
		    ProvisionedThroughput={
		        'ReadCapacityUnits': 1,
		        'WriteCapacityUnits': 1
		    }
		)
	except Exception as exception:
		pass

	from .article import article as article_blueprint
	app.register_blueprint(article_blueprint)

	return app