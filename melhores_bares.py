from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def melhores_bares(base_url):
  #base_url = 'https://www.viajali.com.br/bares-bh/'
  page = urlopen(base_url)
  soup = BeautifulSoup(page, 'html.parser')
  
  localizacao = soup.find_all('p')
  nome_bares = soup.find_all('h3')
  
  bar_loc_list = []
  for loc in localizacao:
      try:
          endereco = re.search('Localização: (.*).', str(loc.text)).group(1)
          
          bar_loc_list.append(endereco)
          
      except Exception as e:
          pass
      
  bar_loc_list = list(dict.fromkeys(bar_loc_list))
  
  bar_list = []
  for bar in nome_bares:
      try:
          nome_bar = re.search('([A-Za-z].*)', bar.text).group(1)
          
          bar_list.append(nome_bar)
          
      except Exception as e:
          pass
  

  listao = {}
  for bar, endereco in zip(bar_list, bar_loc_list):
      listao[bar] = endereco
      
  return(listao)




