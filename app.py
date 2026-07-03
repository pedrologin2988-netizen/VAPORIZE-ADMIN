from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import psycopg2
import psycopg2.extras
import os
from datetime import datetime, timedelta
import json
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')
CORS(app)

# ============ CONFIGURAÇÕES DO BANCO ============
DB_HOST = os.environ.get("DB_HOST", "db.olrswumpeunhstuwnhbu.supabase.co")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_NAME = os.environ.get("DB_NAME", "postgres")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "qcUDE8t8kxRsLDBu")

# ============ FUNÇÃO DE CONEXÃO ============
def get_db_connection():
    """Cria e retorna uma conexão com o banco de dados"""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            connect_timeout=10
        )
        return conn
    except Exception as e:
        print(f"❌ Erro ao conectar ao banco: {str(e)}")
        return None

# ============ ROTAS ============

@app.route('/')
def admin():
    """Dashboard administrativo"""
    return render_template('admin.html')

@app.route('/api/produtos', methods=['GET'])
def get_produtos():
    """Busca todos os produtos do banco"""
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Erro de conexão com o banco'}), 500
            
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("SELECT * FROM produtos ORDER BY id")
        produtos = cur.fetchall()
        cur.close()
        conn.close()
        
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
        return jsonify({'error': str(e)}), 500

@app.route('/api/pedidos', methods=['GET'])
def get_pedidos():
    """Busca todos os pedidos do banco"""
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify([])
            
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("""
            SELECT * FROM pedidos 
            ORDER BY created_at DESC
        """)
        pedidos = cur.fetchall()
        cur.close()
        conn.close()
        
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
        return jsonify([])

