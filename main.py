import sqlite3
import datetime
def getColumns(table_name):
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    cur.execute("PRAGMA table_info({})".format(table_name))
    columnInfo = cur.fetchall()
    if not columnInfo:
        raise ValueError(f"{table_name}: DOES NOT EXIST")

    return columnInfo

def getData(columns):
    new_data = []
    value = ''
    for i in range(len(columns)):
        if(columns[i][2] == "INT" or columns[i][2] == "int"):
            value = str(int(input(f"Enter {columns[i][1]}: ")))
            new_data.append(value)

        elif(columns[i][2] == "TEXT"):
            value = input(f"Enter {columns[i][1]}: ")
            new_data.append(value)
            
        elif (columns[i][2] == "decimal"):
            value = str(float(input(f"Enter {columns[i][1]}: ")))
            new_data.append(value)

        elif(columns[i][2] == "CURRENT_DATE" or columns[i][2] == "CURRENT_TIMESTAMP"):
            current_date = datetime.datetime.now()
            formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
            value = formatted_datetime
            new_data.append(value)

        else:
            value = ''

    print(f"DATA: {new_data}")
    return new_data

def getQuery(table_name, data, columns):
    columnNames = [column[1] for column in columns]

    # Convert each value to its string representation while maintaining data types
    values = []
    for i, value in enumerate(data):
        if columns[i][2] == "INT":
            values.append(str(int(value)))
        elif isinstance(value, str):
            values.append(f"'{value}'")
        else:
            values.append(repr(value))

    # Construct the INSERT statement dynamically
    values_str = ", ".join(values)
    insertQuery = "INSERT INTO {} ({}) VALUES ({})".format(
        table_name,
        ", ".join(columnNames),
        values_str
    )
    return insertQuery

def insert(query):
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    try:
        cur.execute(query)
        con.commit()
    except:
        print("ERROR")

table_name = input("Enter the table name: ")
columns = getColumns(table_name)
data = getData(columns)

query = getQuery(table_name,data,columns)
print(query)

insert(query)






