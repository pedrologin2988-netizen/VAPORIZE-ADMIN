from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests
import os
from datetime import datetime, timedelta
import json
import traceback
import sys

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')
CORS(app)

# ============ CONFIGURAÇÕES SUPABASE ============
SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://olrswumpeunhstuwnhbu.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "sb_publishable_cmGGk2IXVEz4VB4dKkOnXA_XnX2siUU")

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

print(f"🚀 Iniciando VAPORIZE Admin...")
print(f"📌 Supabase URL: {SUPABASE_URL}")
print(f"📌 Supabase Key: {SUPABASE_KEY[:20]}...")

# ============ FUNÇÃO DE TESTE ============
def testar_conexao():
    """Testa a conexão com o Supabase com retorno detalhado"""
    try:
        print("🔌 Testando conexão com Supabase...")
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/pedidos?select=id&limit=1",
            headers=headers,
            timeout=10
        )
        print(f"📊 Status da resposta: {response.status_code}")
        print(f"📊 Conteúdo: {response.text[:200]}")
        
        if response.status_code == 200:
            print("✅ Conexão com Supabase estabelecida!")
            return True, "Conectado"
        else:
            print(f"❌ Erro na conexão: {response.status_code}")
            return False, f"HTTP {response.status_code}"
    except requests.exceptions.Timeout:
        print("❌ Timeout na conexão")
        return False, "Timeout"
    except requests.exceptions.ConnectionError:
        print("❌ Erro de conexão")
        return False, "Erro de conexão"
    except Exception as e:
        print(f"❌ Erro: {str(e)}")
        return False, str(e)

# ============ ROTAS ============

@app.route('/')
def admin():
    """Dashboard administrativo"""
    return render_template('admin.html')

