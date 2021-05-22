import csv
import urllib.parse
import urllib.request

vcard_template = '''BEGIN:VCARD
VERSION:2.1
N:{};{}
FN:{} {}
ORG:Authors, Inc.
TITLE:{}
TEL;WORK;VOICE:{}
ADR;WORK:;;100 Flat Grape Dr.;Fresno;CA;95555;United States of America
EMAIL;PREF;INTERNET:{}
REV:20150922T195243Z
END:VCARD
'''

def createcard(fname, lname, title, phone, email):
    return vcard_template.format(lname,
                                fname,
                                fname, 
                                lname, 
                                title, 
                                phone, 
                                email)

def createcode(data):
    url_base = "https://chart.googleapis.com/chart?"
    params ={
        "cht" : "qr",
        "chs" : "400x400",
        "chl" : data
    }
    qs = urllib.parse.urlencode(params)
    full_url = "{}{}".format(url_base, qs)
    response = urllib.request.urlopen(full_url)
    response.read()

def parsecsv(csvfile):
    r = csv.reader(open(csvfile))
    for fname, lname, title, email, phone in r:
        vcard = createcard(fname, lname, title, phone, email)

        fname = "{}_{}.vcf".format(fname, lname)
        f = open(fname, "w")
        f.write(vcard)
        f.close

        qr_fname = "{}_{}.png".format(fname, lname)
        qrcode = createcode(vcard)
        f = open(qr_fname, "wb")
        f.write(qrcode)
        f.close

if __name__ == "__main__":
    parsecsv("authors.csv")


