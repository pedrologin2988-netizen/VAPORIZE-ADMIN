// ============================================================
//  CONFIGURAÇÕES
// ============================================================
let cart = JSON.parse(localStorage.getItem('cart')) || [];
let produtos = [];
let numeroWhatsApp = null;
let produtoSelecionado = null;

// ============================================================
//  API
// ============================================================
async function carregarProdutos() {
    try {
        const response = await fetch('/api/produtos');
        const data = await response.json();
        if (data.error) throw new Error(data.error);
        produtos = data;
        renderizarProdutos();
    } catch (error) {
        console.error('Erro:', error);
        document.getElementById('productGrid').innerHTML = `
            <div style="text-align:center;padding:2rem;color:var(--muted);grid-column:1/-1;">
                <i class="fas fa-exclamation-triangle" style="font-size:2rem;color:var(--primary);"></i>
                <p style="margin-top:1rem;">Erro ao carregar produtos. Tente novamente.</p>
            </div>
        `;
    }
}

async function carregarWhatsApp() {
    try {
        const response = await fetch('/api/whatsapp');
        const data = await response.json();
        if (data.success && data.whatsapp) {
            numeroWhatsApp = data.whatsapp;
            const formatted = formatarWhatsApp(data.whatsapp);
            document.getElementById('contatoWhatsApp').textContent = formatted;
            document.getElementById('footerWhatsApp').textContent = `WhatsApp: ${formatted}`;
        }
    } catch (error) {
        console.error('Erro ao carregar WhatsApp:', error);
    }
}

function formatarWhatsApp(numero) {
    if (numero.length >= 13) {
        return `+${numero.slice(0,2)} (${numero.slice(2,4)}) ${numero.slice(4,9)}-${numero.slice(9)}`;
    }
    return numero;
}

// ============================================================
//  PRODUTOS
// ============================================================
function renderizarProdutos() {
    const grid = document.getElementById('productGrid');
    if (!produtos || produtos.length === 0) {
        grid.innerHTML = `
            <div style="text-align:center;padding:2rem;color:var(--muted);grid-column:1/-1;">
                <p>📭 Nenhum produto disponível no momento</p>
            </div>
        `;
        return;
    }

    grid.innerHTML = produtos.map(prod => {
        const sabores = prod.sabores ? prod.sabores.map(s => `🍃 ${s}`).join(' / ') : 'Sabores diversos';
        return `
            <div class="product-card fade-up" data-id="${prod.id}">
                <div class="product-img">
                    <img src="${prod.imagem || 'https://placehold.co/400x400/1a1a1a/e53935?text=VAPORIZE'}" 
                         alt="${prod.nome}"
                         loading="lazy"
                         onerror="this.src='https://placehold.co/400x400/1a1a1a/e53935?text=VAPORIZE'">
                </div>
                <div class="product-body">
                    <div class="brand">${prod.marca || 'VAPORIZE'}</div>
                    <h3>${prod.nome}</h3>
                    <div class="flavors">${sabores}</div>
                    <div class="product-footer">
                        <span class="product-price">R$ ${Number(prod.preco).toFixed(2)}</span>
                        <button class="btn btn-primary btn-sm add-to-cart" data-id="${prod.id}">
                            <i class="fas fa-plus"></i> Comprar
                        </button>
                    </div>
                </div>
            </div>
        `;
    }).join('');

    // Adicionar eventos aos botões
    document.querySelectorAll('.add-to-cart').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            const id = parseInt(btn.dataset.id);
            abrirModalSabor(id);
        });
    });
}

