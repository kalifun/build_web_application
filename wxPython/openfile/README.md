# python-gui
## 学习wxpython模块
[![](https://image.kalifun.top/upload/1901/ead8e78517917ab1.png)](https://image.kalifun.top/upload/1901/ead8e78517917ab1.png)
## 安装
```python
pip install -U wxPython
```
## 创建一个简单程序
```python
# First things, first. Import the wxPython package.
import wx

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = wx.Frame(None, title="Hello World")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()
```
## GUI设计
> ### wx.BoxSizer()
### 这个可以设置你的box的比例。proportion比例设置。
```python
url_text = wx.StaticText(self.panel,label=u"路径：")
self.path_text = wx.TextCtrl(self.panel,wx.TE_MULTILINE)
openfile_text = wx.Button(self.panel,label=u"打开")
openfile_text.Bind(wx.EVT_BUTTON,self.readfile)
self.content_text = wx.TextCtrl(self.panel,style =wx.TE_MULTILINE)
box = wx.BoxSizer()
box.Add(url_text,proportion = 0.5,flag = wx.ALIGN_CENTER|wx.ALIGN_RIGHT,border=3)
box.Add(self.path_text,proportion = 3,flag = wx.EXPAND|wx.ALL,border=3)
box.Add(openfile_text,proportion = 1,flag = wx.EXPAND|wx.ALL,border=3)
```
### 设置了0.5|3|1
[![](https://image.kalifun.top/upload/1902/270a32000255164c.png)](https://image.kalifun.top/upload/1902/270a32000255164c.png)
```python
v_box = wx.BoxSizer(wx.VERTICAL)
v_box.Add(box,proportion = 0.5,flag=wx.EXPAND|wx.ALL,border=3)
v_box.Add(self.content_text,proportion = 5,flag=wx.EXPAND|wx.ALL,border=3)
```
### 上下分为两个部分，上下分为0.5|5
### 设置了 0.5|5
[![](https://image.kalifun.top/upload/1902/741a19ade9085a02.png)](https://image.kalifun.top/upload/1902/741a19ade9085a02.png)
## 创建事件
> ### 创建事件基本发生在button上。创建事件关键词bind
```python
openfile_text.Bind(wx.EVT_BUTTON,self.readfile)
def readfile(self,event):
```
