import pandas as pd
import googlemaps

def geocode(lista_endereco, google_key):
  
  gmaps = googlemaps.Client(key = google_key)
  
  geocode_enderecos = []
  
  for nome, endereco in lista_endereco.items():
    
    print("Processando endereco {tmp}".format(tmp = endereco))
    
    try:
      
      resultado_geocode = gmaps.geocode(endereco)
      
      latlong = resultado_geocode[0]['geometry']['location'].values()
      
      latlong.extend([endereco, nome])
      
      geocode_enderecos.append(latlong)
      
    except Exception as e:
      print(e)
      resultado_geocode.append(['NA','NA',endereco,nome])
      
  resultado_geocode_df = pd.DataFrame(geocode_enderecos)
  
  resultado_geocode_df.columns = ['lat', 'long', 'endereco', 'nome']
  
  return(resultado_geocode_df)




