// ============================================================
//  MODAL DE SABOR
// ============================================================
function abrirModalSabor(produtoId) {
    const prod = produtos.find(p => p.id === produtoId);
    if (!prod) return;
    produtoSelecionado = prod;

    const modal = document.getElementById('flavorModal');
    const container = document.getElementById('flavorOptions');

    if (!prod.sabores || prod.sabores.length === 0) {
        container.innerHTML = `
            <p style="color:var(--muted);text-align:center;margin-bottom:1rem;">Este produto não possui opções de sabor</p>
            <button class="btn btn-primary" onclick="adicionarAoCarrinho(${prod.id}, 'Padrão')">
                <i class="fas fa-plus"></i> Adicionar ao Carrinho
            </button>
        `;
    } else {
        container.innerHTML = `
            <p style="color:var(--muted);margin-bottom:1rem;">Selecione o sabor para <strong>${prod.nome}</strong></p>
            <div style="display:flex;flex-direction:column;gap:0.5rem;">
                ${prod.sabores.map(sabor => `
                    <button class="btn btn-outline" onclick="adicionarAoCarrinho(${prod.id}, '${sabor}')" style="width:100%;justify-content:center;">
                        🍃 ${sabor}
                    </button>
                `).join('')}
            </div>
        `;
    }

    modal.classList.add('active');
}

// ============================================================
//  CARRINHO
// ============================================================
function adicionarAoCarrinho(produtoId, sabor) {
    const prod = produtos.find(p => p.id === produtoId);
    if (!prod) return;

    const existing = cart.find(item => item.id === produtoId && item.sabor === sabor);
    if (existing) {
        existing.quantidade++;
        showNotification(`✅ +1 ${prod.nome} - ${sabor}`);
    } else {
        cart.push({
            id: produtoId,
            nome: prod.nome,
            preco: Number(prod.preco),
            sabor: sabor,
            quantidade: 1
        });
        showNotification(`✅ ${prod.nome} - ${sabor} adicionado!`);
    }

    atualizarCarrinho();
    salvarCarrinho();
    animarBotaoCarrinho();

    // Fechar modal
    document.getElementById('flavorModal').classList.remove('active');
}

function removerDoCarrinho(id, sabor) {
    cart = cart.filter(item => !(item.id === id && item.sabor === sabor));
    atualizarCarrinho();
    salvarCarrinho();
    renderizarCarrinho();
}

function atualizarQuantidade(id, sabor, delta) {
    const item = cart.find(i => i.id === id && i.sabor === sabor);
    if (item) {
        item.quantidade += delta;
        if (item.quantidade <= 0) {
            removerDoCarrinho(id, sabor);
        } else {
            atualizarCarrinho();
            salvarCarrinho();
            renderizarCarrinho();
        }
    }
}

function atualizarCarrinho() {
    const count = cart.reduce((sum, item) => sum + item.quantidade, 0);
    document.getElementById('cartCount').textContent = count;
}

function salvarCarrinho() {
    localStorage.setItem('cart', JSON.stringify(cart));
}

function animarBotaoCarrinho() {
    const btn = document.getElementById('cartBtn');
    btn.style.transform = 'scale(1.2)';
    setTimeout(() => btn.style.transform = '', 300);
}

