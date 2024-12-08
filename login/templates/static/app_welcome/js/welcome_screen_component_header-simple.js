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
animalForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const selectedAnimal = document.querySelector('#animal-select').value;
  const animalColor = document.querySelector('#animal-color').value;
  const owner = sessionStorage.getItem('owner');

  try {
    const response = await fetch(animalForm.action, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value, // Certifique-se de incluir o CSRF token
      },
      body: new URLSearchParams({
        animal: selectedAnimal,
        color: animalColor,
        owner: owner,
      }),
    });

    const result = await response.json();
    console.log(result);
  } catch (err) {
    console.error('Erro ao enviar o formulário:', err);
  }
});

