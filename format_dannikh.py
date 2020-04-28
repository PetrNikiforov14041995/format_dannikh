#JSON
import json
from pprint import pprint

with open(r"format_dannikh/newsafr.json") as f:
  json_data = json.load(f)
  list_news = []
  for news in json_data["rss"]["channel"]["items"]:
    news = news["description"].lower()
    for word in news.split():
      if len(word) > 6:
        list_news.append(word)
        
  word_list = {}
  for afr_news in list_news:
    top_word_list = {afr_news:list_news.count(afr_news)}
    word_list.update(top_word_list)

  list_words = list(word_list.items())
  list_words.sort(key=lambda afr_news:afr_news[1])
  list_words = list_words[-10:]
  
  list_words.reverse()
  print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в файле .JSON\n') 
  for afr_news in range(10):
    print(list_words[afr_news])




#XML
import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse(f"format_dannikh/newsafr.xml", parser)
root = tree.getroot()

new_list = []
news_xml = root.findall("channel/item")
for news_top in news_xml:
  news_top = news_top.find("description").text.lower()
  new_list += news_top.split()
  
new_xml_list = []
for xml in new_list:
  if len(xml) > 6:
    new_xml_list.append(xml)

word_list = {}
for afr_news in new_xml_list:
  top_word_list = {afr_news:new_xml_list.count(afr_news)}
  word_list.update(top_word_list)

list_words = list(word_list.items())
list_words.sort(key=lambda afr_news:afr_news[1])
list_words = list_words[-10:]
  
list_words.reverse()
print('\nТоп 10 самых часто встречающихся в новостях слов длиннее 6 символов в файле .XML\n')
for afr_news in range(10):
  print(list_words[afr_news])
    

