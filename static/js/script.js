document.addEventListener('DOMContentLoaded', () => {
    const empresaButton = document.getElementById('empresaButton');
    const clienteButton = document.getElementById('clienteButton');
    const cadastroEmpresaForm = document.getElementById('cadastroEmpresaForm');
    const cadastroClienteForm = document.getElementById('cadastroClienteForm');

    if (empresaButton) {
        empresaButton.addEventListener('click', () => {
            cadastroEmpresaForm.style.display = 'block';
            cadastroClienteForm.style.display = 'none';
        });
    }

    if (clienteButton) {
        clienteButton.addEventListener('click', () => {
            cadastroEmpresaForm.style.display = 'none';
            cadastroClienteForm.style.display = 'block';
        });
    }

    if (cadastroEmpresaForm) {
        cadastroEmpresaForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const nome = document.getElementById('empresaNome').value;
            const email = document.getElementById('empresaEmail').value;
            const senha = document.getElementById('empresaSenha').value;
            console.log(`Empresa cadastrada: ${nome}, ${email}`);
        });
    }

    if (cadastroClienteForm) {
        cadastroClienteForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const nome = document.getElementById('clienteNome').value;
            const email = document.getElementById('clienteEmail').value;
            const senha = document.getElementById('clienteSenha').value;
            console.log(`Cliente cadastrado: ${nome}, ${email}`);
        });
    }

    const cadastroProdutoForm = document.getElementById('cadastroProdutoForm');
    if (cadastroProdutoForm) {
        cadastroProdutoForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const formData = new FormData();
            formData.append('nome', document.getElementById('produtoNome').value);
            formData.append('tipo', document.getElementById('produtoTipo').value);
            formData.append('validade', document.getElementById('produtoValidade').value);
            formData.append('preco', document.getElementById('produtoPreco').value);
            formData.append('quantidade', document.getElementById('produtoQuantidade').value);
            formData.append('foto', document.getElementById('produtoFoto').files[0]);

            fetch('api/cadastrarProduto', {
                method: 'POST',
                body: formData
            }).then(response => {
                if (response.ok) {
                    alert('Produto cadastrado com sucesso!');
                } else {
                    alert('Falha ao cadastrar produto.');
                }
            }).catch(error => {
                console.error('Erro:', error);
                alert('Erro ao cadastrar produto.');
            });
        });
    }
});









function focusFunc(){
    let parent = this.parentNode.parentNode;
    parent.classList.add('focus');
}

function blurFunc(){
    let parent = this.parentNode.parentNode;
    if(this.value == ""){
        parent.classList.remove('focus');
    }
    
}

const inputs = document.querySelectorAll('.input');

inputs.forEach(input => {
    input.addEventListener('focus', focusFunc);
    input.addEventListener('blur', blurFunc);
});










function redirectToConfirmation(event) {// Impede o envio padrão do formulário

    window.location.href = "cadastro_confirmado.html";
}








let menuList = document.getElementById("nav-links")
menuList.style.maxHeight = "0px";

function toggleMenu(){
    if(menuList.style.maxHeight == "0px")
    {
        menuList.style.maxHeight = "300px";
    }
    else{
        menuList.style.maxHeight = "0px";
    }
}



// rolagem do footer

document.addEventListener('DOMContentLoaded', () => {
    const links = document.querySelectorAll('a[href^="#"]');

    for (const link of links) {
        link.addEventListener('click', function (event) {
            event.preventDefault();

            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            window.scrollTo({
                top: targetElement.offsetTop,
                behavior: 'smooth'
            });
        });
    }
});





const scrollToTopBtn = document.getElementById('scroll-to-top');

scrollToTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth' 
    });
});

window.addEventListener('scroll', () => {
    if (window.scrollY > 200) {
        scrollToTopBtn.classList.add('show');
    } else {
        scrollToTopBtn.classList.remove('show');
    }
});





document.addEventListener('DOMContentLoaded', (event) => {
    const loginButton = document.getElementById('loginButton');
    loginButton.addEventListener('click', (e) => {
        e.preventDefault(); // Evita o comportamento padrão do botão
        window.location.href = 'promocoes_user.html'; // Substitua pelo URL da página de promoções
    });
});