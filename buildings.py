# Copyright 2011 Omniscale (http://omniscale.com)
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from imposm.mapping import (
  Options,
  Points, LineStrings, Polygons,
  String, Bool, Integer, OneOfInt,
  set_default_name_type, LocalizedName,
  WayZOrder, ZOrder, Direction,
  GeneralizedTable, UnionView,
  PseudoArea, meter_to_mapunit, sqr_meter_to_mapunit,
)

# # internal configuration options
# # uncomment to make changes to the default values
import imposm.config
# 
# # import relations with missing rings
imposm.config.import_partial_relations = False
# 
# # select relation builder: union or contains
imposm.config.relation_builder = 'contains'
# 
# # log relation that take longer than x seconds
# imposm.config.imposm_multipolygon_report = 60
# 
# # skip relations with more rings (0 skip nothing)
# imposm.config.imposm_multipolygon_max_ring = 0


# # You can prefer a language other than the data's local language
# set_default_name_type(LocalizedName(['name:en', 'int_name', 'name']))

db_conf = Options(
  # db='osm',
  host='localhost',
  port=5432,
  user='osm',
  password='osm',
  sslmode='allow',
  prefix='osm_new_',
  proj='epsg:900913',
)

address_tags = (
  ('addr:housenumber',String()),
  ('addr:housename', String()),
  ('addr:street', String()),
  ('addr:place', String()),
  ('addr:city', String()),
  ('addr:country', String()),
  ('addr:full', String()),
  ('addr:hamlet', String()),
  ('addr:subdistrict', String()),
  ('addr:district', String()),
  ('addr:province', String()),
  ('addr:state', String()),
)

buildings = Polygons(
  name = 'buildings',
  fields = address_tags,
  mapping = {
    'building': (
      '__any__',
    ),
  }
)