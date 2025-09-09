class TextClassificationHelper:
    @staticmethod
    def performances_and_variety(hostile_words, text) -> dict:
        counter = 0
        lis = []
        dic = {'performances_precent': 0, 'variety_precent': 0}
        for i in text.split(','):
            if f'{i}' in hostile_words:
                counter += 1
                if not f'{i}' in lis:
                    lis.append(i)

        dic['performances_precent'] = counter / len(text.split(','))
        dic['variety_precent'] = len(lis) / len(hostile_words)
        return dic

    @staticmethod
    def calculate_text_classification(hostile_words_1, hostile_words_2, text):
        hostile_words_1_data = TextClassificationHelper.performances_and_variety(hostile_words_1, text)
        hostile_words_2_data = TextClassificationHelper.performances_and_variety(hostile_words_2, text)

        percentage_of_dangerous_words_performances = hostile_words_1_data['performances_precent'] + \
                                                     hostile_words_2_data['performances_precent']
        performance_diversity_percentage = hostile_words_1_data['variety_precent'] * hostile_words_2_data[
            'variety_precent']