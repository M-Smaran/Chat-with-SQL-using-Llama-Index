import os 
from langchain.agents import *
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import AgentExecutor
os.environ["OPEN_API_KEY"] = os.getenv("OPEN_API_KEY")
load_dotenv()

class ChatwithSQL:
    """ChatwithSql class is use for chat and query user question with the SQL database"""
    def __init__(self,db_user,db_password,db_host,db_name):
       """ This is a constructor method for chatsql class"""
       self.db_user = db_user
       self.db_password = db_password
       self.db_host = db_host
       self.db_name = db_name
       
    def message(self,query):
        """_summary_

        Args:
            query (_type_): _description_
        """
        # Initializing the llm
        llm = ChatOpenAI(model_name = "gpt-3.5-turbo")
        #Initializeing the toolkit 
        toolkit = SQLDatabaseToolkit(db=db,llm=llm)
        #Creatig the agent executor
        agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True
        )
        
        
        response = agent_executor.run(query)
        return response
    
obj =  ChatwithSql("root",12345,"localhost","ahi_database")
obj.message("How many rows do we have in cattle table?")