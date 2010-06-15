
import wx
from wx import xrc


class MainWindow(wx.Frame):
    
    def __init__(self, parent , id,  title):
        wx.Frame.__init__(self, parent, id, title, size=(550, 580))

        self.MenuBar()
        self.MainArea()
        self.StatusBar()


        self.Centre()
        self.Maximize()
        self.Show()

        
    def MenuBar(self):
        
        menubar = wx.MenuBar()
        file = wx.Menu()
        edit = wx.Menu()
        help = wx.Menu()

        menubar.Append(file , "&File")
        menubar.Append(edit , "&Edit")
        menubar.Append(help , "&Help")
        
        self.SetMenuBar(menubar)
        
    
    def MainArea(self):
        # Master Blaster container, the main guy in the app responsible for every thing
        vbox = wx.BoxSizer(wx.VERTICAL)
        editortoolbar = self.EditorToolbar() #Editor actions, below menubar
        verticaltoolbar = self.VerticalToolbar() # the three main research, edit etc
        vbox.Add(editortoolbar, 0 , wx.EXPAND)
        vbox.Add(verticaltoolbar, 0, wx.EXPAND) 

        self.Bind(wx.EVT_TOOL, self.OnExit, id=wx.ID_EXIT)
        self.SetSizer(vbox)


    def OnExit(self, event):
        self.Close()
        
    def VerticalToolbar(self):
        
        MainContainer = wx.GridBagSizer(2,2)

        verticaltoolbar = wx.ToolBar(self, -1, style = wx.TB_VERTICAL )
        verticaltoolbar.AddLabelTool(-1, "Research", wx.Bitmap('/home/desktop/Desktop/crystal_project/64x64/apps/search.png'))
        verticaltoolbar.AddLabelTool(-1, "Edit", wx.Bitmap('/home/desktop/Desktop/crystal_project/64x64/apps/package_editorspackage_editors.png'))
        verticaltoolbar.AddLabelTool(-1, "Saved Articles", wx.Bitmap('/home/desktop/Desktop/crystal_project/64x64/filesystems/folder_red.png'))
        verticaltoolbar.Realize()

        MainContainer.Add(verticaltoolbar, (5,0), flag = wx.EXPAND , border = 4)

        return MainContainer


    def EditorToolbar(self):

        editortoolbar = wx.ToolBar(self, -1 )
        editortoolbar.AddLabelTool(wx.ID_EXIT, '', wx.Bitmap('/home/desktop/Desktop/crystal_project/24x24/actions/save_all.png'))
        editortoolbar.AddLabelTool(wx.ID_EXIT, '', wx.Bitmap('/home/desktop/Desktop/crystal_project/24x24/actions/fileclose.png'))
        editortoolbar.Realize()
        return editortoolbar


    def StatusBar(self):
        self.statusbar = self.CreateStatusBar()
    

    def ResearchNoteBook(self):
        
        p = wx.Panel(self)
        nb = wx.Notebook(p)

        # create the page windows as children of the notebook
        page1 = PageOne(nb)
        page2 = PageTwo(nb)
        page3 = PageThree(nb)

        # add the pages to the notebook with the label to show on the tab
        nb.AddPage(page1, "Page 1")
        nb.AddPage(page2, "Page 2")
        nb.AddPage(page3, "Page 3")

        # finally, put the notebook in a sizer for the panel to manage
        # the layout
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)







class ArtdirsPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageOne object", (20,20))

class WikipediaPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageTwo object", (40,40))

class YAnswersPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageThree object", (60,60))





if __name__ == '__main__':
    app = wx.App(False)
    MainWindow(None, -1, "Article Domination")
    app.MainLoop()
