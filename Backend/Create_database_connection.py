from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy


def connect():
    connector = Connector()

    def getconn():
        conn = connector.connect(
            "planar-method-425304-t6:us-central1:shop-management-data", # Cloud SQL Instance Connection Name
            "pymysql",
            user="root",
            password="",
            db="shop_data",
            ip_type=IPTypes.PUBLIC # IPTypes.PRIVATE for private IP
        )
        return conn
    
    pool = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn,)
    
    return pool.connect(), connector
    
def disconnect(connector):
    connector.close()
