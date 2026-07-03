<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>VAPORIZE - Admin Dashboard</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Rajdhani:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        :root {
            --bg: #050505;
            --fg: #f5f5f5;
            --card: #0d0d0d;
            --border: #1a1a1a;
            --primary: #e53935;
            --primary-dark: #c62828;
            --success: #4caf50;
            --warning: #ffc107;
            --danger: #f44336;
            --muted: #888;
            --radius: 12px;
        }
        
        body {
            background: var(--bg);
            color: var(--fg);
            font-family: 'Rajdhani', sans-serif;
            padding: 20px;
            min-height: 100vh;
        }
        
        .container {
            max-width: 1440px;
            margin: 0 auto;
        }
        
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: var(--bg); }
        ::-webkit-scrollbar-thumb { background: var(--primary); border-radius: 4px; }
        
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
            border-bottom: 1px solid var(--border);
            margin-bottom: 30px;
            flex-wrap: wrap;
            gap: 15px;
        }
        
        .header h1 {
            font-family: 'Bebas Neue', sans-serif;
            font-size: 2.5rem;
            color: var(--primary);
            text-shadow: 0 0 20px rgba(229, 57, 53, 0.3);
        }
        
        .header h1 span { color: var(--fg); }
        
        .header-actions {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            align-items: center;
        }
        
        .header-actions select,
        .header-actions input {
            background: var(--card);
            border: 1px solid var(--border);
            color: var(--fg);
            padding: 10px 16px;
            border-radius: var(--radius);
            font-family: 'Rajdhani', sans-serif;
            font-size: 0.9rem;
            min-width: 140px;
        }
        
        .header-actions select:focus,
        .header-actions input:focus {
            outline: none;
            border-color: var(--primary);
        }
        
        .btn {
            padding: 10px 24px;
            border: none;
            border-radius: var(--radius);
            cursor: pointer;
            font-family: 'Bebas Neue', sans-serif;
            font-size: 1rem;
            letter-spacing: 0.05em;
            transition: all 0.3s;
            color: #fff;
        }
        
        .btn-primary { background: var(--primary); }
        .btn-primary:hover { transform: scale(1.05); box-shadow: 0 0 30px rgba(229, 57, 53, 0.3); }
        
        .btn-success { background: var(--success); }
        .btn-success:hover { transform: scale(1.05); box-shadow: 0 0 30px rgba(76, 175, 80, 0.3); }
        
        .btn-danger { background: var(--danger); }
        .btn-danger:hover { transform: scale(1.05); box-shadow: 0 0 30px rgba(244, 67, 54, 0.3); }
        
        .btn-warning { background: var(--warning); color: #000; }
        .btn-warning:hover { transform: scale(1.05); box-shadow: 0 0 30px rgba(255, 193, 7, 0.3); }
        
        .btn-sm { padding: 6px 14px; font-size: 0.8rem; }
        .btn-xs { padding: 4px 10px; font-size: 0.7rem; }
        
        .btn-outline {
            background: transparent;
            border: 2px solid var(--primary);
            color: var(--primary);
        }
        .btn-outline:hover { background: rgba(229, 57, 53, 0.1); }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .stat-card {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 20px 24px;
            transition: all 0.3s;
        }
        
        .stat-card:hover {
            border-color: var(--primary);
            box-shadow: 0 0 20px rgba(229, 57, 53, 0.1);
        }
        
        .stat-card .label {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.15em;
            color: var(--muted);
        }
        
        .stat-card .value {
            font-family: 'Bebas Neue', sans-serif;
            font-size: 2rem;
            margin-top: 4px;
            color: var(--primary);
        }
        
        .stat-card .sub {
            font-size: 0.8rem;
            color: var(--muted);
            margin-top: 4px;
        }
        
        .charts-grid {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .chart-card {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 20px;
        }
        
        .chart-card h3 {
            font-family: 'Bebas Neue', sans-serif;
            font-size: 1.3rem;
            margin-bottom: 15px;
            color: var(--muted);
            letter-spacing: 0.05em;
        }
        
        .chart-card canvas {
            width: 100% !important;
            height: auto !important;
            max-height: 280px;
        }
        
        .table-card {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 20px;
            overflow-x: auto;
            margin-bottom: 20px;
        }
        
        .table-card h3 {
            font-family: 'Bebas Neue', sans-serif;
            font-size: 1.3rem;
            margin-bottom: 15px;
            color: var(--muted);
            letter-spacing: 0.05em;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.9rem;
        }
        
        thead {
            border-bottom: 1px solid var(--border);
        }
        
        th {
            text-align: left;
            padding: 12px 16px;
            color: var(--muted);
            text-transform: uppercase;
            font-size: 0.7rem;
            letter-spacing: 0.1em;
        }
        
        td {
            padding: 12px 16px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        tr:hover td {
            background: rgba(229, 57, 53, 0.05);
        }
        
        .status-badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.7rem;
            font-weight: 600;
            text-transform: uppercase;
        }
        
        .status-badge.success { background: rgba(76, 175, 80, 0.2); color: var(--success); }
        .status-badge.pending { background: rgba(255, 193, 7, 0.2); color: var(--warning); }
        .status-badge.canceled { background: rgba(244, 67, 54, 0.2); color: var(--danger); }
        .status-badge.unknown { background: rgba(136, 136, 136, 0.2); color: var(--muted); }
        
        .actions-cell {
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
        }
        
        .loading-overlay {
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.85);
            z-index: 999;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        
        .loading-overlay.active { display: flex; }
        
        .spinner {
            width: 50px;
            height: 50px;
            border: 3px solid var(--border);
            border-top-color: var(--primary);
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        
        .loading-overlay p {
            margin-top: 16px;
            color: var(--muted);
        }
        
        .empty-state {
            text-align: center;
            padding: 40px;
            color: var(--muted);
        }
        
        .empty-state i {
            font-size: 3rem;
            opacity: 0.3;
            margin-bottom: 1rem;
        }
        
        /* MODAL */
        .modal-overlay {
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.9);
            z-index: 1000;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .modal-overlay.active { display: flex; }
        
        .modal {
            background: var(--card);
            border: 2px solid var(--primary);
            border-radius: var(--radius);
            padding: 2rem;
            max-width: 600px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
        }
        
        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
        }
        
        .modal-header h3 {
            font-family: 'Bebas Neue', sans-serif;
            font-size: 1.5rem;
            color: var(--primary);
        }
        
        .modal-close {
            background: none;
            border: none;
            color: #fff;
            font-size: 2rem;
            cursor: pointer;
            transition: 0.3s;
        }
        
        .modal-close:hover { color: var(--primary); transform: rotate(90deg); }
        
        .modal label {
            display: block;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: var(--muted);
            margin-bottom: 4px;
        }
        
        .modal input, .modal textarea, .modal select {
            width: 100%;
            padding: 0.75rem;
            margin-bottom: 1rem;
            background: #111;
            border: 1px solid var(--border);
            border-radius: var(--radius);
            color: #fff;
            font-family: 'Rajdhani', sans-serif;
            font-size: 1rem;
        }
        
        .modal input:focus, .modal textarea:focus, .modal select:focus {
            outline: none;
            border-color: var(--primary);
        }
        
        .modal .btn { width: 100%; margin-top: 0.5rem; }
        
        .text-truncate {
            max-width: 150px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
            display: inline-block;
        }
        
        @media (max-width: 1024px) {
            .charts-grid { grid-template-columns: 1fr; }
        }
        
        @media (max-width: 768px) {
            .header { flex-direction: column; align-items: flex-start; }
            .header-actions { width: 100%; }
            .header-actions select, .header-actions input { flex: 1; min-width: 100px; }
            .stats-grid { grid-template-columns: repeat(2, 1fr); }
            .stat-card .value { font-size: 1.5rem; }
            .header h1 { font-size: 1.8rem; }
            .modal { padding: 1.5rem; }
        }
        
        @media (max-width: 480px) {
            .stats-grid { grid-template-columns: 1fr; }
            .header-actions { flex-direction: column; }
            .header-actions select, .header-actions input, .header-actions button { width: 100%; }
            .actions-cell { flex-direction: column; }
            .actions-cell .btn { width: 100%; justify-content: center; }
        }
    </style>
</head>
<body>

    <div class="container">
        <!-- HEADER -->
        <header class="header">
            <h1>VAPORIZE <span>📊 Admin</span></h1>
            <div class="header-actions">
                <select id="filterPeriod">
                    <option value="7">Últimos 7 dias</option>
                    <option value="30" selected>Últimos 30 dias</option>
                    <option value="90">Últimos 90 dias</option>
                    <option value="365">Último ano</option>
                    <option value="0">Todos</option>
                </select>
                <select id="filterStatus">
                    <option value="">Todos os status</option>
                    <option value="sucesso">✅ Sucesso</option>
                    <option value="pendente">⏳ Pendente</option>
                    <option value="cancelado">❌ Cancelado</option>
                </select>
                <button class="btn btn-primary" onclick="carregarDados()">
                    <i class="fas fa-sync-alt"></i> Atualizar
                </button>
                <button class="btn btn-success" onclick="exportarCSV()">
                    <i class="fas fa-file-export"></i> CSV
                </button>
            </div>
        </header>

        <!-- STATS -->
        <section class="stats-grid" id="statsGrid">
            <div class="stat-card">
                <div class="label">📦 Total de Pedidos</div>
                <div class="value" id="totalPedidos">-</div>
                <div class="sub" id="pedidosSub">Carregando...</div>
            </div>
            <div class="stat-card">
                <div class="label">💰 Faturamento Total</div>
                <div class="value" id="faturamentoTotal">R$ -</div>
                <div class="sub" id="faturamentoSub">Carregando...</div>
            </div>
            <div class="stat-card">
                <div class="label">📊 Ticket Médio</div>
                <div class="value" id="ticketMedio">R$ -</div>
                <div class="sub">Por pedido</div>
            </div>
            <div class="stat-card">
                <div class="label">🔥 Produto Top</div>
                <div class="value" id="produtoTop" style="font-size:1.2rem;">-</div>
                <div class="sub" id="topVendas">0 unidades</div>
            </div>
            <div class="stat-card">
                <div class="label">👥 Status</div>
                <div class="value" id="statusCount" style="font-size:1.2rem;">-</div>
                <div class="sub">Sucesso / Pendente / Cancelado</div>
            </div>
        </section>

        <!-- CHARTS -->
        <section class="charts-grid">
            <div class="chart-card">
                <h3>📈 Vendas por Dia (últimos 30 dias)</h3>
                <canvas id="vendasChart"></canvas>
            </div>
            <div class="chart-card">
                <h3>🍃 Top 5 Produtos</h3>
                <canvas id="produtosChart"></canvas>
            </div>
        </section>

        <!-- ÚLTIMOS PEDIDOS -->
        <section class="table-card">
            <h3>📋 Últimos Pedidos</h3>
            <div id="recentOrders">
                <div class="empty-state">
                    <i class="fas fa-spinner fa-spin"></i>
                    <p>Carregando pedidos...</p>
                </div>
            </div>
        </section>

        <!-- TODOS OS PRODUTOS -->
        <section class="table-card">
            <h3>📦 Análise de Produtos</h3>
            <div id="productsTable">
                <div class="empty-state">
                    <i class="fas fa-spinner fa-spin"></i>
                    <p>Carregando produtos...</p>
                </div>
            </div>
        </section>
    </div>

    <!-- MODAL EDITAR -->
    <div class="modal-overlay" id="editModal">
        <div class="modal">
            <div class="modal-header">
                <h3><i class="fas fa-edit"></i> Editar Pedido</h3>
                <button class="modal-close" onclick="fecharModal('editModal')">&times;</button>
            </div>
            <form id="editForm">
                <input type="hidden" id="editId">
                <label>Cliente</label>
                <input type="text" id="editCliente" required>
                <label>Telefone</label>
                <input type="text" id="editTelefone" required>
                <label>Endereço</label>
                <textarea id="editEndereco" rows="2"></textarea>
                <label>Total</label>
                <input type="number" id="editTotal" step="0.01" required>
                <label>Status</label>
                <select id="editStatus">
                    <option value="pendente">⏳ Pendente</option>
                    <option value="sucesso">✅ Sucesso</option>
                    <option value="cancelado">❌ Cancelado</option>
                </select>
                <button type="submit" class="btn btn-primary">
                    <i class="fas fa-save"></i> Salvar Alterações
                </button>
            </form>
        </div>
    </div>

    <!-- MODAL CONFIRMAR DELETAR -->
    <div class="modal-overlay" id="deleteModal">
        <div class="modal" style="max-width:400px;">
            <div class="modal-header">
                <h3 style="color:var(--danger);"><i class="fas fa-trash"></i> Confirmar Exclusão</h3>
                <button class="modal-close" onclick="fecharModal('deleteModal')">&times;</button>
            </div>
            <p style="color:var(--muted);margin-bottom:1.5rem;font-size:1.1rem;">
                Tem certeza que deseja <strong style="color:var(--danger);">excluir</strong> o pedido <strong id="deleteIdDisplay">#</strong>?
            </p>
            <p style="color:var(--muted);margin-bottom:1.5rem;font-size:0.9rem;">
                Esta ação não pode ser desfeita!
            </p>
            <div style="display:flex;gap:1rem;">
                <button class="btn btn-danger" id="confirmDeleteBtn" style="flex:1;">
                    <i class="fas fa-trash"></i> Sim, Excluir
                </button>
                <button class="btn btn-outline" onclick="fecharModal('deleteModal')" style="flex:1;">
                    Cancelar
                </button>
            </div>
        </div>
    </div>

    <!-- LOADING -->
    <div class="loading-overlay" id="loadingOverlay">
        <div class="spinner"></div>
        <p>⏳ Carregando dados...</p>
    </div>

    <script>
        // ============================================================
        //  VARIÁVEIS GLOBAIS
        // ============================================================
        let todosPedidos = [];
        let todosProdutos = [];
        let vendasChart = null;
        let produtosChart = null;
        let dadosCompletos = null;

        // ============================================================
        //  CARREGAR DADOS
        // ============================================================
        async function carregarDados() {
            showLoading(true);
            try {
                const [statsRes, produtosRes] = await Promise.all([
                    fetch('/api/dashboard/stats'),
                    fetch('/api/produtos')
                ]);
                
                dadosCompletos = await statsRes.json();
                todosProdutos = await produtosRes.json();
                
                if (!dadosCompletos || dadosCompletos.error) {
                    throw new Error(dadosCompletos?.error || 'Erro ao carregar dados');
                }
                
                if (!Array.isArray(todosProdutos)) todosProdutos = [];
                
                // Buscar todos os pedidos para o modal de edição
                const pedidosRes = await fetch('/api/pedidos');
                todosPedidos = await pedidosRes.json();
                
                atualizarDashboard();
            } catch (error) {
                console.error('Erro:', error);
                alert('❌ Erro ao carregar dados: ' + error.message);
            }
            showLoading(false);
        }

        // ============================================================
        //  ATUALIZAR DASHBOARD
        // ============================================================
        function atualizarDashboard() {
            const stats = dadosCompletos;
            if (!stats) return;
            
            const total = stats.total_pedidos || 0;
            const faturamento = stats.total_faturamento || 0;
            const ticket = stats.ticket_medio || 0;
            
            const statusCount = stats.status_count || {};
            const statusText = Object.entries(statusCount)
                .map(([k, v]) => {
                    const emoji = k === 'sucesso' ? '✅' : k === 'pendente' ? '⏳' : '❌';
                    return `${emoji} ${k}: ${v}`;
                })
                .join(' / ') || 'Nenhum pedido';
            
            const topProdutos = stats.top_produtos || [];
            const topProduto = topProdutos.length > 0 ? topProdutos[0] : { nome: '-', quantidade: 0 };
            
            document.getElementById('totalPedidos').textContent = total;
            document.getElementById('faturamentoTotal').textContent = `R$ ${faturamento.toFixed(2)}`;
            document.getElementById('ticketMedio').textContent = `R$ ${ticket.toFixed(2)}`;
            document.getElementById('produtoTop').textContent = topProduto.nome || '-';
            document.getElementById('topVendas').textContent = `${topProduto.quantidade || 0} unidades`;
            document.getElementById('statusCount').textContent = statusText;
            
            const vendasDia = stats.vendas_dia || {};
            const topProdutosList = stats.top_produtos || [];
            atualizarGraficos(vendasDia, topProdutosList);
            
            const ultimosPedidos = stats.ultimos_pedidos || [];
            atualizarPedidosRecentes(ultimosPedidos);
            atualizarTabelaProdutos(todosProdutos);
        }

        // ============================================================
        //  GRÁFICOS
        // ============================================================
        function atualizarGraficos(vendasDia, topProdutos) {
            const ctx1 = document.getElementById('vendasChart').getContext('2d');
            const labels = Object.keys(vendasDia).sort();
            const values = labels.map(l => vendasDia[l]);
            
            if (vendasChart) vendasChart.destroy();
            vendasChart = new Chart(ctx1, {
                type: 'bar',
                data: {
                    labels: labels.length > 0 ? labels : ['Sem dados'],
                    datasets: [{
                        label: 'Pedidos',
                        data: labels.length > 0 ? values : [0],
                        backgroundColor: 'rgba(229, 57, 53, 0.7)',
                        borderColor: '#e53935',
                        borderWidth: 2,
                        borderRadius: 4,
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: true,
                    plugins: { legend: { labels: { color: '#888' } } },
                    scales: {
                        x: { ticks: { color: '#888', maxRotation: 45, font: { size: 10 } } },
                        y: { ticks: { color: '#888', stepSize: 1 } }
                    }
                }
            });
            
            const ctx2 = document.getElementById('produtosChart').getContext('2d');
            const labels2 = topProdutos.map(p => p.nome.length > 15 ? p.nome.slice(0, 15) + '...' : p.nome);
            const values2 = topProdutos.map(p => p.quantidade);
            const cores = ['#e53935', '#ff6f00', '#ffb300', '#ff7043', '#8d6e63'];
            
            if (produtosChart) produtosChart.destroy();
            produtosChart = new Chart(ctx2, {
                type: 'doughnut',
                data: {
                    labels: labels2.length > 0 ? labels2 : ['Sem dados'],
                    datasets: [{
                        data: labels2.length > 0 ? values2 : [1],
                        backgroundColor: cores.slice(0, Math.max(labels2.length, 1)),
                        borderColor: '#0d0d0d',
                        borderWidth: 2,
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: true,
                    plugins: {
                        legend: {
                            position: 'bottom',
                            labels: { color: '#888', padding: 10, font: { size: 11 } }
                        }
                    }
                }
            });
        }

        // ============================================================
        //  TABELA - PEDIDOS RECENTES (com botões Editar/Apagar)
        // ============================================================
        function atualizarPedidosRecentes(pedidos) {
            const container = document.getElementById('recentOrders');
            
            if (!pedidos || pedidos.length === 0) {
                container.innerHTML = `
                    <div class="empty-state">
                        <i class="fas fa-inbox"></i>
                        <p>Nenhum pedido encontrado</p>
                    </div>
                `;
                return;
            }
            
            let html = `
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Cliente</th>
                            <th>Telefone</th>
                            <th>Produtos</th>
                            <th>Total</th>
                            <th>Status</th>
                            <th>Data</th>
                            <th>Ações</th>
                        </tr>
                    </thead>
                    <tbody>
            `;
            
            pedidos.forEach(p => {
                const statusClass = p.status === 'sucesso' ? 'success' : 
                                   p.status === 'cancelado' ? 'canceled' : 
                                   p.status === 'pendente' ? 'pending' : 'unknown';
                const statusLabel = p.status || 'pendente';
                
                let produtosTexto = '-';
                if (p.produtos) {
                    try {
                        const parsed = typeof p.produtos === 'string' ? JSON.parse(p.produtos) : p.produtos;
                        if (Array.isArray(parsed) && parsed.length > 0) {
                            produtosTexto = parsed.map(item => item.nome || 'Produto').join(', ');
                        } else if (typeof parsed === 'object' && parsed.nome) {
                            produtosTexto = parsed.nome;
                        }
                    } catch (e) {}
                }
                
                const total = parseFloat(p.total) || 0;
                
                let data = '-';
                if (p.created_at) {
                    try {
                        const d = new Date(p.created_at);
                        data = d.toLocaleDateString('pt-BR') + ' ' + d.toLocaleTimeString('pt-BR', {hour: '2-digit', minute:'2-digit'});
                    } catch (e) {}
                }
                
                const cliente = p.nome_cliente || 'Anônimo';
                const telefone = p.telefone || '-';
                
                html += `
                    <tr>
                        <td>#${p.id}</td>
                        <td>${cliente}</td>
                        <td>${telefone}</td>
                        <td><span class="text-truncate" title="${produtosTexto}">${produtosTexto}</span></td>
                        <td>R$ ${total.toFixed(2)}</td>
                        <td><span class="status-badge ${statusClass}">${statusLabel}</span></td>
                        <td>${data}</td>
                        <td>
                            <div class="actions-cell">
                                <button class="btn btn-warning btn-xs" onclick="abrirEditar(${p.id})">
                                    <i class="fas fa-edit"></i>
                                </button>
                                <button class="btn btn-danger btn-xs" onclick="abrirDeletar(${p.id})">
                                    <i class="fas fa-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                `;
            });
            
            html += `</tbody></table>`;
            container.innerHTML = html;
        }

        // ============================================================
        //  TABELA - PRODUTOS
        // ============================================================
        function atualizarTabelaProdutos(produtos) {
            const container = document.getElementById('productsTable');
            
            if (!produtos || produtos.length === 0) {
                container.innerHTML = `
                    <div class="empty-state">
                        <i class="fas fa-box-open"></i>
                        <p>Nenhum produto cadastrado</p>
                    </div>
                `;
                return;
            }
            
            // Calcular vendas por produto
            const vendasProduto = {};
            if (todosPedidos && todosPedidos.length > 0) {
                todosPedidos.forEach(p => {
                    if (p.produtos) {
                        try {
                            const parsed = typeof p.produtos === 'string' ? JSON.parse(p.produtos) : p.produtos;
                            if (Array.isArray(parsed)) {
                                parsed.forEach(item => {
                                    const nome = item.nome || 'Produto';
                                    const qtd = item.quantidade || 1;
                                    vendasProduto[nome] = (vendasProduto[nome] || 0) + qtd;
                                });
                            }
                        } catch (e) {}
                    }
                });
            }
            
            let html = `
                <table>
                    <thead>
                        <tr>
                            <th>Produto</th>
                            <th>Marca</th>
                            <th>Preço</th>
                            <th>Vendas</th>
                            <th>Faturamento</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
            `;
            
            produtos.forEach(prod => {
                const vendas = vendasProduto[prod.nome] || 0;
                const faturamento = vendas * (parseFloat(prod.preco) || 0);
                const statusClass = vendas > 0 ? 'success' : 'pending';
                const statusLabel = vendas > 0 ? '✅ Ativo' : '⏳ Sem vendas';
                
                const imagem = prod.imagem || 'https://placehold.co/40x40/1a1a1a/e53935?text=V';
                
                html += `
                    <tr>
                        <td>
                            <div style="display:flex;align-items:center;gap:10px;">
                                <img src="${imagem}" 
                                     alt="${prod.nome}"
                                     style="width:40px;height:40px;object-fit:cover;border-radius:8px;border:1px solid var(--border);"
                                     onerror="this.src='https://placehold.co/40x40/1a1a1a/e53935?text=V'">
                                ${prod.nome}
                            </div>
                        </td>
                        <td>${prod.marca || 'VAPORIZE'}</td>
                        <td>R$ ${parseFloat(prod.preco).toFixed(2)}</td>
                        <td>${vendas}</td>
                        <td>R$ ${faturamento.toFixed(2)}</td>
                        <td><span class="status-badge ${statusClass}">${statusLabel}</span></td>
                    </tr>
                `;
            });
            
            html += `</tbody></table>`;
            container.innerHTML = html;
        }

        // ============================================================
        //  EDITAR PEDIDO
        // ============================================================
        function abrirEditar(id) {
            const pedido = todosPedidos.find(p => p.id === id);
            if (!pedido) {
                alert('Pedido não encontrado');
                return;
            }
            
            document.getElementById('editId').value = id;
            document.getElementById('editCliente').value = pedido.nome_cliente || '';
            document.getElementById('editTelefone').value = pedido.telefone || '';
            document.getElementById('editEndereco').value = pedido.endereco || '';
            document.getElementById('editTotal').value = pedido.total || 0;
            document.getElementById('editStatus').value = pedido.status || 'pendente';
            
            document.getElementById('editModal').classList.add('active');
        }

        document.getElementById('editForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const id = document.getElementById('editId').value;
            const dados = {
                nome_cliente: document.getElementById('editCliente').value,
                telefone: document.getElementById('editTelefone').value,
                endereco: document.getElementById('editEndereco').value,
                total: parseFloat(document.getElementById('editTotal').value),
                status: document.getElementById('editStatus').value
            };
            
            try {
                showLoading(true);
                const response = await fetch(`/api/pedido/${id}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(dados)
                });
                
                const result = await response.json();
                
                if (result.success) {
                    alert('✅ Pedido atualizado com sucesso!');
                    fecharModal('editModal');
                    carregarDados();
                } else {
                    alert('❌ Erro: ' + (result.error || 'Erro ao atualizar'));
                }
            } catch (error) {
                alert('❌ Erro: ' + error.message);
            }
            showLoading(false);
        });

        // ============================================================
        //  DELETAR PEDIDO
        // ============================================================
        let deletarId = null;

        function abrirDeletar(id) {
            deletarId = id;
            document.getElementById('deleteIdDisplay').textContent = `#${id}`;
            document.getElementById('deleteModal').classList.add('active');
        }

        document.getElementById('confirmDeleteBtn').addEventListener('click', async () => {
            if (!deletarId) return;
            
            try {
                showLoading(true);
                const response = await fetch(`/api/pedido/${deletarId}`, {
                    method: 'DELETE'
                });
                
                const result = await response.json();
                
                if (result.success) {
                    alert('✅ Pedido excluído com sucesso!');
                    fecharModal('deleteModal');
                    deletarId = null;
                    carregarDados();
                } else {
                    alert('❌ Erro: ' + (result.error || 'Erro ao excluir'));
                }
            } catch (error) {
                alert('❌ Erro: ' + error.message);
            }
            showLoading(false);
        });

        // ============================================================
        //  UTILITÁRIOS
        // ============================================================
        function fecharModal(id) {
            document.getElementById(id).classList.remove('active');
        }

        function showLoading(active) {
            document.getElementById('loadingOverlay').classList.toggle('active', active);
        }

        // Fechar modais clicando fora
        document.querySelectorAll('.modal-overlay').forEach(modal => {
            modal.addEventListener('click', (e) => {
                if (e.target === modal) {
                    modal.classList.remove('active');
                }
            });
        });

        // ============================================================
        //  EXPORTAR CSV
        // ============================================================
        async function exportarCSV() {
            try {
                const response = await fetch('/api/pedidos');
                const pedidos = await response.json();
                
                if (!pedidos || pedidos.length === 0) {
                    alert('📭 Nenhum dado para exportar');
                    return;
                }
                
                const headers = ['ID', 'Cliente', 'Telefone', 'Endereço', 'Total', 'Status', 'Data', 'Produtos'];
                const rows = pedidos.map(p => {
                    let produtosTexto = '';
                    if (p.produtos) {
                        try {
                            const parsed = typeof p.produtos === 'string' ? JSON.parse(p.produtos) : p.produtos;
                            if (Array.isArray(parsed)) {
                                produtosTexto = parsed.map(item => `${item.nome || ''} x${item.quantidade || 1}`).join('; ');
                            }
                        } catch (e) {}
                    }
                    if (!produtosTexto) produtosTexto = '-';
                    
                    return [
                        p.id || '',
                        p.nome_cliente || '',
                        p.telefone || '',
                        p.endereco || '',
                        parseFloat(p.total || 0).toFixed(2),
                        p.status || 'pendente',
                        p.created_at || '',
                        produtosTexto
                    ];
                });
                
                let csv = '\uFEFF' + headers.join(';') + '\n';
                rows.forEach(row => {
                    csv += row.join(';') + '\n';
                });
                
                const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `vaporize_pedidos_${new Date().toISOString().split('T')[0]}.csv`;
                a.click();
                URL.revokeObjectURL(url);
                
            } catch (error) {
                console.error('Erro ao exportar:', error);
                alert('❌ Erro ao exportar dados');
            }
        }

        // ============================================================
        //  INIT
        // ============================================================
        document.addEventListener('DOMContentLoaded', () => {
            document.getElementById('filterPeriod').addEventListener('change', carregarDados);
            document.getElementById('filterStatus').addEventListener('change', carregarDados);
            carregarDados();
            setInterval(carregarDados, 60000);
        });
    </script>

</body>
</html>