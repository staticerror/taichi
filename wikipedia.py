from base.sitescraper import SiteScraper
from base.htmlutils import getHtml, getTitle, parseAll


class Wikipedia(SiteScraper):

	def makeSearchLink(self):
		return "http://en.wikipedia.org/wiki/"

	def fetchArticle(self, keyword):
		url = self.makeSearchLink() + keyword
		htmlpage =  getHtml(url)
		self.article.append( url)
		self.article.append(getTitle(htmlpage) )
		self.article.append(parseAll(htmlpage, 'p'))


a = Wikipedia()
a.fetchArticle("Pink_floyd")
print a.article
