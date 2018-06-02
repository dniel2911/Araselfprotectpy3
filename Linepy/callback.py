# -*- coding: utf-8 -*-
class Callback(object):

    def __init__(self, callback):
        self.callback = callback

    def PinVerified(self, pin):
        self.callback("Masukan pin'" + pin + "' Batas Satu menit")

    def QrUrl(self, url, showQr=True):
        if showQr:
            notice='pindaiQR '
        else:
            notice=''
        self.callback('masukan boskuh' + notice + 'Batas maksimal 1menit\n\n\n\n' + url)
        if showQr:
            try:
                import pyqrcode
                url = pyqrcode.create(url)
                self.callback(url.terminal('green', 'white', 1))
            except:
                pass

    def default(self, str):
        self.callback(str)
