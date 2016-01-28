from setuptools import setup

setup(name='slackclient-asyncio',
      version='0.16',
      description='Python client for Slack.com using asyncio library',
      url='http://github.com/slackhq/python-slackclient-asyncio',
      author='Ryan Huber',
      author_email='ryan@slack-corp.com',
      license='MIT',
      packages=['slackclient_asyncio'],
      install_requires=[
        'websockets',
      ],
      zip_safe=False)