// ============================================================
//  RENDER CART
// ============================================================
function renderizarCarrinho() {
    const container = document.getElementById('cartItems');
    const totalEl = document.getElementById('cartTotal');

    if (cart.length === 0) {
        container.innerHTML = `
            <div style="text-align:center;color:var(--muted);padding:2rem;">
                <i class="fas fa-shopping-cart" style="font-size:3rem;opacity:0.3;margin-bottom:1rem;display:block;"></i>
                <p>Seu carrinho está vazio</p>
                <small>Adicione produtos clicando em "Comprar"</small>
            </div>
        `;
        totalEl.textContent = 'R$ 0,00';
        return;
    }

    let total = 0;
    container.innerHTML = cart.map(item => {
        const subtotal = item.preco * item.quantidade;
        total += subtotal;
        return `
            <div style="background:#111;border-radius:var(--radius);padding:1rem;margin-bottom:0.75rem;border:1px solid var(--border);">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                    <div>
                        <h4 style="font-family:'Bebas Neue',sans-serif;font-size:1.1rem;">${item.nome}</h4>
                        <p style="color:var(--muted);font-size:0.8rem;">🍃 ${item.sabor}</p>
                        <p style="color:var(--primary);font-weight:bold;">R$ ${item.preco.toFixed(2)}</p>
                    </div>
                    <button onclick="removerDoCarrinho(${item.id}, '${item.sabor}')" 
                            style="background:none;border:none;color:#ff1744;cursor:pointer;font-size:1.2rem;">
                        <i class="fas fa-trash"></i>
                    </button>
                </div>
                <div style="display:flex;align-items:center;gap:0.5rem;margin-top:0.5rem;">
                    <button onclick="atualizarQuantidade(${item.id}, '${item.sabor}', -1)" 
                            style="background:var(--border);border:none;color:#fff;width:30px;height:30px;border-radius:6px;cursor:pointer;">
                        <i class="fas fa-minus"></i>
                    </button>
                    <span style="min-width:30px;text-align:center;">${item.quantidade}</span>
                    <button onclick="atualizarQuantidade(${item.id}, '${item.sabor}', 1)" 
                            style="background:var(--border);border:none;color:#fff;width:30px;height:30px;border-radius:6px;cursor:pointer;">
                        <i class="fas fa-plus"></i>
                    </button>
                </div>
            </div>
        `;
    }).join('');

    totalEl.textContent = `R$ ${total.toFixed(2)}`;
}

// ============================================================
//  FINALIZAR COMPRA
// ============================================================
async function finalizarCompra(dados) {
    if (cart.length === 0) {
        showNotification('Carrinho vazio!');
        return;
    }

    const numero = numeroWhatsApp || '5581995248272';
    const total = cart.reduce((sum, item) => sum + (item.preco * item.quantidade), 0);

    let msg = `VAPORIZE - NOVO PEDIDO\n\n`;
    msg += `Cliente: ${dados.nome}\n`;
    msg += `WhatsApp: ${dados.telefone}\n`;
    msg += `Endereço: ${dados.endereco}\n\n`;
    msg += `ITENS:\n`;
    msg += `----------------------------------------\n`;
    cart.forEach((item, i) => {
        msg += `${i + 1}. ${item.nome}\n`;
        msg += `   Sabor: ${item.sabor}\n`;
        msg += `   Quantidade: ${item.quantidade}\n`;
        msg += `   Valor: R$ ${item.preco.toFixed(2)}\n\n`;
    });
    msg += `----------------------------------------\n`;
    msg += `TOTAL: R$ ${total.toFixed(2)}\n\n`;
    msg += `Pedido confirmado via site VAPORIZE\n`;
    msg += `Data: ${new Date().toLocaleString('pt-BR')}`;

    // Salvar no Supabase
    try {
        await fetch('/api/pedido', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                nome: dados.nome,
                telefone: dados.telefone,
                endereco: dados.endereco,
                total: total,
                itens: cart
            })
        });
    } catch (e) {
        console.error('Erro ao salvar pedido:', e);
    }

    // Abrir WhatsApp
    const link = `https://wa.me/${numero}?text=${encodeURIComponent(msg)}`;
    
    if (/Mobi|Android|iPhone|iPad|iPod/i.test(navigator.userAgent)) {
        window.location.href = link;
    } else {
        window.open(link, '_blank');
    }

    // Limpar carrinho
    cart = [];
    salvarCarrinho();
    atualizarCarrinho();
    renderizarCarrinho();
    document.getElementById('cartSidebar').classList.remove('open');
}

