
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
        
        vbox.Add(editortoolbar, 0, wx.EXPAND) # editor, below menubar
        

        vbox.Add(verticaltoolbar, 10, wx.EXPAND | wx.RIGHT| wx.TOP| wx.BOTTOM, 20) 


        self.Bind(wx.EVT_TOOL, self.OnExit, id=wx.ID_EXIT)
        self.SetSizer(vbox)


    def OnExit(self, event):
        self.Close()
        
    def VerticalToolbar(self):
        
        MainContainer = wx.BoxSizer(wx.HORIZONTAL)

        verticaltoolbar = wx.ToolBar(self, -1, style = wx.TB_VERTICAL )
        verticaltoolbar.AddLabelTool(-1, "Research", wx.Bitmap('/home/desktop/Desktop/crystal_project/64x64/apps/search.png'))
        verticaltoolbar.AddLabelTool(-1, "Edit", wx.Bitmap('/home/desktop/Desktop/crystal_project/64x64/apps/package_editorspackage_editors.png'))
        verticaltoolbar.AddLabelTool(-1, "Saved Articles", wx.Bitmap('/home/desktop/Desktop/crystal_project/64x64/filesystems/folder_red.png'))
        verticaltoolbar.Realize()

        MainContainer.Add(verticaltoolbar)
        
        notebook = self.ResearchNoteBook()
        MainContainer.Add(notebook, 5,  wx.EXPAND | wx.ALL, 20)
        

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
        
        panel = wx.Panel(self)
        nb = wx.Notebook(panel)

        # create the page windows as children of the notebook
        page1 = ResearchPage(nb)
        page2 = ResearchPage(nb)
        # add the pages to the notebook with the label to show on the tab
        nb.AddPage(page1, "Article Directories")
        nb.AddPage(page2, "Wikipedia")


        # finally, put the notebook in a sizer for the panel to manage
        # the layout
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(nb, 10, wx.EXPAND)
        panel.SetSizer(sizer)

        return panel





class ResearchPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        textbox = wx.TextCtrl(self, -1 )
        button = wx.Button(self, -1, 'Go!')
        resultbox = wx.TextCtrl(self, -1,style =  wx.TE_MULTILINE | wx.TE_DONTWRAP)
        hbox.Add(textbox, 4)
        hbox.Add((35,-1))
        hbox.Add(button , 1 ,  wx.ALIGN_RIGHT | wx.LEFT)
        hbox.Add((155,-1))

        
        vbox.Add(hbox, 1, wx.EXPAND | wx.ALL, 20)
        vbox.Add(resultbox, 7,  wx.EXPAND | wx.ALL , 20)

        self.SetSizer(vbox)




if __name__ == '__main__':
    app = wx.App(False)
    MainWindow(None, -1, "Article Domination")
    app.MainLoop()
