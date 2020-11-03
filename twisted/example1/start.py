"""
This is the simplest example of twisted.
1. Run this script in one terminal by: python3 start.py
2. Send some request in another terminal by: telnet localhost 1234
   and then i can send text from this terminal.
"""

from twisted.internet import protocol, reactor, endpoints

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        print('i received a request...') #  my line...
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

endpoints.serverFromString(reactor, "tcp:1234").listen(EchoFactory())
reactor.run()