// ============================================================
//  NOTIFICAÇÕES
// ============================================================
function showNotification(msg) {
    const el = document.createElement('div');
    el.style.cssText = `
        position:fixed;bottom:100px;right:30px;background:var(--primary);
        color:#fff;padding:0.75rem 1.5rem;border-radius:var(--radius);
        z-index:999;font-weight:bold;animation:slideIn 0.3s ease;
    `;
    el.textContent = msg;
    document.body.appendChild(el);
    setTimeout(() => {
        el.style.opacity = '0';
        el.style.transition = 'opacity 0.3s';
        setTimeout(() => el.remove(), 300);
    }, 3000);
}

// ============================================================
//  EVENTS
// ============================================================
document.addEventListener('DOMContentLoaded', async () => {
    // Ano no footer
    document.getElementById('year').textContent = new Date().getFullYear();

    // Carregar dados
    await Promise.all([
        carregarProdutos(),
        carregarWhatsApp()
    ]);

    // Atualizar carrinho
    atualizarCarrinho();
    renderizarCarrinho();

    // Mobile menu
    const menuBtn = document.getElementById('menuBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    menuBtn.addEventListener('click', () => mobileMenu.classList.toggle('open'));
    mobileMenu.querySelectorAll('a').forEach(a => {
        a.addEventListener('click', () => mobileMenu.classList.remove('open'));
    });

    // Cart sidebar
    const cartBtn = document.getElementById('cartBtn');
    const cartSidebar = document.getElementById('cartSidebar');
    const closeCartBtn = document.getElementById('closeCartBtn');

    cartBtn.addEventListener('click', () => {
        renderizarCarrinho();
        cartSidebar.classList.add('open');
    });
    closeCartBtn.addEventListener('click', () => cartSidebar.classList.remove('open'));

    // Modal cliente
    const finalizarBtn = document.getElementById('finalizarBtn');
    const clienteModal = document.getElementById('clienteModal');
    const closeClienteBtn = document.getElementById('closeClienteBtn');

    finalizarBtn.addEventListener('click', () => {
        if (cart.length === 0) {
            showNotification('Adicione produtos ao carrinho!');
            return;
        }
        cartSidebar.classList.remove('open');
        clienteModal.classList.add('active');
    });

    closeClienteBtn.addEventListener('click', () => clienteModal.classList.remove('active'));

    // Fechar modal ao clicar fora
    clienteModal.addEventListener('click', (e) => {
        if (e.target === clienteModal) clienteModal.classList.remove('active');
    });

    // Fechar flavor modal
    document.getElementById('closeFlavorBtn').addEventListener('click', () => {
        document.getElementById('flavorModal').classList.remove('active');
    });
    document.getElementById('flavorModal').addEventListener('click', (e) => {
        if (e.target === e.currentTarget) e.currentTarget.classList.remove('active');
    });

    // Form cliente
    document.getElementById('clienteForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const nome = document.getElementById('nome').value;
        const telefone = document.getElementById('telefone').value;
        const endereco = document.getElementById('endereco').value;

        await finalizarCompra({ nome, telefone, endereco });
        document.getElementById('clienteModal').classList.remove('active');
        document.getElementById('clienteForm').reset();
    });

    // Fechar sidebar ao clicar fora
    document.addEventListener('click', (e) => {
        const sidebar = document.getElementById('cartSidebar');
        const btn = document.getElementById('cartBtn');
        if (sidebar.classList.contains('open') && !sidebar.contains(e.target) && !btn.contains(e.target)) {
            sidebar.classList.remove('open');
        }
    });

    console.log('🚀 VAPORIZE pronto!');
});

// ============================================================
//  ANIMAÇÃO DE SCROLL
// ============================================================
const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
        if (e.isIntersecting) {
            e.target.style.opacity = '1';
            e.target.style.transform = 'translateY(0)';
        }
    });
}, { threshold: 0.1 });

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));
});

// ============================================================
//  EXPORTAR FUNÇÕES GLOBAIS
// ============================================================
window.adicionarAoCarrinho = adicionarAoCarrinho;
window.removerDoCarrinho = removerDoCarrinho;
window.atualizarQuantidade = atualizarQuantidade;