from pydantic_settings import BaseSettings,SettingsConfigDict

class Config(BaseSettings):
    GROQ_API_KEY : str
    GOOGLE_API_KEY : str
    OPENAI_API_KEY : str

    model_config = SettingsConfigDict(env_file="env")

config = Config() 