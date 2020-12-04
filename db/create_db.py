import csv, sqlite3

# con = sqlite3.connect("C:/sqlite/poc/source.db")
# cur = con.cursor()
#
# with open("C:/sqlite/poc/csvfiles/claims.csv") as data:
#     dr = csv.DictReader(data)
#     to_db = [(i['ID'], i['CLAIM_ID'], i['MEMBER_ID'], i['START_DATE'], i['END_DATE'], i['CLAIM_AMOUNT']) for i in dr]
#
# cur.executemany("INSERT INTO claims(ID, CLAIM_ID, MEMBER_ID, START_DATE, END_DATE, CLAIM_AMOUNT) values(?,?,?,?,?,?);", to_db)
# con.commit()
# con.close()

# con = sqlite3.connect("C:/sqlite/poc/source.db")
# cur = con.cursor()
#
# with open("C:/sqlite/poc/csvfiles/members.csv") as data:
#     dr = csv.DictReader(data)
#     to_db = [(i['ID'], i['FIRST_NAME'], i['LAST_NAME'], i['DOB'], i['MEMBER_ID'], i['SSN'], i['ADDRESS1'], i['ADDRESS2'], i['CITY'], i['STATE'], i['ZIP']) for i in dr]
#
# cur.executemany("INSERT INTO members(ID, FIRST_NAME, LAST_NAME, DOB, MEMBER_ID, SSN, ADDRESS1, ADDRESS2, CITY, STATE, ZIP) values(?,?,?,?,?,?,?,?,?,?,?);", to_db)
# con.commit()
# con.close()

# con = sqlite3.connect("C:/sqlite/poc/destination.db")
# cur = con.cursor()
#
# with open("C:/sqlite/poc/csvfiles/reports.csv") as data:
#     dr = csv.DictReader(data)
#     to_db = [(i['ID'], i['NAME'], i['DOB'], i['MEMBER_ID'], i['SSN'], i['ADDRESS'], i['CITY'], i['STATE'], i['ZIP'], i['CLAIM_COUNT'], i['TOTAL_AMOUNT']) for i in dr]
#
# cur.executemany("INSERT INTO reports(ID, NAME, DOB, MEMBER_ID, SSN, ADDRESS, CITY, STATE, ZIP, CLAIM_COUNT, TOTAL_AMOUNT) values(?,?,?,?,?,?,?,?,?,?,?);", to_db)
# con.commit()
# con.close()