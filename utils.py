import time
import re

def revgen():
    t = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current time: {t}")
    t = t.replace(":","")
    t= t.replace(" ","T")
    t = t.replace("-","")
    t = t+"Z"
    return t

def genrev():
    return f"REV:{revgen()}\n"

def genphn(phn,number):
    if phn == "Phone Number+Mobile":
        return f"TEL;TYPE=CELL:{number}\n"
    elif phn == "Phone Number+Work":
        return f"TEL;TYPE=WORK:{number}\n"
    elif phn == "Phone Number+Home":
        return f"TEL;TYPE=HOME:{number}\n"
    else:
        return f"TEL:{number}\n"
    
def gennote(note):
    if note:
        return f"NOTE:{note}\n"
    else:
        return "\n"

def genorg(organization):
    if organization:
        return f"ORG:{organization}\n"
    else:
        return "\n"

def genemail(email_type, email):
    if email_type == "Email+Work":
        return f"EMAIL;TYPE=WORK:{email}\n"
    elif email_type == "Email+Home":
        return f"EMAIL;TYPE=HOME:{email}\n"
    elif email_type == "Email+Other":
        return f"EMAIL;TYPE=OTHER:{email}\n"
    else:
        return f"EMAIL:{email}\n"
    
def genjob(job_title):
    if job_title:
        return f"TITLE:{job_title}\n"
    else:
        return "\n"

def genaddress(address):
    if address:
        return f"ADR:{address}\n"
    else:
        return "\n"

def genfullname(name):
    fn = ""
    for i in name:
        if i:
            fn += i + " "
    fn = fn.strip()
    if not fn:
        fn = "Unknown"
    
    return f"FN:{fn}\n"

def genname(name,suffix):
    name = " ".join(name)
    name = name.strip()
    name = name + ";;;;"
    name = name+ " ".join(suffix)
    return f"N:{name}\n"

def textedit(text):
    if text:
        text = re.sub(r'[^A-Za-z\s]', ' ', text)
        return text.strip()
    else:
        return ""
