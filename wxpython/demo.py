import wx

app = wx.App() 
frame = wx.Frame(None, -1, title='wx_00_base.py', pos=(800,800), size=(300,350))
frame.Centre()
frame.Show()
print "hello world"
print "fff"

app.MainLoop()