import wx, wx.html
from artdirs import *
from wx import xrc
from wikipedia import Wikipedia
import threading
from base.htmlutils import stripHtml

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
        

        vbox.Add(verticaltoolbar, 1, wx.EXPAND | wx.RIGHT| wx.TOP | wx.BOTTOM, 20) 



        self.SetSizer(vbox)


        
    def VerticalToolbar(self):
        
        MainContainer = wx.BoxSizer(wx.HORIZONTAL)

        verticaltoolbar = wx.ToolBar(self, -1, style = wx.TB_VERTICAL )

        verticaltoolbar.AddSeparator()
        verticaltoolbar.AddLabelTool(-1, "Research", wx.Bitmap('/home/desktop/Desktop/crystal_project/64x64/apps/search.png'))
        verticaltoolbar.AddSeparator()
        verticaltoolbar.AddLabelTool(-1, "Edit", wx.Bitmap('/home/desktop/Desktop/crystal_project/64x64/apps/package_editorspackage_editors.png'))
        verticaltoolbar.AddSeparator()
        verticaltoolbar.AddLabelTool(-1, "Saved Articles", wx.Bitmap('/home/desktop/Desktop/crystal_project/64x64/filesystems/folder_red.png'))
        verticaltoolbar.AddSeparator()
        verticaltoolbar.Realize()


        MainContainer.Add(verticaltoolbar, 0, wx.TOP , border = 10)
        MainContainer.Add((20, -1))
        
        notebook = self.ResearchNoteBook()
        MainContainer.Add(notebook, 7,  wx.EXPAND | wx.ALL, 10)
        

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
        page1 = ResearchPage(nb, [ Ezine, Dashboard, ABase])
        page2 = ResearchPage(nb, [ Wikipedia ])
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
    def __init__(self, parent, models):
        wx.Panel.__init__(self, parent)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.textbox = wx.TextCtrl(self, -1 )
        self.button = wx.Button(self, 200, 'Go!')



        self.resultbox = wx.TextCtrl(self, -1,style =  wx.TE_MULTILINE)
#        self.resultbox = wx.html.HtmlWindow(self, -1)
       # self.resultbox.SetFonts(normal_face = "helvetica", fixed_face = "helvetica")
        self.hbox.Add(self.textbox, 3)
        self.hbox.Add((25,-1))
        self.hbox.Add(self.button , 1 ,  wx.ALIGN_RIGHT | wx.LEFT)
        self.hbox.Add((155,-1))

        
        self.vbox.Add(self.hbox, 1, wx.EXPAND | wx.ALL, 30)
        self.vbox.Add(self.resultbox, 7,  wx.EXPAND | wx.ALL , 30)

        self.SetSizer(self.vbox)
        self.models = models
        

        self.Bind(wx.EVT_BUTTON,  self.OnClicked, id = self.button.GetId())


    def fetchArticleThread(self):
        self.resultbox.Disable()
        for model in self.models:
            n = model()
            n.fetchArticle(self.keyword)
            for result in n.article:
                self.resultbox.AppendText(stripHtml(str(result)))
        self.resultbox.AppendText("\n\n\n")

    def OnClicked(self, event):
        
        self.keyword = str(self.textbox.GetValue())
#        self.keyword = str(self.keyword.replace(' ', "+"))

        self.resultbox.Clear()
        threading.Thread(target = self.fetchArticleThread).start()

        
if __name__ == '__main__':
    app = wx.App(False)
    MainWindow(None, -1, "Article Domination")
    app.MainLoop()
