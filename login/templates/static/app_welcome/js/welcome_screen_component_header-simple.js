const addAnimal = document.querySelector('.animal.add');
const animalForm = addAnimal.querySelector('.animal-form');
const animalOwner = document.querySelector('#owner')

// Expande o card e exibe o formulário ao clicar no card
addAnimal.addEventListener('click', (e) => {
  e.stopPropagation(); // Evita que o evento se propague para o clique global
  addAnimal.classList.add('expanded');
  animalForm.style.display = 'flex';
});

// Fecha o card se clicar fora ou se o botão de adicionar for clicado
document.addEventListener('click', (e) => {
  if (!addAnimal.contains(e.target)) {
    addAnimal.classList.remove('expanded');
    animalForm.style.display = 'none';
  }
});

// Lógica para o botão de adicionar animal
animalForm.addEventListener('submit', (e) => {
  e.preventDefault(); // Impede o comportamento padrão do formulário
  
  const selectedAnimal = document.querySelector('#animal-select').value;
  const animalColor = document.querySelector('#animal-color').value;
  
  console.log(`Animal: ${selectedAnimal}, Cor: ${animalColor}`);
  
  // Fechar o card após enviar o formulário
  addAnimal.classList.remove('expanded');
  animalForm.style.display = 'none';
  
  // Aqui você pode adicionar lógica para criar um novo card com os dados
});

animalOwner.setAttribute('name', sessionStorage.getItem('owner'))