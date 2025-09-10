import re
import base64
class TextClassificationHelper:

    def __init__(self):
        self._base64_dangerous_vocabulary = "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="
        self._base64_very_dangerous_vocabulary = "R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT"
        self._dangerous_vocabulary = TextClassificationHelper.decoded_base_64(self._base64_dangerous_vocabulary).lower().split(',')
        self._very_dangerous_vocabulary = TextClassificationHelper.decoded_base_64(self._base64_very_dangerous_vocabulary).lower().split(',')


    @staticmethod
    def decoded_base_64(encoded_string) -> str:
        return base64.b64decode(encoded_string).decode()


    @staticmethod
    def classification_by_category(score) -> str:
        result = None
        if score < 0.005:
            result = 'none'
        elif score > 0.007:
            result = 'high'
        else:
            result = 'medium'
        return result



    @staticmethod
    def is_risk(score):
        return True if score >= 0.005 else False

    @staticmethod
    def performances_and_variety(bank:list, text:str) -> dict:
        performance_counter = 0
        variety_counter = 0
        dic = {}

        for word_from_bank in bank:
            performances = re.findall(rf'\b{word_from_bank}\b', text.lower())
            if performances:
                performance_counter += len(performances)
                variety_counter += 1

        dic['performances_precent'] = performance_counter / len(text.split())
        dic['variety_precent'] = variety_counter / len(bank)
        return dic


    def calculate_text_classification(self, text) -> float:
        dangerous_vocabulary_data = TextClassificationHelper.performances_and_variety(self._dangerous_vocabulary, text)
        very_dangerous_vocabulary_data = TextClassificationHelper.performances_and_variety(self._dangerous_vocabulary, text)

        words_performances_precent = dangerous_vocabulary_data['performances_precent']/2 + \
                                                     very_dangerous_vocabulary_data['performances_precent']
        performance_diversity_percent = dangerous_vocabulary_data['variety_precent'] * very_dangerous_vocabulary_data[
            'variety_precent']
        return words_performances_precent * performance_diversity_percent

