from dotenv import load_dotenv
load_dotenv()

# ドキュメントローダーをインポート
from langchain.document_loaders import TextLoader
# ドキュメントローダーの初期化
loader = TextLoader('identityv.txt', encoding='utf-8')
# loader = TextLoader('data.txt', encoding='utf-8')

# インデックスの作成に用いるクラスをインポート
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper

# ベクターストアの作成
index: VectorStoreIndexWrapper = VectorstoreIndexCreator().from_loaders([loader])

query = "ディレクションをしているのはだれですか？"
answer = index.query(query)

print(answer)