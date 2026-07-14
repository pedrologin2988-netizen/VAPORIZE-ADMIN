from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests
import os
from datetime import datetime, timedelta
import json
import traceback

app = Flask(__name__, template_folder='templates')
CORS(app)

# ==================== NOVA CONFIGURAÇÃO SUPABASE ====================
SUPABASE_URL = "https://htnqtolrgpnruxhmtfsl.supabase.co"
SUPABASE_KEY = "sb_secret_PzH80X6g4FKnFmxsXW5fBQ_gfzFr-ZI"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

@app.route('/')
def admin():
    return render_template('admin.html')

@app.route('/api/produtos', methods=['GET'])
def get_produtos():
    try:
        response = requests.get(f"{SUPABASE_URL}/rest/v1/produtos?select=*", headers=headers, timeout=15)
        if response.status_code == 200:
            produtos = response.json()
            for p in produtos:
                p['preco'] = float(p['preco']) if p.get('preco') else 0
            return jsonify(produtos)
        return jsonify([])
    except Exception as e:
        return jsonify([])

@app.route('/api/produto/<int:id>/preco', methods=['PUT'])
def atualizar_preco(id):
    try:
        dados = request.json
        novo_preco = dados.get('preco')
        if novo_preco is None or float(novo_preco) < 0:
            return jsonify({'error': 'Preço inválido'}), 400
        
        response = requests.patch(
            f"{SUPABASE_URL}/rest/v1/produtos?id=eq.{id}",
            headers=headers,
            json={'preco': float(novo_preco)}
        )
        if response.status_code in [200, 204]:
            return jsonify({'success': True})
        return jsonify({'error': 'Erro ao atualizar'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/pedidos', methods=['GET'])
def get_pedidos():
    try:
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/pedidos?select=*&order=created_at.desc",
            headers=headers,
            timeout=15
        )
        if response.status_code == 200:
            pedidos = response.json()
            for p in pedidos:
                p['total'] = float(p['total']) if p.get('total') else 0
            return jsonify(pedidos)
        return jsonify([])
    except Exception as e:
        return jsonify([])

@app.route('/api/dashboard/stats', methods=['GET'])
def get_stats():
    try:
        response = requests.get(f"{SUPABASE_URL}/rest/v1/pedidos?select=*", headers=headers, timeout=15)
        if response.status_code != 200:
            return jsonify({'error': 'Erro'}), 500
            
        pedidos = response.json()
        if not pedidos:
            return jsonify({
                'total_pedidos': 0,
                'total_faturamento': 0,
                'ticket_medio': 0,
                'status_count': {},
                'top_produtos': [],
                'vendas_dia': {},
                'ultimos_pedidos': []
            })
        
        total_pedidos = len(pedidos)
        total_faturamento = sum(float(p.get('total', 0) or 0) for p in pedidos)
        ticket_medio = total_faturamento / total_pedidos if total_pedidos > 0 else 0
        
        status_count = {}
        for p in pedidos:
            status = p.get('status', 'pendente')
            status_count[status] = status_count.get(status, 0) + 1
        
        vendas_produtos = {}
        for p in pedidos:
            produtos = p.get('produtos')
            if produtos:
                try:
                    if isinstance(produtos, str):
                        produtos = json.loads(produtos)
                    if isinstance(produtos, list):
                        for item in produtos:
                            nome = item.get('nome', 'Produto')
                            qtd = item.get('quantidade', 1)
                            vendas_produtos[nome] = vendas_produtos.get(nome, 0) + qtd
                except:
                    pass
        
        top = sorted(vendas_produtos.items(), key=lambda x: x[1], reverse=True)[:5]
        top_produtos = [{'nome': n, 'quantidade': q} for n, q in top]
        
        vendas_dia = {}
        data_corte = datetime.now() - timedelta(days=30)
        for p in pedidos:
            created = p.get('created_at')
            if created:
                try:
                    if isinstance(created, str):
                        data = datetime.fromisoformat(created.replace('Z', '+00:00'))
                    else:
                        data = created
                    if isinstance(data, datetime) and data >= data_corte:
                        chave = data.strftime('%Y-%m-%d')
                        vendas_dia[chave] = vendas_dia.get(chave, 0) + 1
                except:
                    pass
        
        ultimos = sorted(pedidos, key=lambda x: x.get('created_at', ''), reverse=True)[:10]
        
        return jsonify({
            'total_pedidos': total_pedidos,
            'total_faturamento': total_faturamento,
            'ticket_medio': ticket_medio,
            'status_count': status_count,
            'top_produtos': top_produtos,
            'vendas_dia': dict(sorted(vendas_dia.items())),
            'ultimos_pedidos': ultimos
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)