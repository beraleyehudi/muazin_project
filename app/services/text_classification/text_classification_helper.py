import re
class TextClassificationHelper:

    def __init__(self):
        self._word_bank_1 = None
        self._word_bank_2 = None

    @staticmethod
    def decrypt_base_64(base_64_text) -> str:
        pass


    def classification_by_category(self, score) -> str:
        pass

    def is_risk(self, score):
        pass

    @staticmethod
    def performances_and_variety(bank:list, text:str) -> dict:
        performance_counter = 0
        variety_counter = 0
        dic = {}

        for word_from_bank in bank:
            performances = re.findall(rf'\b{word_from_bank}\b', text)
            if performances:
                variety_counter += 1
                performance_counter += len(performances)

        dic['performances_precent'] = performance_counter / len(text.split())
        dic['variety_precent'] = variety_counter / len(bank)
        return dic


    def calculate_text_classification(self, text) -> float:
        hostile_words_1_data = TextClassificationHelper.performances_and_variety(self._word_bank_1, text)
        hostile_words_2_data = TextClassificationHelper.performances_and_variety(self._word_bank_2, text)

        percentage_of_dangerous_words_performances = hostile_words_1_data['performances_precent'] + \
                                                     hostile_words_2_data['performances_precent']
        performance_diversity_percentage = hostile_words_1_data['variety_precent'] * hostile_words_2_data[
            'variety_precent']
        return performance_diversity_percentage

