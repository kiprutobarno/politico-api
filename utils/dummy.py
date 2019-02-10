import json

# party dummies
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

party_missing_name_key = json.dumps(dict(
    id=1, 
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

party_non_string_hqAddress = json.dumps(dict(
    id=1,
    name="Jubilee",
    hqAddress=7,
    logoUrl="kent.png"
))

empty_data_party = json.dumps(dict(
    
))

existing_party = json.dumps(dict(
    id=1,
    name="Blue",
    hqAddress="Memphis",
    logoUrl="blue.img"
))


# office dummies
office = json.dumps(dict(
    id=1,
    type="National",
    name="Presidential"
))

office_missing_name_key = json.dumps(dict(
    id=1, 
    type="National"
))
office_empty_body = json.dumps(dict(
    
))

office_empty_type = json.dumps(dict(
    id=1,
    type="",
    name="Presidential"
))

office_empty_name = json.dumps(dict(
    id=1,
    type="National",
    name=""
))

non_string_office_name = json.dumps(dict(
    id=1,
    type="National",
    name=5
))

non_string_office_type = json.dumps(dict(
    id=1,
    type=5,
    name="Presidential"
))