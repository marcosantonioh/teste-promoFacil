document.addEventListener('DOMContentLoaded', () => {
    const configForm = document.getElementById('configForm');

    configForm.addEventListener('submit', (e) => {
        e.preventDefault();

        // Obtenha os valores do formulário
        const nome = document.getElementById('nome').value;
        const email = document.getElementById('email').value;
        const senha = document.getElementById('senha').value;
        const nomeNegocio = document.getElementById('nomeNegocio').value;
        const enderecoNegocio = document.getElementById('enderecoNegocio').value;
        const telefoneNegocio = document.getElementById('telefoneNegocio').value;
        const descricaoNegocio = document.getElementById('descricaoNegocio').value;

        // Exemplo de armazenamento local (localStorage) - substitua pelo método de armazenamento apropriado
        localStorage.setItem('nome', nome);
        localStorage.setItem('email', email);
        localStorage.setItem('senha', senha);
        localStorage.setItem('nomeNegocio', nomeNegocio);
        localStorage.setItem('enderecoNegocio', enderecoNegocio);
        localStorage.setItem('telefoneNegocio', telefoneNegocio);
        localStorage.setItem('descricaoNegocio', descricaoNegocio);

        alert('Configurações salvas com sucesso!');
    });

    // Carregar configurações salvas (se houver)
    document.getElementById('nome').value = localStorage.getItem('nome') || '';
    document.getElementById('email').value = localStorage.getItem('email') || '';
    document.getElementById('senha').value = localStorage.getItem('senha') || '';
    document.getElementById('nomeNegocio').value = localStorage.getItem('nomeNegocio') || '';
    document.getElementById('enderecoNegocio').value = localStorage.getItem('enderecoNegocio') || '';
    document.getElementById('telefoneNegocio').value = localStorage.getItem('telefoneNegocio') || '';
    document.getElementById('descricaoNegocio').value = localStorage.getItem('descricaoNegocio') || '';
});














document.addEventListener('DOMContentLoaded', function() {
    const backToPromotions = document.getElementById('backToPromotions');
    const editInfo = document.getElementById('editInfo');
    const newPromotion = document.getElementById('newPromotion');
    const myInfo = document.getElementById('myInfo');
    const currentInfoSection = document.getElementById('currentInfo');
    const editInfoSection = document.getElementById('editInfoSection');
    const newPromotionSection = document.getElementById('newPromotionSection');

    // Redireciona para a página de promoções ao clicar em "Voltar"
    backToPromotions.addEventListener('click', function(e) {
        e.preventDefault();
        window.location.href = 'promocoes.html';
    });

    // Mostra a seção de editar informações ao clicar em "Editar Informações"
    editInfo.addEventListener('click', function(e) {
        e.preventDefault();
        hideAllSections();
        editInfoSection.style.display = 'block';
    });

    // Redireciona para a página de cadastro de promoção ao clicar em "Cadastrar Nova Promoção"
    newPromotion.addEventListener('click', function(e) {
        e.preventDefault();
        window.location.href = 'cadastrar_produto.html'; // Substitua pelo caminho da sua página de cadastro de promoção
    });

    // Mostra a seção de informações atuais ao clicar em "Minhas Informações"
    myInfo.addEventListener('click', function(e) {
        e.preventDefault();
        hideAllSections();
        currentInfoSection.style.display = 'block';
    });

    function hideAllSections() {
        currentInfoSection.style.display = 'none';
        editInfoSection.style.display = 'none';
        newPromotionSection.style.display = 'none';
    }
});
