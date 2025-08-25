from configparser import ConfigParser
from typing import Self


class Config:
    def __init__(self, filename: str = "./src/LanggraphagenticAI/ui/uiconfigfile.ini"):
        self.config = ConfigParser()
    
        self.config.read(filename)
        self.defaults = self.config["DEFAULT"] 
    

    @property
    def page_title(self) -> str:
        return self.defaults.get("PAGE_TITLE")

    @property
    def llm_options(self):
        return self.defaults.get("LLM_OPTIONS", "None").split(",")

    @property
    def usecase_options(self):
        return self.defaults.get("USECASE_OPTIONS").split(",")

    @property
    def groq_model_options(self) -> list:
        # Split the comma-separated list and strip whitespace
        value = self.defaults.get("GROQ_MODEL_OPTIONS", "")
        return [v.strip() for v in value.split(",") if v.strip()]

    @property
    def AI_NEWS_OPTIONS(self):
        return self.defaults.get("AI_NEWS_OPTIONS", "None").split(",")
    
            
    