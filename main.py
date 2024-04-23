import geopandas as gpd

# CArregar o shapefile
gdf = gpd.read_file('palmeira/municipio_palmeira.shp')

#formato utilizado nos dados do sicar

#cod_tema;nom_tema;cod_imovel;mod_fiscal;num_area;ind_status;ind_tipo;des_condic;municipio;cod_estado
#AREA_IMOVEL;Area do Imovel;RS-4313706-ACCCBEB81F2F48348595909C8523B84D;0,1927;3,0835;AT;IRU;Aguardando analise;Palmeira das Missoes;



# Iterate over each row and save individual shapefiles
for index, row in gdf.iterrows():
    # Extract the 'cod_imovel' property
    cod_imovel = row['cod_imovel']

    # Filter the GeoDataFrame to get only the current row and save it
    single_item_gdf = gdf[gdf['cod_imovel'] == cod_imovel]
    output_filename = f"output/{cod_imovel}.shp"
    single_item_gdf.to_file(output_filename)
