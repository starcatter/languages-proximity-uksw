from googletrans import Translator
import mysql.connector
import asyncio
from codetiming import Timer

async def test(connection, tableName,mycursor,translator,language,short):
    cursor = connection.cursor()
    sql_select_Query = "select * from " + str(tableName).replace("(", "").replace(")", "").replace(",",
                                                                                                   "").replace(
        "'", "")
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)
    for row in records:
        tlumaczenie = ""
        try:
            tlumaczenie = translator.translate(row[22], src='en', dest=short).text.replace("'", "").replace("`", "")
            print(tlumaczenie)
            sql_update_Query = "UPDATE `" + str(tableName).replace("(", "").replace(")", "").replace(",",
                                                                                                     "").replace(
                "'", "") + "` SET `"+language+"` = '" + tlumaczenie + "' WHERE `" + str(tableName).replace("(",
                                                                                                     "").replace(
                ")", "").replace(",", "").replace("'", "") + "`.`id` = " + str(
                row[21]) + ";"
            mycursor.execute(sql_update_Query)
            connection.commit()
        except Exception as e:
            print(e)

async def main(language,short):
    translator = Translator()

    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='',
                                             user='',
                                             password='')

        mycursor = connection.cursor()
        mycursor.execute("Show tables;")

        myresult = mycursor.fetchall()
        # for tableName in myresult:
        with Timer(text="\nTotal elapsed time: {:.1f}"):
            await asyncio.gather(
                asyncio.create_task(test(connection, myresult[0], mycursor, translator, language, short)),
            )


    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")


if __name__ == '__main__':
    asyncio.run(main("french", "fr"))
