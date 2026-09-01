import re
from typing import cast

import deep_translator  # pyright: ignore[reportMissingTypeStubs]
from deep_translator import (  # pyright: ignore[reportMissingTypeStubs]
    GoogleTranslator,
    LingueeTranslator,
    MyMemoryTranslator,
    PonsTranslator,
)
from deep_translator.base import (  # pyright: ignore[reportMissingTypeStubs]
    BaseTranslator,
)
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    DEEPL_API: str = Field(default="provide_API_key")
    translator: BaseTranslator = GoogleTranslator()
    translator_name: str = "Google Translator"
    DEFAULT_SOURCE: str = "auto"
    source: str = "auto"
    DEFAULT_TARGET: str = "en"
    target: str = "en"
    DEFAULT_SOURCE_TITLE: str = "Auto"
    DEFAULT_TARGET_TITLE: str = "English"

    def get_available_translators(self) -> list[tuple[str, str]]:
        available_translators = deep_translator.__all__[0:4]
        result = cast(list[tuple[str, str]], [])

        for item in available_translators:
            if "Translator" in item:
                display_name = ""
                for word in re.findall("[a-zA-Z][^A-Z]*", item):
                    display_name += word
                    display_name += " "
                result.append((display_name.strip(), item))

        return result

    def set_translator(self, name: str) -> None:
        all = deep_translator.__all__
        if name == all[0]:
            self.translator = GoogleTranslator()
            self.translator_name = "Google Translator"
        if name == all[1]:
            self.translator = PonsTranslator("en")
            self.translator_name = "Pons Translator"
        if name == all[2]:
            self.translator = LingueeTranslator("english", "english")
            self.translator_name = "Linguee Translator"
        if name == all[3]:
            self.translator = MyMemoryTranslator(target="en-US")
            self.translator_name = "MyMemory Translator"
        # Not implemented yet
        # if name == all[4]:
        #     self.translator = YandexTranslator()
        #     self.translator_name = "Yandex Translator"
        # if name == all[5]:
        #     self.translator = MicrosoftTranslator()
        #     self.translator_name = "Microsoft Translator"
        # if name == all[6]:
        #     self.translator = QcriTranslator()
        #     self.translator_name = "Qcri Translator"
        # if name == all[7]:
        #     self.translator = DeeplTranslator()
        #     self.translator_name = "Deepl Translator"
        # if name == all[8]:
        #     self.translator = LibreTranslator()
        #     self.translator_name = "Libre Translator"
        # if name == all[9]:
        #     self.translator = PapagoTranslator()
        #     self.translator_name = "Papago Translator"
        # if name == all[10]:
        #     self.translator = ChatGptTranslator()
        #     self.translator_name = "ChatGpt Translator"
        # if name == all[11]:
        #     self.translator = BaiduTranslator()
        #     self.translator_name = "Baidu Translator"


# Initialize once to share across the application
settings = Settings()
