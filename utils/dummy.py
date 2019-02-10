import json

party = json.dumps(dict(
    id=1,
    name="Blue",
    hqAddress="Memphis",
    logoUrl="blue.img"
))

party_edit_data = json.dumps(dict(
    id=1, 
    name="Red", 
    hqAddress="Addis", 
    logoUrl="red.img"
))

party_blank_name = json.dumps(dict(
    id=1,
    name="",
    hqAddress="Belgrade",
    logoUrl="logo.png"
))

party_blank_hqAddress = json.dumps(dict(
    id=1,
    name="Jubilee",
    hqAddress="",
    logoUrl="logo.png"
))

party_blank_logoUrl = json.dumps(dict(
    id=1,
    name="Jubilee",
    hqAddress="Kent",
    logoUrl=""
))

party_non_string_name = json.dumps(dict(
    id=1,
    name=5,
    hqAddress="Kent",
    logoUrl="kent.png"
))

empty_data_party = json.dumps(dict(
    
))

office = json.dumps(dict(
    id=1,
    type="National",
    name="Presidential"
))