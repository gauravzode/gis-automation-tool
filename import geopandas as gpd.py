import geopandas as gpd

gdf = gpd.read_file("result.shp")
gdf.to_csv("result.csv", index=False)

print("✅ CSV created")