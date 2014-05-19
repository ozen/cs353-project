def getCityList():
	cursor = connection.cursor()
	cursor.execute(''' SELECT DISTINCT city FROM Terminal ORDER BY city ''')
	cities = cursor.fetchall()
	return cities