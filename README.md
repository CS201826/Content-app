# CRUD Module with FLASK + AMAZON DYNAMODB

Save all articles using Flask (http://scrapy.org) + Amazon DynamoDb

##Compatability

This is Compatiable with Python 3, Flask 0.12, AWS DynamoDb

### Usage

This program required python to be installed

Install Python 3.6 from https://www.python.org/downloads/

### Create a virtual environment not required, but nice to have

mkvirtualenv content-env

### Install Flask from 

pip install flask

also install below additional dependency

pip install flask-bootstrap

pip install flask-wtf

### Install python library Boto 3 (The AWS SDK for Python)

pip install boto3

Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3, Amazon DynamoDb and Amazon EC2.

You can read documentation from https://boto3.readthedocs.io/en/latest/

### Install and Setup DynamoDb on your local machine

Dependency - JRE version > 6.0

1. Download and run DynamoDB on your computer

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html

After you download the archive, extract the contents and copy the extracted directory to a location of your choice.

2. Set up an AWS access key to use the AWS SDKs

AWS_ACCESS_KEY = EXAMPLE

AWS_SECRET_ACCESS_KEY = EXAMPLEAPP

3. To start DynamoDB on your computer, open a command prompt window, navigate to the directory where you extracted DynamoDBLocal.jar, and type the following command:

java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb

Default port is 8000, if you want to change port specify below parameter

--port 8999

4. Check DynamoDB instance is working or not, type below url in browser

http://127.0.0.1:8000/shell

### Integrate Flask with DynamoDB

1. Import Boto 3 library

import boto3

2. Create DynamoDB instance in your __init__.py file

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

3. Create Table "articles" if not exists

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

4. Add an article

data = dict()
data['article_id'] = 'UNIQUE_KEY'
data['title'] = title
data['description'] = description

response = table.put_item(Item=data)

or 

response = table.put_item(
	Item={
		'article_id':'UNIQUE_KEY',
		'title':title,
		'description':description
	}
)

5. Edit an article

data = dict()
data['article_id'] = article_id
data['title'] = title
data['description'] = description

response = table.update_item(Item=data)

or 

response = table.update_item(
	Key={
		'article_id':article_id,
		'title':title,
		'description':description
	}
)

6. Delete an article

response = table.delete_item(
	Key={
		'article_id':article_id
	}
)

7. List articles

response = table.scan(
// specify an filters if required 
)

8. Query

response = table.query(
	KeyConditionExpression=Key('title').eq('test')
)


You can use this code as an example to help you get started as well as DynamoDB's great documentation. 

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html

==> All articles will be stored in DynamoDB.

## License

This project is licensed under the MIT License