@app.route('/api/pedido/<int:id>', methods=['GET'])
def get_pedido(id):
    """Busca um pedido específico pelo ID"""
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Erro de conexão'}), 500
            
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("SELECT * FROM pedidos WHERE id = %s", (id,))
        pedido = cur.fetchone()
        cur.close()
        conn.close()
        
        if not pedido:
            return jsonify({'error': 'Pedido não encontrado'}), 404
            
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
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Erro de conexão'}), 500
            
        cur = conn.cursor()
        
        # Verificar se o pedido existe
        cur.execute("SELECT id FROM pedidos WHERE id = %s", (id,))
        if not cur.fetchone():
            cur.close()
            conn.close()
            return jsonify({'error': 'Pedido não encontrado'}), 404
        
        # Atualizar campos
        campos = []
        valores = []
        
        if 'nome_cliente' in dados:
            campos.append("nome_cliente = %s")
            valores.append(dados['nome_cliente'])
        if 'telefone' in dados:
            campos.append("telefone = %s")
            valores.append(dados['telefone'])
        if 'endereco' in dados:
            campos.append("endereco = %s")
            valores.append(dados['endereco'])
        if 'total' in dados:
            campos.append("total = %s")
            valores.append(dados['total'])
        if 'status' in dados:
            campos.append("status = %s")
            valores.append(dados['status'])
        if 'produtos' in dados:
            campos.append("produtos = %s")
            valores.append(json.dumps(dados['produtos']))
        
        if not campos:
            return jsonify({'error': 'Nenhum campo para atualizar'}), 400
        
        valores.append(id)
        query = f"UPDATE pedidos SET {', '.join(campos)} WHERE id = %s"
        
        cur.execute(query, valores)
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({'success': True, 'message': 'Pedido atualizado com sucesso'})
    except Exception as e:
        print(f"❌ Erro ao atualizar pedido: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/pedido/<int:id>', methods=['DELETE'])
def deletar_pedido(id):
    """Deleta um pedido pelo ID"""
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Erro de conexão'}), 500
            
        cur = conn.cursor()
        
        # Verificar se o pedido existe
        cur.execute("SELECT id FROM pedidos WHERE id = %s", (id,))
        if not cur.fetchone():
            cur.close()
            conn.close()
            return jsonify({'error': 'Pedido não encontrado'}), 404
        
        cur.execute("DELETE FROM pedidos WHERE id = %s", (id,))
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({'success': True, 'message': 'Pedido deletado com sucesso'})
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
        
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Erro de conexão'}), 500
            
        cur = conn.cursor()
        
        cur.execute("SELECT id FROM pedidos WHERE id = %s", (id,))
        if not cur.fetchone():
            cur.close()
            conn.close()
            return jsonify({'error': 'Pedido não encontrado'}), 404
        
        cur.execute("UPDATE pedidos SET status = %s WHERE id = %s", (novo_status, id))
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({'success': True, 'message': f'Status atualizado para {novo_status}'})
    except Exception as e:
        print(f"❌ Erro ao atualizar status: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/dashboard/stats', methods=['GET'])
def get_dashboard_stats():
    """Retorna estatísticas consolidadas do dashboard"""
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Erro de conexão'}), 500
            
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        
        # DADOS BÁSICOS
        cur.execute("""
            SELECT 
                COUNT(*) as total_pedidos,
                COALESCE(SUM(total), 0) as total_faturamento,
                COALESCE(AVG(total), 0) as ticket_medio
            FROM pedidos
        """)
        stats = cur.fetchone()
        
        # STATUS COUNT
        cur.execute("""
            SELECT status, COUNT(*) as count 
            FROM pedidos 
            GROUP BY status
        """)
        status_count = cur.fetchall()
        status_dict = {row['status']: row['count'] for row in status_count}
        
        # TOP PRODUTOS
        cur.execute("""
            SELECT id, produtos FROM pedidos 
            WHERE produtos IS NOT NULL 
            AND produtos != '[]'::jsonb
            AND produtos != 'null'::jsonb
        """)
        pedidos_com_produtos = cur.fetchall()
        
        vendas_produtos = {}
        for pedido in pedidos_com_produtos:
            produtos_data = pedido['produtos']
            if produtos_data:
                try:
                    if isinstance(produtos_data, str):
                        produtos_list = json.loads(produtos_data)
                    elif isinstance(produtos_data, list):
                        produtos_list = produtos_data
                    else:
                        continue
                    
                    if isinstance(produtos_list, list):
                        for item in produtos_list:
                            if isinstance(item, dict):
                                nome = item.get('nome', 'Produto')
                                qtd = item.get('quantidade', 1)
                                if isinstance(qtd, (int, float)):
                                    vendas_produtos[nome] = vendas_produtos.get(nome, 0) + qtd
                except Exception:
                    continue
        
        top_produtos = sorted(vendas_produtos.items(), key=lambda x: x[1], reverse=True)[:5]
        top_produtos_formatado = [{'nome': nome, 'quantidade': qtd} for nome, qtd in top_produtos]
        
        # VENDAS POR DIA
        cur.execute("""
            SELECT 
                DATE(created_at) as data,
                COUNT(*) as total
            FROM pedidos
            WHERE created_at >= NOW() - INTERVAL '30 days'
            GROUP BY DATE(created_at)
            ORDER BY data ASC
        """)
        vendas_dia = cur.fetchall()
        vendas_dia_dict = {}
        for row in vendas_dia:
            if row['data']:
                vendas_dia_dict[row['data'].strftime('%Y-%m-%d')] = row['total']
        
        # ÚLTIMOS 10 PEDIDOS
        cur.execute("""
            SELECT * FROM pedidos 
            ORDER BY created_at DESC 
            LIMIT 10
        """)
        ultimos_pedidos = cur.fetchall()
        
        cur.close()
        conn.close()
        
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
            'total_pedidos': stats['total_pedidos'] if stats else 0,
            'total_faturamento': float(stats['total_faturamento']) if stats else 0,
            'ticket_medio': float(stats['ticket_medio']) if stats else 0,
            'status_count': status_dict,
            'top_produtos': top_produtos_formatado,
            'vendas_dia': vendas_dia_dict,
            'ultimos_pedidos': ultimos_pedidos
        })
        
    except Exception as e:
        print(f"❌ Erro no dashboard: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/api/whatsapp', methods=['GET'])
def get_whatsapp():
    """Busca o número do WhatsApp configurado"""
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({'success': False, 'whatsapp': '5581995248272'})
            
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("""
            SELECT whatsapp FROM numero 
            WHERE ativo = true 
            LIMIT 1
        """)
        resultado = cur.fetchone()
        cur.close()
        conn.close()
        
        if resultado:
            return jsonify({'success': True, 'whatsapp': resultado['whatsapp']})
        return jsonify({'success': False, 'whatsapp': '5581995248272'})
    except Exception as e:
        print(f"❌ Erro ao buscar WhatsApp: {str(e)}")
        return jsonify({'success': False, 'whatsapp': '5581995248272'})

@app.route('/api/pedidos', methods=['POST'])
def criar_pedido():
    """Cria um novo pedido no banco"""
    try:
        dados = request.json
        
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Erro de conexão'}), 500
            
        cur = conn.cursor()
        
        produtos_json = json.dumps(dados.get('itens', []))
        
        cur.execute("""
            INSERT INTO pedidos (nome_cliente, telefone, endereco, total, status, produtos, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, NOW())
            RETURNING id
        """, (
            dados.get('nome'),
            dados.get('telefone'),
            dados.get('endereco'),
            dados.get('total'),
            'pendente',
            produtos_json
        ))
        
        pedido_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({'success': True, 'id': pedido_id})
    except Exception as e:
        print(f"❌ Erro ao criar pedido: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("🔌 Testando conexão com o banco...")
    conn = get_db_connection()
    if conn:
        print("✅ Conexão com banco estabelecida!")
        conn.close()
    else:
        print("❌ Falha na conexão com o banco!")
    
    app.run(debug=True, port=5001)