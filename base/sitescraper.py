from htmlutils import *


class SiteScraper:

	def __init__(self):
		self.article = []


	def makeSearchLink(self, searchurl):
		allLinks = getSearchLinks(getHtml(searchurl))
		searchlink = randElement(allLinks)
		return searchlink

	def makeArticle(self,searchurl, *body_pattern):
			searchlink = self.makeSearchLink(searchurl)
			htmlpage = getHtml(searchlink)
			title = getTitle(htmlpage)
			body= parse(htmlpage, *body_pattern)
			self.article.append(title)
			self.article.append(body)
			self.article.append(searchlink)
