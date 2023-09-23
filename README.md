# CodeBot
![image](https://img.shields.io/badge/-LangChain-32CD32?logo=LangChain&logoColor=white&style=for-the-badge)
![image](https://img.shields.io/badge/-llama2_7b-0467DF.svg?style=for-the-badge&logo=Meta&logoColor=white)
![image](https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white)
![image](https://img.shields.io/badge/StableCode-5E5E5E.svg?style=for-the-badge&logo=Microsoft&logoColor=white)

This app allows users to ask code-related questions and receive generated code snippets as answers. The app leverages powerful AI models and datasets to understand natural language code queries and provide targeted responses. It utilizes Microsoft's StableCode AI (https://huggingface.co/stabilityai/stablecode-instruct-alpha-3b) model to process users' questions and comprehend the programming task or issue being described. For representing code embeddings, the app leverages the pre-trained UnixCoder model from Microsoft (https://huggingface.co/microsoft/unixcoder-base). On the backend, the popular LangChain framework is implemented to orchestrate the models and handle the NLP pipeline. Two relevant open-source datasets  GPTeacher and CodeAlpaca -(https://github.com/teknium1/GPTeacher)-(https://github.com/sahil280114/codealpaca)- are also utilized to provide the models with code task instructions and examples to help inform their responses. The simple and intuitive frontend is built with Streamlit, making the app easily accessible directly through a web browser

![Alt text](<Screenshot 2023-09-23 180536.png>)

## Deployment

To deploy this project run

1:
```bash
  git clone https://github.com/AminHaghdadi/CodeBot.git
```
2: install requirements:
```bash
  pip install -r requirement.txt 
```
3:
Download the Stablecode-alpha-3b model from this link :
[StableCode](https://huggingface.co/TheBloke/stablecode-instruct-alpha-3b-GGML/resolve/main/stablecode-instruct-alpha-3b.ggmlv1.q8_0.bin)

4:
Add model to Stablecode-alpha-3b folder

5: Run in Terminal
```bash
streamlit run main.py
```
