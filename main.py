import geopandas as gpd

# Load the shapefile
gdf = gpd.read_file('palmeira/municipio_palmeira.shp')

# Iterate over each row and save individual shapefiles
for index, row in gdf.iterrows():
    # Extract the 'cod_imovel' property
    cod_imovel = row['cod_imovel']

    # Filter the GeoDataFrame to get only the current row and save it
    single_item_gdf = gdf[gdf['cod_imovel'] == cod_imovel]
    output_filename = f"output/{cod_imovel}.shp"
    single_item_gdf.to_file(output_filename)
