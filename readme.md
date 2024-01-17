# Сравнение 2-ух текстов на схожесть с помощью ML NLP
## Разработано: Заложный Виталий Евгеньевич(130906)
### Принцип работы программы:
```
1.Сравнение текстов будет происходить при помощи sentence_transformers.
2. model для сравнения: sentence-transformers/all-MiniLM-L6-v2
```
ссылка на проект Streamlit: https://comparetexts-xy4ygxexs2f6g7y3dkstbh.streamlit.app/
## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Odds112/compare_Texts.git
   cd compare_Texts.git

   pip install -r requirements.txt

   streamlit run sl_main.py

## Пример работы проекта на StreamLit
![image](https://github.com/Odds112/compare_Texts/assets/83842891/0bc68d45-4a75-4b28-b88a-c16881b78e8d)



## Зависимости

- [Streamlit](https://streamlit.io/)
- [SentenceTransformer](https://www.sbert.net/)
