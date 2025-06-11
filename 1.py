def generate_vcard(filename):
    vcard = """BEGIN:VCARD
VERSION:4.0
FN:Simon Perreault
N:Perreault;Simon;;;ing. jr,M.Sc.
BDAY:--0203
GENDER:M
EMAIL;TYPE=work:simon.perreault@viagenie.ca
END:VCARD
"""
    with open(filename, 'w') as f:
        f.write(vcard)

if __name__ == "__main__":
    generate_vcard("contact.vcf")
