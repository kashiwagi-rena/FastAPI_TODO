from api.settings.env import Env
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base

# データベースの接続情報の設定
_database_url = URL.create(
    drivername="mysql+mysqldb",
    username=Env.DATABASE_USER,
    password=Env.DATABASE_PASSWORD,
    host=Env.DATABASE_HOST,
    port=Env.DATABASE_PORT,
    database=Env.DATABASE_NAME
)

# データベースエンジンを作成
Engine = create_engine(_database_url, echo=True)
# セッションファクトリを作成
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=Engine)
# モデルを定義するための基本となるBaseクラスを作成
Base = declarative_base()

# セッションを依存性として定義
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
