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

office = json.dumps(dict(
    id=1,
    type="National",
    name="Presidential"
))