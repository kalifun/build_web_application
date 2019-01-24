# -*- coding:utf-8 -*-
import wx
import os

class OpenfileTool(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self, parent, title=title,size=(500,400))
        self.panel = wx.Panel(self)
        self.content()

 

    def content(self):
        url_text = wx.StaticText(self.panel,label=u"路径：")
        self.path_text = wx.TextCtrl(self.panel,wx.TE_MULTILINE)
        openfile_text = wx.Button(self.panel,label=u"打开")
        openfile_text.Bind(wx.EVT_BUTTON,self.readfile)
        self.content_text = wx.TextCtrl(self.panel,style =wx.TE_MULTILINE)
        box = wx.BoxSizer()
        box.Add(url_text,proportion = 0.5,flag = wx.ALIGN_CENTER|wx.ALIGN_RIGHT,border=3)
        box.Add(self.path_text,proportion = 3,flag = wx.EXPAND|wx.ALL,border=3)
        box.Add(openfile_text,proportion = 1,flag = wx.EXPAND|wx.ALL,border=3)

        v_box = wx.BoxSizer(wx.VERTICAL)
        v_box.Add(box,proportion = 0.5,flag=wx.EXPAND|wx.ALL,border=3)
        v_box.Add(self.content_text,proportion = 5,flag=wx.EXPAND|wx.ALL,border=3)
        self.panel.SetSizer(v_box)

    def readfile(self,event):
        with wx.FileDialog(self, "Open XYZ file", wildcard="txt files (*.txt)|*.txt",style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     
            # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            self.path_text.SetValue(pathname)
            try:
                with open(pathname, 'r') as file:
                    # datas = file.readlines()
                    # for data in datas:
                    #     self.loadfile(data)
                    self.content_text.SetValue(file.read())
            except IOError:
                wx.LogError("Cannot open file '%s'." % newfile)
    # def loadfile(self,data):
    #     self.content_text.SetValue(data)
if __name__ == "__main__":
    app = wx.App(True)
    frame = OpenfileTool(None,"OpenfileTool")
    frame.Show()
    app.MainLoop()
