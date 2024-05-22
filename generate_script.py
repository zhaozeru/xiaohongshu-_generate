# 这里写所有和AI大模型交互的代码
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from prompt_template import system_template_text, user_template_text
from xiaohongshu_model import Xiaohongshu

def generate_xiaohongshu(theme, apikey):
    prompt = ChatPromptTemplate.from_messages([
            ('system', system_template_text),
            ('user', user_template_text)
        ])
    model = ChatOpenAI(model = 'gpt-3.5-turbo', openai_api_key = apikey, openai_api_base = "https://api.aigc369.com/v1")
    output_parser = PydanticOutputParser(pydantic_object = Xiaohongshu)
    chain = prompt | model | output_parser
    result = chain.invoke({
        'parser_instructions': output_parser.get_format_instructions(),
        'theme': theme
    })
    return result

