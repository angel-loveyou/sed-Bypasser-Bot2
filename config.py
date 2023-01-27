import os


class Config(object):
    bot_token = os.environ.get("TOKEN", "5860879943:AAGB-DH_yrmc3MRwXWH8QuyzakO2UtFcZxk")
    api_hash = os.environ.get("HASH", "1c521005e55c95e6973ae714d2e9e424") 
    api_id = os.environ.get("ID", "7234399")
    GDTot_Crypt = os.environ.get("CRYPT","RHdWM1VmNWlIUE5Wd3hGQ0ZUZE5lVUQ0L2JhKzJYNXZyeDUrQWtnamcxbz0%3D")
    Laravel_Session = os.environ.get("Laravel_Session","")
    XSRF_TOKEN = os.environ.get("XSRF_TOKEN","")
    DCRYPT = os.environ.get("DRIVEFIRE_CRYPT","")
    KCRYPT = os.environ.get("KOLOP_CRYPT","aWFicnVaNWh4TThRbzFqdkE2U2FKNmJOTWhvWkZmbWswaUFadTB5NXJ3RT0%3D")
    HCRYPT = os.environ.get("HUBDRIVE_CRYPT","Q29hdlpLUEZTSEJLUjVZRkZQSExLODFuWGVudUlNK0ZPZlZmS1hENWxZVT0%3D")
    KATCRYPT = os.environ.get("KATDRIVE_CRYPT","")
