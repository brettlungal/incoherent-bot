import uuid

class Persistence:

    def __init__(self,db, cursor):
        self.db = db
        self.cursor = cursor

    def get_sink_count(self) -> int:
        query_string = f"SELECT COUNT(*) FROM sinks"
        self.cursor.execute(query_string)
        count = self.cursor.fetchone()
        return int(count[0])

    def add_sink(self, boatname=None) -> None:
        if boatname is None:
            boatname  = "None"
        sink_id = str(uuid.uuid4())
        add_sink = ("INSERT INTO sinks "
                    "(id, boatname) "
                    "VALUES (%s, %s)")
        sink_data = (sink_id, boatname)
        self.cursor.execute(add_sink,sink_data)
        self.db.commit()

    