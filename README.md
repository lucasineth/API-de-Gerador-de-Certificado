# Certificados API

Esta API permite a gestão e emissão de certificados digitais para eventos, cursos ou treinamentos.
<img width="833" height="586" alt="Image" src="https://github.com/user-attachments/assets/410dfdba-221c-4a14-aa46-c41f7f6c97b0" />

## Funcionalidades

- Cadastro de participantes
- Geração de certificados em PDF

## Endpoints Principais

| Método | Rota                  | Descrição                       |
|--------|-----------------------|---------------------------------|
| GET    | `/api/certificados/`  | gerar certificado               |
| POST   | `/api/certificados/`  | certificado gerado e salvo      |

## Requisitos

- Python 3.12
- Banco de dados SQLite

## Instalação

```bash
git clone https://github.com/seu-usuario/certificados-api.git
cd certificados-api
```

## Uso

```bash
python manage.py runserver
```

## Licença

MIT
