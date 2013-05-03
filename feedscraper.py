mport feedparser
import nltk
from urllib import urlopen
import re

def get_entries(feed, words):
	feeds1b=[]
	feeds1a = feedparser.parse(feed)
	for i in range(len(feeds1a.entries)):
		for j in words:
			if j in feeds1a.entries[i].title:
				feeds1b.append(feeds1a.entries[i])
	return feeds1b

def get_summary(url):
	sentences2, sentences3, sentences4 = {}, {}, {}	
	summary1 = []
	html1 = urlopen(url).read()
	html2 = nltk.clean_html(html1)
	sentences1 = nltk.sent_tokenize(html2)
	for i in range(len(sentences1)):
		sentences2[i] = sentences1[i]
	for key, value in sentences2.items():
		sentences3[key] = nltk.word_tokenize(value)
	regex1 = '\d+'
	regex2 = re.compile(regex1)
	for key1, value1 in sentences3.iteritems():
		for j in range(len(value1)):
			if re.match(regex2, value1[j]):
				sentences4[key1] = value1
	for i in sentences4.itervalues():
		summary1.append(' '.join(i))
	return summary1

def get_feed_summary(feed, words):
	feed_summary = []
	entries1 = get_entries(feed, words)
	for i in range(len(entries1)):
		feed_summary.append(get_summary(entries1[i].link))
	return feed_summary
