from flask import Flask, jsonify, request, send_from_directory
import requests
import os
from datetime import datetime
import json

app = Flask(__name__, 
            static_folder='../static',
            template_folder='../templates')

SUPABASE_URL = "https://olrswumpeunhstuwnhbu.supabase.co"
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "sb_publishable_cmGGk2IXVEz4VB4dKkOnXA_XnX2siUU")

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

# ==================== FUNÇÃO PARA NORMALIZAR PUFFS ====================
def normalizar_puffs(valor):
    """Converte '30k' para 30000, '8k' para 8000, etc."""
    if not valor:
        return None
    if isinstance(valor, (int, float)):
        return int(valor)
    if isinstance(valor, str):
        valor = valor.lower().strip()
        if valor in ['vape', 'pod', 'recarregável', '']:
            return None
        if 'k' in valor:
            try:
                clean = valor.replace('k', '').replace(' ', '').replace(',', '.')
                return int(float(clean) * 1000)
            except:
                return None
        else:
            try:
                return int(valor)
            except:
                return None
    return None

# ==================== ROTAS ====================

@app.route('/')
@app.route('/admin')
def admin():
    return send_from_directory('../templates', 'admin.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('../static', path)

@app.route('/api/produtos', methods=['GET'])
def get_produtos():
    try:
        print("📦 Buscando produtos via Supabase API...")
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/produtos?select=*",
            headers=headers,
            timeout=15
        )
        
        if response.status_code == 200:
            produtos = response.json()
            produtos_normalizados = []
            for p in produtos:
                puffs_value = p.get('Puffs') or p.get('puffs') or p.get('PUFFS')
                
                sabores = p.get('sabores', [])
                if isinstance(sabores, str):
                    try:
                        sabores = json.loads(sabores)
                    except:
                        sabores = []
                
                item = {
                    'id': p.get('id'),
                    'nome': p.get('nome', ''),
                    'marca': p.get('marca', 'VAPORIZE'),
                    'preco': float(p.get('preco', 0)) if p.get('preco') else 0,
                    'puffs': normalizar_puffs(puffs_value),
                    'sabores': sabores,
                    'imagem': p.get('imagem', 'https://placehold.co/400x400/1a1a1a/00ffcc?text=VAPORIZE')
                }
                produtos_normalizados.append(item)
            
            print(f"✅ {len(produtos_normalizados)} produtos normalizados")
            return jsonify(produtos_normalizados)
        else:
            return jsonify({'error': f'HTTP {response.status_code}'}), 500
    except Exception as e:
        print(f"❌ Erro: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/produto/<int:id>/preco', methods=['PUT'])
def atualizar_preco_produto(id):
    """Atualiza o preço de um produto específico"""
    try:
        dados = request.json
        novo_preco = dados.get('preco')
        
        if novo_preco is None:
            return jsonify({'error': 'Preço não informado'}), 400
        if float(novo_preco) < 0:
            return jsonify({'error': 'Preço não pode ser negativo'}), 400
        
        # Verificar se produto existe
        check = requests.get(
            f"{SUPABASE_URL}/rest/v1/produtos?id=eq.{id}&select=id",
            headers=headers,
            timeout=10
        )
        if check.status_code != 200 or not check.json():
            return jsonify({'error': 'Produto não encontrado'}), 404
        
        # Atualizar preço
        response = requests.patch(
            f"{SUPABASE_URL}/rest/v1/produtos?id=eq.{id}",
            headers=headers,
            json={'preco': float(novo_preco)},
            timeout=10
        )
        
        if response.status_code in [200, 204]:
            return jsonify({'success': True, 'message': 'Preço atualizado com sucesso'})
        else:
            return jsonify({'error': f'Erro ao atualizar: {response.status_code}'}), 500
            
    except Exception as e:
        print(f"❌ Erro ao atualizar preço: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/pedidos', methods=['GET'])
def get_pedidos():
    try:
        print("📋 Buscando pedidos...")
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/pedidos?select=*&order=created_at.desc",
            headers=headers,
            timeout=15
        )
        
        if response.status_code == 200:
            pedidos = response.json()
            for p in pedidos:
                if 'total' in p:
                    p['total'] = float(p['total']) if p['total'] else 0
                if 'produtos' in p and p['produtos']:
                    try:
                        if isinstance(p['produtos'], str):
                            p['produtos'] = json.loads(p['produtos'])
                    except:
                        p['produtos'] = []
                else:
                    p['produtos'] = []
            return jsonify(pedidos)
        return jsonify([])
    except Exception as e:
        print(f"❌ Erro: {str(e)}")
        return jsonify([])

@app.route('/api/dashboard/stats', methods=['GET'])
def get_dashboard_stats():
    try:
        print("📊 Buscando estatísticas...")
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/pedidos?select=*",
            headers=headers,
            timeout=15
        )
        
        if response.status_code != 200:
            return jsonify({'error': 'Erro ao buscar pedidos'}), 500
            
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
                            if isinstance(qtd, (int, float)):
                                vendas_produtos[nome] = vendas_produtos.get(nome, 0) + qtd
                except:
                    pass
        
        top_produtos = sorted(vendas_produtos.items(), key=lambda x: x[1], reverse=True)[:5]
        top_produtos_formatado = [{'nome': nome, 'quantidade': qtd} for nome, qtd in top_produtos]
        
        # Vendas por dia (últimos 30 dias)
        from datetime import datetime, timedelta
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
        
        ultimos_pedidos = sorted(pedidos, key=lambda x: x.get('created_at', ''), reverse=True)[:10]
        
        return jsonify({
            'total_pedidos': total_pedidos,
            'total_faturamento': total_faturamento,
            'ticket_medio': ticket_medio,
            'status_count': status_count,
            'top_produtos': top_produtos_formatado,
            'vendas_dia': dict(sorted(vendas_dia.items())),
            'ultimos_pedidos': ultimos_pedidos
        })
        
    except Exception as e:
        print(f"❌ Erro: {str(e)}")
        return jsonify({'error': str(e)}), 500

# ==================== HANDLER PARA VERCEL ====================
def handler(event, context):
    return app(event, context)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
