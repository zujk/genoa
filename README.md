# Genoa in voxels

A port of [stared/warsaw-vibe-voxel](https://github.com/stared/warsaw-vibe-voxel) (MIT, © 2026 Piotr Migdał) to Genoa: a 5600 × 3500 m diorama of the centre at 1 m voxels, from the Lanterna and the port in the west to Brignole in the east, anchored on Piazza De Ferrari.

## Status: scaffold, not yet built

The viewer (`web/`) and the data pipeline (`scripts/`) are copied from the Warsaw project and re-pointed at Genoa. **No Genoa data has been generated yet and nothing here has been run**: the session that did the port had no network access to Geofabrik, Overpass or the Liguria geoportal.

Done:
- `scripts/aoi.py`: Genoa AOI, EPSG:32632 (UTM 32N), axis-aligned. The anchor coordinates are approximate.
- `scripts/fetch_osm.sh`: reads the Geofabrik `nord-ovest` extract instead of Mazowieckie. CRS changed to 32632 in the scripts.
- Viewer: title, search box, credits and sun position (44.41° N, 8.93° E) changed to Genoa.

Still to do:
1. **Elevation and imagery.** `scripts/fetch_gugik.sh` is a stub. Pick Italian sources (Regione Liguria LiDAR DSM/DTM and orthophoto, or the national LiDAR) and adapt `scripts/prep.py`.
2. **Warsaw-specific code.** `scripts/voxelize.py` imports a curated `landmarks.py` (not copied: it is keyed to Warsaw OSM ids), finds the Palace of Culture by name, and uses Warsaw's tree register (`fetch_trees.py`, `trees.py`), the Vistula flood gauge (`flood.py`) and tram livery. Each needs replacing, stubbing or removing. Genoa equivalents would be the Lanterna, the Porto Antico, the Righi funicular and the Morandi-bridge replacement (Ponte San Giorgio), with the sea in place of the river.
3. **Check the AOI** against OSM once data is available, and `pnpm dev` on the output.

Viewer: `cd web && pnpm install && pnpm dev`. Pages deploy via `.github/workflows/pages.yml`.

## License

Code under the MIT license (see `LICENSE`, © 2026 Piotr Migdał). Generated data derived from OpenStreetMap is under the ODbL (© OpenStreetMap contributors).