@app.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint para verificar saúde do serviço"""
    try:
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/pedidos?select=id&limit=1",
            headers=headers,
            timeout=5
        )
        if response.status_code == 200:
            return jsonify({
                'status': 'ok', 
                'database': 'connected',
                'supabase_url': SUPABASE_URL,
                'records': 'ok'
            })
        return jsonify({
            'status': 'error', 
            'database': 'disconnected',
            'error': f'HTTP {response.status_code}',
            'details': response.text[:100]
        }), 500
    except Exception as e:
        return jsonify({
            'status': 'error', 
            'database': 'disconnected',
            'error': str(e)
        }), 500

@app.route('/api/produtos', methods=['GET'])
def get_produtos():
    """Busca todos os produtos do Supabase"""
    try:
        print("📦 Buscando produtos...")
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/produtos?select=*",
            headers=headers,
            timeout=15
        )
        
        print(f"📊 Status produtos: {response.status_code}")
        
        if response.status_code != 200:
            print(f"❌ Erro ao buscar produtos: {response.status_code}")
            print(f"📊 Resposta: {response.text[:200]}")
            return jsonify({'error': f'HTTP {response.status_code}', 'details': response.text[:100]}), 500
            
        produtos = response.json()
        print(f"✅ {len(produtos)} produtos encontrados")
        
        # Converter para formato compatível
        for p in produtos:
            if 'preco' in p:
                p['preco'] = float(p['preco']) if p['preco'] else 0
            if 'sabores' in p and p['sabores']:
                try:
                    if isinstance(p['sabores'], str):
                        p['sabores'] = json.loads(p['sabores'])
                except:
                    p['sabores'] = []
            if 'imagem' not in p or not p['imagem']:
                p['imagem'] = 'https://placehold.co/400x400/1a1a1a/e53935?text=VAPORIZE'
                    
        return jsonify(produtos)
    except Exception as e:
        print(f"❌ Erro ao buscar produtos: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'error': str(e), 'details': traceback.format_exc()}), 500

@app.route('/api/pedidos', methods=['GET'])
def get_pedidos():
    """Busca todos os pedidos do Supabase"""
    try:
        print("📋 Buscando pedidos...")
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/pedidos?select=*&order=created_at.desc",
            headers=headers,
            timeout=15
        )
        
        print(f"📊 Status pedidos: {response.status_code}")
        
        if response.status_code != 200:
            print(f"❌ Erro ao buscar pedidos: {response.status_code}")
            print(f"📊 Resposta: {response.text[:200]}")
            return jsonify([])
            
        pedidos = response.json()
        print(f"✅ {len(pedidos)} pedidos encontrados")
        
        for p in pedidos:
            if 'total' in p:
                p['total'] = float(p['total']) if p['total'] else 0
            if 'produtos' in p and p['produtos']:
                try:
                    if isinstance(p['produtos'], str):
                        p['produtos'] = json.loads(p['produtos'])
                    elif isinstance(p['produtos'], list):
                        pass
                    else:
                        p['produtos'] = []
                except:
                    p['produtos'] = []
            else:
                p['produtos'] = []
                    
        return jsonify(pedidos)
    except Exception as e:
        print(f"❌ Erro ao buscar pedidos: {str(e)}")
        print(traceback.format_exc())
        return jsonify([])

@app.route('/api/pedido/<int:id>', methods=['GET'])
def get_pedido(id):
    """Busca um pedido específico pelo ID"""
    try:
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/pedidos?id=eq.{id}&select=*",
            headers=headers,
            timeout=10
        )
        
        if response.status_code != 200:
            return jsonify({'error': 'Pedido não encontrado'}), 404
            
        pedidos = response.json()
        if not pedidos:
            return jsonify({'error': 'Pedido não encontrado'}), 404
            
        pedido = pedidos[0]
        if 'total' in pedido:
            pedido['total'] = float(pedido['total']) if pedido['total'] else 0
        if 'produtos' in pedido and pedido['produtos']:
            try:
                if isinstance(pedido['produtos'], str):
                    pedido['produtos'] = json.loads(pedido['produtos'])
            except:
                pedido['produtos'] = []
        else:
            pedido['produtos'] = []
            
        return jsonify(pedido)
    except Exception as e:
        print(f"❌ Erro ao buscar pedido: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/pedido/<int:id>', methods=['PUT'])
def atualizar_pedido(id):
    """Atualiza um pedido existente"""
    try:
        dados = request.json
        
        # Verificar se o pedido existe
        check = requests.get(
            f"{SUPABASE_URL}/rest/v1/pedidos?id=eq.{id}&select=id",
            headers=headers,
            timeout=10
        )
        if check.status_code != 200 or not check.json():
            return jsonify({'error': 'Pedido não encontrado'}), 404
        
        # Preparar dados para atualização
        update_data = {}
        if 'nome_cliente' in dados:
            update_data['nome_cliente'] = dados['nome_cliente']
        if 'telefone' in dados:
            update_data['telefone'] = dados['telefone']
        if 'endereco' in dados:
            update_data['endereco'] = dados['endereco']
        if 'total' in dados:
            update_data['total'] = dados['total']
        if 'status' in dados:
            update_data['status'] = dados['status']
        if 'produtos' in dados:
            update_data['produtos'] = dados['produtos']
        
        if not update_data:
            return jsonify({'error': 'Nenhum campo para atualizar'}), 400
        
        response = requests.patch(
            f"{SUPABASE_URL}/rest/v1/pedidos?id=eq.{id}",
            headers=headers,
            json=update_data,
            timeout=10
        )
        
        if response.status_code == 200 or response.status_code == 204:
            return jsonify({'success': True, 'message': 'Pedido atualizado com sucesso'})
        else:
            return jsonify({'error': f'Erro ao atualizar: {response.status_code}'}), 500
            
    except Exception as e:
        print(f"❌ Erro ao atualizar pedido: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/pedido/<int:id>', methods=['DELETE'])
def deletar_pedido(id):
    """Deleta um pedido pelo ID"""
    try:
        # Verificar se o pedido existe
        check = requests.get(
            f"{SUPABASE_URL}/rest/v1/pedidos?id=eq.{id}&select=id",
            headers=headers,
            timeout=10
        )
        if check.status_code != 200 or not check.json():
            return jsonify({'error': 'Pedido não encontrado'}), 404
        
        response = requests.delete(
            f"{SUPABASE_URL}/rest/v1/pedidos?id=eq.{id}",
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200 or response.status_code == 204:
            return jsonify({'success': True, 'message': 'Pedido deletado com sucesso'})
        else:
            return jsonify({'error': f'Erro ao deletar: {response.status_code}'}), 500
            
    except Exception as e:
        print(f"❌ Erro ao deletar pedido: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/pedido/<int:id>/status', methods=['PATCH'])
def atualizar_status_pedido(id):
    """Atualiza apenas o status de um pedido"""
    try:
        dados = request.json
        novo_status = dados.get('status')
        
        if not novo_status:
            return jsonify({'error': 'Status não informado'}), 400
            
        status_validos = ['pendente', 'sucesso', 'cancelado']
        if novo_status not in status_validos:
            return jsonify({'error': f'Status inválido. Use: {", ".join(status_validos)}'}), 400
        
        response = requests.patch(
            f"{SUPABASE_URL}/rest/v1/pedidos?id=eq.{id}",
            headers=headers,
            json={'status': novo_status},
            timeout=10
        )
        
        if response.status_code == 200 or response.status_code == 204:
            return jsonify({'success': True, 'message': f'Status atualizado para {novo_status}'})
        else:
            return jsonify({'error': f'Erro ao atualizar: {response.status_code}'}), 500
            
    except Exception as e:
        print(f"❌ Erro ao atualizar status: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/dashboard/stats', methods=['GET'])
def get_dashboard_stats():
    """Retorna estatísticas consolidadas do dashboard"""
    try:
        print("📊 Buscando estatísticas do dashboard...")
        
        # Buscar todos os pedidos
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/pedidos?select=*",
            headers=headers,
            timeout=15
        )
        
        print(f"📊 Status dashboard: {response.status_code}")
        
        if response.status_code != 200:
            print(f"❌ Erro ao buscar pedidos: {response.status_code}")
            print(f"📊 Resposta: {response.text[:200]}")
            return jsonify({
                'error': f'HTTP {response.status_code}',
                'details': response.text[:100]
            }), 500
            
        pedidos = response.json()
        print(f"✅ {len(pedidos)} pedidos encontrados para análise")
        
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
        
        # Estatísticas básicas
        total_pedidos = len(pedidos)
        total_faturamento = sum(float(p.get('total', 0) or 0) for p in pedidos)
        ticket_medio = total_faturamento / total_pedidos if total_pedidos > 0 else 0
        
        # Contagem por status
        status_count = {}
        for p in pedidos:
            status = p.get('status', 'pendente')
            status_count[status] = status_count.get(status, 0) + 1
        
        # Análise de produtos (campo 'produtos' é JSONB)
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
                except (json.JSONDecodeError, TypeError) as e:
                    print(f"Erro ao processar produtos: {e}")
                    pass
        
        # Top 5 produtos
        top_produtos = sorted(vendas_produtos.items(), key=lambda x: x[1], reverse=True)[:5]
        top_produtos_formatado = [{'nome': nome, 'quantidade': qtd} for nome, qtd in top_produtos]
        
        # Vendas por dia (últimos 30 dias)
        vendas_dia = {}
        data_corte = datetime.now() - timedelta(days=30)
        
        for p in pedidos:
            created = p.get('created_at')
            if created:
                try:
                    if isinstance(created, str):
                        # Tenta vários formatos de data
                        data = None
                        for fmt in ['%Y-%m-%dT%H:%M:%S.%f%z', '%Y-%m-%dT%H:%M:%S%z', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d']:
                            try:
                                data = datetime.strptime(created[:19], fmt if '%f' not in fmt else fmt)
                                break
                            except:
                                continue
                        if data is None:
                            data = datetime.fromisoformat(created.replace('Z', '+00:00'))
                    else:
                        data = created
                    
                    if isinstance(data, datetime) and data >= data_corte:
                        chave = data.strftime('%Y-%m-%d')
                        vendas_dia[chave] = vendas_dia.get(chave, 0) + 1
                except (ValueError, TypeError) as e:
                    print(f"Erro ao processar data: {e}")
                    pass
        
        # Ordenar vendas por dia
        vendas_dia_ordenado = dict(sorted(vendas_dia.items()))
        
        # Últimos 10 pedidos
        ultimos_pedidos = sorted(pedidos, key=lambda x: x.get('created_at', ''), reverse=True)[:10]
        
        # Converter para JSON serializável
        for p in ultimos_pedidos:
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
        
        return jsonify({
            'total_pedidos': total_pedidos,
            'total_faturamento': total_faturamento,
            'ticket_medio': ticket_medio,
            'status_count': status_count,
            'top_produtos': top_produtos_formatado,
            'vendas_dia': vendas_dia_ordenado,
            'ultimos_pedidos': ultimos_pedidos
        })
        
    except Exception as e:
        print(f"❌ Erro no dashboard: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'error': str(e), 'details': traceback.format_exc()}), 500

@app.route('/api/pedidos', methods=['POST'])
def criar_pedido():
    """Cria um novo pedido no Supabase"""
    try:
        dados = request.json
        
        pedido = {
            "nome_cliente": dados.get('nome'),
            "telefone": dados.get('telefone'),
            "endereco": dados.get('endereco'),
            "total": dados.get('total'),
            "status": "pendente",
            "produtos": json.dumps(dados.get('itens', [])),
            "created_at": datetime.now().isoformat()
        }
        
        response = requests.post(
            f"{SUPABASE_URL}/rest/v1/pedidos",
            headers=headers,
            json=pedido,
            timeout=10
        )
        
        if response.status_code == 201:
            return jsonify({'success': True, 'id': response.json().get('id')})
        else:
            return jsonify({'error': f'Erro ao criar pedido: {response.status_code}'}), 500
            
    except Exception as e:
        print(f"❌ Erro ao criar pedido: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/whatsapp', methods=['GET'])
def get_whatsapp():
    """Busca o número do WhatsApp configurado"""
    try:
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/numero?ativo=eq.true&select=whatsapp&limit=1",
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            if data:
                return jsonify({'success': True, 'whatsapp': data[0].get('whatsapp')})
        
        return jsonify({'success': False, 'whatsapp': '5581995248272'})
    except Exception as e:
        print(f"❌ Erro ao buscar WhatsApp: {str(e)}")
        return jsonify({'success': False, 'whatsapp': '5581995248272'})

if __name__ == '__main__':
    print("🔌 Testando conexão com Supabase...")
    conectado, msg = testar_conexao()
    if conectado:
        print("✅ Conexão com Supabase estabelecida!")
    else:
        print(f"❌ Falha na conexão: {msg}")
    
    app.run(debug=True, port=5001)