# Quiron_Quant_AULA_GIT

Repositório de treino da oficina de Git do QUIRON. Aqui pode errar à vontade: ele existe para isso.

## O que tem aqui

```
Quiron_Quant_AULA_GIT/
├── src/indicadores.py     # calcula a média móvel de uma série de preços
├── dados/precos.csv       # preços fictícios, só para o exemplo
├── participantes/         # cada participante adiciona um arquivo aqui (exercício)
├── requirements.txt       # bibliotecas Python do projeto
├── .env.example           # modelo para o arquivo de segredos (.env)
└── .gitignore             # o que o Git não deve acompanhar
```

## Como rodar

```bash
git clone https://github.com/bernardorubio/Quiron_Quant_AULA_GIT.git
cd Quiron_Quant_AULA_GIT

python -m venv .venv
source .venv/bin/activate        # macOS e Linux
source .venv/Scripts/activate    # Windows (Git Bash)

pip install -r requirements.txt
python src/indicadores.py
```

No macOS e no Linux, o comando pode ser `python3` em vez de `python`.

## Exercício

1. Atualize a `main`: `git switch main` e `git pull`
2. Crie sua branch: `git switch -c participante/seu-nome`
3. Copie `participantes/_modelo.md` para `participantes/seu-nome.md` e preencha
4. Faça o commit e publique: `git push -u origin participante/seu-nome`
5. Abra um Pull Request no GitHub e peça revisão

## Combinados

- Nunca commitar direto na `main` nos projetos de verdade: sempre branch e Pull Request
- `git pull` antes de começar a trabalhar
- Commits pequenos, com mensagens que dizem o que mudou
- Chaves e senhas ficam no `.env`, que está no `.gitignore`
- Nada de arquivos grandes: o GitHub recusa arquivos acima de 100 MB
