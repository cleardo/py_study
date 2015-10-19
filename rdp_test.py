from rdpy.protocol.rfb import rfb

class MyRFBFactory(rfb.ClientFactory):

    def clientConnectionLost(self, connector, reason):
        reactor.stop()

    def clientConnectionFailed(self, connector, reason):
        reactor.stop()

    def buildObserver(self, controller, addr):
        class MyObserver(rfb.RFBClientObserver):

            def onReady(self):
                """
                @summary: Event when network stack is ready to receive or send event
                """

            def onUpdate(self, width, height, x, y, pixelFormat, encoding, data):
                """
                @summary: Implement RFBClientObserver interface
                @param width: width of new image
                @param height: height of new image
                @param x: x position of new image
                @param y: y position of new image
                @param pixelFormat: pixefFormat structure in rfb.message.PixelFormat
                @param encoding: encoding type rfb.message.Encoding
                @param data: image data in accordance with pixel format and encoding
                """

            def onCutText(self, text):
                """
                @summary: event when server send cut text event
                @param text: text received
                """

            def onBell(self):
                """
                @summary: event when server send biiip
                """

            def onClose(self):
                """
                @summary: Call when stack is close
                """
		print "exit"

        return MyObserver(controller)

from twisted.internet import reactor

print "rdp"

reactor.connectTCP("192.168.56.101", 3389, MyRFBFactory())

reactor.run()

