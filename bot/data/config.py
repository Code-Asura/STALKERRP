from pydantic import SecretStr

from pydantic_settings import BaseSettings, SettingsConfigDict

class Config_class(BaseSettings):
    token: SecretStr

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

config = Config_class