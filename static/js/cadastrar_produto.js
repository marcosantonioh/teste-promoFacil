document.getElementById('offerForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Coleta os dados do formulário
    const productImage = document.getElementById('productImage').files[0];
    const DescriçãoProduto = document.getElementById('DescriçãoProduto').value;
    const valorAntes = document.getElementById('valorAntes').value;
    const valor = document.getElementById('valor').value;

    // Cria um objeto FormData
    const formData = new FormData();
    formData.append('productImage', productImage);
    formData.append('DescriçãoProduto', DescriçãoProduto);
    formData.append('valorAntes', valorAntes);
    formData.append('valor', valor);

    // Envia os dados do formulário para o servidor (a implementação do servidor não está incluída neste exemplo)
    fetch('/path-to-your-server-endpoint', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert('Oferta publicada com sucesso!');
        // Aqui você pode redirecionar ou atualizar a página, se necessário
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Houve um erro ao publicar a oferta.');
    });
});