///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Dec 29 2008)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

Article::Article( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	statusBar = this->CreateStatusBar( 1, wxST_SIZEGRIP, wxID_ANY );
	menuBar = new wxMenuBar( 0 );
	fileMenu = new wxMenu();
	menuBar->Append( fileMenu, wxT("File") );
	
	editMenu = new wxMenu();
	menuBar->Append( editMenu, wxT("Edit") );
	
	helpMenu = new wxMenu();
	menuBar->Append( helpMenu, wxT("Help") );
	
	this->SetMenuBar( menuBar );
	
	wxBoxSizer* mainSizer;
	mainSizer = new wxBoxSizer( wxVERTICAL );
	
	mainNotebook = new wxNotebook( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0 );
	researchPanel = new wxPanel( mainNotebook, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* bSizer2;
	bSizer2 = new wxBoxSizer( wxVERTICAL );
	
	m_notebook2 = new wxNotebook( researchPanel, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0|wxSUNKEN_BORDER|wxTAB_TRAVERSAL );
	m_panel8 = new wxPanel( m_notebook2, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* bSizer3;
	bSizer3 = new wxBoxSizer( wxVERTICAL );
	
	wxBoxSizer* bSizer8;
	bSizer8 = new wxBoxSizer( wxHORIZONTAL );
	
	m_textCtrl4 = new wxTextCtrl( m_panel8, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_textCtrl4->SetMaxSize( wxSize( 200,-1 ) );
	
	bSizer8->Add( m_textCtrl4, 1, wxALL, 5 );
	
	m_button3 = new wxButton( m_panel8, wxID_ANY, wxT("MyButton"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer8->Add( m_button3, 0, wxALL, 5 );
	
	
	bSizer8->Add( 0, 0, 0, wxEXPAND|wxFIXED_MINSIZE|wxRIGHT|wxLEFT, 40 );
	
	bSizer3->Add( bSizer8, 0, wxEXPAND, 5 );
	
	m_panel8->SetSizer( bSizer3 );
	m_panel8->Layout();
	bSizer3->Fit( m_panel8 );
	m_notebook2->AddPage( m_panel8, wxT("Wikipedia"), true );
	m_panel9 = new wxPanel( m_notebook2, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* bSizer4;
	bSizer4 = new wxBoxSizer( wxVERTICAL );
	
	m_panel9->SetSizer( bSizer4 );
	m_panel9->Layout();
	bSizer4->Fit( m_panel9 );
	m_notebook2->AddPage( m_panel9, wxT("Article Directories"), false );
	m_panel10 = new wxPanel( m_notebook2, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* bSizer5;
	bSizer5 = new wxBoxSizer( wxVERTICAL );
	
	m_panel10->SetSizer( bSizer5 );
	m_panel10->Layout();
	bSizer5->Fit( m_panel10 );
	m_notebook2->AddPage( m_panel10, wxT("Yahoo! Answers"), false );
	
	bSizer2->Add( m_notebook2, 1, wxEXPAND | wxALL, 5 );
	
	researchPanel->SetSizer( bSizer2 );
	researchPanel->Layout();
	bSizer2->Fit( researchPanel );
	mainNotebook->AddPage( researchPanel, wxT("Research"), true );
	editPanel = new wxPanel( mainNotebook, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	mainNotebook->AddPage( editPanel, wxT("Editor"), false );
	savedArticlesPanel = new wxPanel( mainNotebook, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	mainNotebook->AddPage( savedArticlesPanel, wxT("Saved Articles"), false );
	
	mainSizer->Add( mainNotebook, 1, wxEXPAND | wxALL, 5 );
	
	this->SetSizer( mainSizer );
	this->Layout();
}

Article::~Article()
{
}
