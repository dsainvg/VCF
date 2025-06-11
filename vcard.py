from utils import genphn,genrev,gennote,genorg,genemail,genjob,genaddress,genfullname,genname

def gen_vcard(assign,row,version="2.1"):
    returntext = f"BEGIN:VCARD\nVERSION:{version}\n"
    name = []
    suffix = []
    
    for key, value in assign.items():
        key = key[:-1]
        if key.startswith("!"):
            value = value
            key = key[1:]  # Remove the '!' prefix
        else:
            value = row[value]
        value = str(value).strip()  
        if key.startswith("Name"):
            name.append(value)
        elif key.startswith("Suffix"):
            suffix.append(value)
    if not name:
        name = ["Unknown"]
    returntext += genname(name=name,suffix=suffix)
    name.extend(suffix)
    returntext += genfullname(name=name)
    
    for key, value in assign.items():
        key = key[:-1]  # Remove the last character which is a number
        if key.startswith("!"):
            value = value
            key = key[1:]
        else:
            value = row[value]
        value = str(value).strip()  
        if key.startswith("Phone Number"):
            returntext += genphn(key, value)
        elif key.startswith("Name"):
            continue
        elif key.startswith("Suffix"):
            continue
        elif key.startswith("NOTE"):
            returntext += gennote(value)
        elif key == "Organization":
            returntext += genorg(value)
        elif key.startswith("Email"):
            returntext += genemail(key, value)
        elif key.startswith("Job"):
            returntext += genjob(value)
        elif key.startswith("Address"):
            returntext += genaddress(value)

    returntext += genrev()
    returntext += "END:VCARD\n"
    return returntext