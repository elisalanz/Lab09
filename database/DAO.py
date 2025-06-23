from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass


    @staticmethod
    def getAllFlights():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID, DISTANCE
                    from flights"""
        cursor.execute(query)
        for row in cursor:
            result.append((row["ORIGIN_AIRPORT_ID"], row["DESTINATION_AIRPORT_ID"], row["DISTANCE"]))
        cursor.close()
        conn.close()
        return result
