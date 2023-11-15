post and get portion can be found at 
https://www.tutorialspoint.com/nodejs/nodejs_express_framework.htm

mysql connection can be found at 
https://www.npmjs.com/package/mysql2



install mysql2 instead of mysql
The link below explains the issue with using mysql
https://stackoverflow.com/questions/50093144/mysql-8-0-client-does-not-support-authentication-protocol-requested-by-server/56509065#56509065

using link as css reference
https://codepen.io/chriscoyier/pen/vWEMWw

creating table from json results
https://www.tutorialspoint.com/how-to-convert-json-data-to-a-html-table-using-javascript-jquery

 '''
    data = [
      ('Jane', date(2005, 2, 12)),
      ('Joe', date(2006, 5, 23)),
      ('John', date(2010, 10, 3)),
    ]
    stmt = "INSERT INTO employees (first_name, hire_date) VALUES (%s, %s)"
    cursor.executemany(stmt, data)
sample_list = ['Compile', 'With', 'Favtutor']

#convert list into tuple
tuple1 = tuple(sample_list)