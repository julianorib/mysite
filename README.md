# Projeto python + flask 

Este projeto foi criado para funcionar em conjunto com uma Stack de Observabilidade.\
Estudos sobre métricas e traces.

- Métricas
- Traces
- *Logs 

*Em desenvolvimento.

## Como usar

```
docker compose up -d
```

<http://localhost:8080/>\
<http://localhost:8080/blue>\
<http://localhost:8080/green>\
<http://localhost:8080/metrics>\


## Ferramentas

- Prometheus: <http://localhost:9090>
- Grafana: <http://localhost:3000>
- Jaeger: <http://localhost:16686>

### Grafana: 
- admin : admin
- Necessário cadastrar o `datasource prometheus`: http://prometheus:9090
- Importar o Dashboard `flask_python_observability_dashboard`.
