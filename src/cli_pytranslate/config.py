import deep_translator  # pyright: ignore[reportMissingTypeStubs]
from deep_translator import (  # pyright: ignore[reportMissingTypeStubs]
    BaiduTranslator,
    ChatGptTranslator,
    DeeplTranslator,
    GoogleTranslator,
    LibreTranslator,
    LingueeTranslator,
    MicrosoftTranslator,
    MyMemoryTranslator,
    PapagoTranslator,
    PonsTranslator,
    QcriTranslator,
    YandexTranslator,
)
from deep_translator.base import (  # pyright: ignore[reportMissingTypeStubs]
    BaseTranslator,
)
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    DEEPL_API: str = Field(default="provide_API_key")
    default_translator: BaseTranslator = GoogleTranslator()
    default_translator_name: str = "Google Translator"
    DEFAULT_SOURCE: str = "auto"
    DEFAULT_TARGET: str = "en"
    DEFAULT_SOURCE_TITLE: str = "Auto"
    DEFAULT_TARGET_TITLE: str = "English"

    def get_available_translators(self) -> list[str]:
        all = deep_translator.__all__
        result = []

        for item in all:
            if "Translator" in item:
                result.append(item)  # pyright: ignore[reportUnknownMemberType]

        return result  # pyright: ignore[reportUnknownVariableType]

    def set_default_translator(self, name: str) -> None:
        all = deep_translator.__all__
        if name == all[0]:
            self.default_translator = GoogleTranslator()
            self.default_translator_name = "Google Translator"
        if name == all[1]:
            self.default_translator = PonsTranslator("en")
            self.default_translator_name = "Pons Translator"
        if name == all[2]:
            self.default_translator = LingueeTranslator()
            self.default_translator_name = "Linguee Translator"
        if name == all[3]:
            self.default_translator = MyMemoryTranslator()
            self.default_translator_name = "MyMemory Translator"
        if name == all[4]:
            self.default_translator = YandexTranslator()
            self.default_translator_name = "Yandex Translator"
        if name == all[5]:
            self.default_translator = MicrosoftTranslator()
            self.default_translator_name = "Microsoft Translator"
        if name == all[6]:
            self.default_translator = QcriTranslator()
            self.default_translator_name = "Qcri Translator"
        if name == all[7]:
            self.default_translator = DeeplTranslator()
            self.default_translator_name = "Deepl Translator"
        if name == all[8]:
            self.default_translator = LibreTranslator()
            self.default_translator_name = "Libre Translator"
        if name == all[9]:
            self.default_translator = PapagoTranslator()
            self.default_translator_name = "Papago Translator"
        if name == all[10]:
            self.default_translator = ChatGptTranslator()
            self.default_translator_name = "ChatGpt Translator"
        if name == all[11]:
            self.default_translator = BaiduTranslator()
            self.default_translator_name = "Baidu Translator"


# Initialize once to share across the application
settings = Settings()
translator = settings.default_translator
