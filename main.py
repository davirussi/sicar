import geopandas as gpd
from pathlib import Path
import fiona

#ativar drive kml
fiona.supported_drivers['KML'] = 'rw'


# Carregar o shapefile
gdf = gpd.read_file('palmeira/municipio_palmeira.shp')

#formato utilizado nos dados do sicar

#cod_tema;nom_tema;cod_imovel;mod_fiscal;num_area;ind_status;ind_tipo;des_condic;municipio;cod_estado
#AREA_IMOVEL;Area do Imovel;RS-4313706-ACCCBEB81F2F48348595909C8523B84D;0,1927;3,0835;AT;IRU;Aguardando analise;Palmeira das Missoes;

#cidades que irá salvar, verificar se a pasta já existe senão criar
cidades = ['Palmeira das Missoes','Boa Vista das Missoes', 'Jaboticaba']

for cidade in cidades:
    path = Path('output/'+cidade)
    path.mkdir(parents=True, exist_ok=True)




# Iterate over each row and save individual shapefiles
for index, row in gdf.iterrows():
    # Extract the 'cod_imovel' property
    cod_imovel = row['cod_imovel']
    municipio = row['municipio'] #municipio
    

    # Filter the GeoDataFrame to get only the current row and save it
    if municipio in cidades:
        single_item_gdf = gdf[gdf['cod_imovel'] == cod_imovel]
        output_filename = f"output/{municipio}/{cod_imovel}.shp"
        single_item_gdf.to_file(output_filename)
        
    # Filtrar GeoDataFrame para pegar cada linha e salvar num novo kml
    if municipio in cidades:
        single_item_gdf = gdf[gdf['cod_imovel'] == cod_imovel]
        output_filename = f"output/{municipio}/{cod_imovel}.kml"
        single_item_gdf.to_file(output_filename, driver='KML')