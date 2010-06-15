///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Dec 29 2008)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __noname__
#define __noname__

#include <wx/statusbr.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/string.h>
#include <wx/menu.h>
#include <wx/textctrl.h>
#include <wx/button.h>
#include <wx/sizer.h>
#include <wx/panel.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/notebook.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class Article
///////////////////////////////////////////////////////////////////////////////
class Article : public wxFrame 
{
	private:
	
	protected:
		wxStatusBar* statusBar;
		wxMenuBar* menuBar;
		wxMenu* fileMenu;
		wxMenu* editMenu;
		wxMenu* helpMenu;
		wxNotebook* mainNotebook;
		wxPanel* researchPanel;
		wxNotebook* m_notebook2;
		wxPanel* m_panel8;
		wxTextCtrl* m_textCtrl4;
		wxButton* m_button3;
		
		wxPanel* m_panel9;
		wxPanel* m_panel10;
		wxPanel* editPanel;
		wxPanel* savedArticlesPanel;
	
	public:
		Article( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("Article Domination"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 609,474 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		~Article();
	
};

#endif //__noname__
