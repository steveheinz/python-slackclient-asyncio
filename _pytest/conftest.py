import pytest
from slackclient_asyncio._channel import Channel
from slackclient_asyncio._server import Server
from slackclient_asyncio._client import SlackClient

@pytest.fixture
def server(monkeypatch):
    myserver = Server('xoxp-1234123412341234-12341234-1234', False)
    return myserver

@pytest.fixture
def slackclient(server):
    myslackclient = SlackClient('xoxp-1234123412341234-12341234-1234')
    return myslackclient

@pytest.fixture
def channel(server):
    mychannel = Channel(server, "somechannel", "C12341234", ["user"])
    return mychannel

