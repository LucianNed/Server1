#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding-utf8 :
'''
Simple client web per descarregar de udl.cat

@author: Lucian
'''
import urllib2
import bs4


class Client(object):

    def get_webpage(self, page):
        # obtenir plana web
        f = urllib2.urlopen(page)   #obro la pagina
        htmlpage = f.read()     #llegeixo la pagina
        f.close()
        return htmlpage

    def search_data(self, html):
        # buscar dades
        bs = bs4.BeautifulSoup(html,"lxml")     # crea un arbre apartit del html
        caixa = bs.find("div","sg-featuredlink")    #retorna 21
        items = caixa.find_all("div", "featured-links-item")    #retorna 9
        results = []
        for item in items:
            time = item.find('time')["datetime"]
            text = item.find('span','flink-title').text
            results.append((time,text))
        return results

    def main(self):
        webpag = self.get_webpage('http://www.udl.cat')
        results = self.search_data(webpag)

        # imprimir resultats
        print results
        #print len(results)

if __name__ == "__main__":
    cw = Client()
    cw.main()
