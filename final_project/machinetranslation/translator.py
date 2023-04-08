"""Translator.py

Using IBM Watson for translating French to English 
and vice-verca

Author : Lesego Sebusi
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['APIKey']
url = os.environ['URL']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
def english_to_french(english_text):
    """
    For translating english to french 
    This function doesn't allow empty input    
    """
    if not english_text:
        return ""
    frechtranslation = language_translator.translate(
        text=english_text, model_id="en-fr").get_result()
    return frechtranslation.get("translations")[0].get("translation")


def french_to_english(french_text):
    """
    For translating french to english 
    This function doesn't allow empty input    
    """
    if not french_text:
        return ""
    englishtranslation = language_translator.translate(
        text=french_text, model_id="fr-en").get_result()
    return englishtranslation.get('translations')[0].get('translation')
