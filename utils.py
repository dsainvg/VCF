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
    number = str(number)
    number = number.strip()
    number = re.sub(r'[^0-9]', '', number)  # Remove non-numeric characters
    if "." in number:
        number = number.split(".")[0]
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

def columncheck(req):
    columnoptions = ["NONE","Address", "Name", "Phone Number", "Email","Suffix","Organization", "Job Title","NOTE"]
    if req in columnoptions:
        return req
    req = req.strip()
    req = req.lower()
    Nameoptions = ["name","full name","name","fullname"]
    addressoptions = ["address","address work","address home","hall of residence","residence","hall","home address","work address","office address","location","place of residence"]
    phoneoptions = ["phone number","phone","mobile","ph no","mobile number","cell","home phone","work phone","business phone","business fax","mobile no"]
    emailoptions = ["email","email work","email home","email other","email personal","gmail","outlook","yahoo","hotmail","icloud","mail","work mail","personal mail","mailid","email id", "email address", "mail id"]
    companyoptions = ["company","organization","org","company name","organization name","org name"]
    noteoptions = ["note","department","notes","comment","comments","description","remarks","feedback","observation","annotation","branch"]
    jobtitleoptions = ["job title","job","designation","position","role","occupation","profession","work title","work position"]
    suffixoptions = ["suffix","name suffix","title suffix","honorific suffix","post-nominal letters","post-nominal title","post-nominal suffix"]
    if req in Nameoptions:
        return "Name"
    elif req in addressoptions:
        return "Address"
    elif req in phoneoptions:
        return "Phone Number"
    elif req in emailoptions:
        return "Email"
    elif req in jobtitleoptions:
        return "Job Title"
    elif req in companyoptions:
        return "Organization"
    elif req in noteoptions:
        return "NOTE"
    elif req in suffixoptions:
        return "Suffix"
    else:
        return ''