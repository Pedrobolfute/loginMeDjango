class Cardmenu extends HTMLElement {
  constructor() {
    super()

    const shadow = this.attachShadow({ mode: 'open' })
    shadow.appendChild(this.build())
    shadow.appendChild(this.style())
  }

  build() {
    //Welcome message
    const title = document.querySelector('head title').textContent
    console.log(`Bem vindo á ${title}!!`)

    //Aux vars
    const maxElements = 6

    const menuSpan = []
    const menuSpanDiv = []
    const menuSpanDivImg = []
    const menuSpanA = []

    const globalItemsName = []
    const globalItemsImage = []
    const globalItemsSrc = []

    //creating some elements
    const headerRoot = document.createElement('header')
    const headerContainer = document.createElement('div')
    const logo = document.createElement('div')
    const logoImg = document.createElement('img')
    const logoSpan = document.createElement('span')
    const menu = document.createElement('div')

    //setting some properties
    headerContainer.setAttribute('class', 'headerContainer')
    logo.setAttribute('class', 'logo')
    logoImg.src = this.getAttribute('logo') || 'assets/img/cozinharteLogoResized.png' //aki
    logoImg.alt = `${title} logo`

    //treating menu elements
    menu.setAttribute('class', 'menu')
    for (let i = 0; i < maxElements; i++) {
      let itemName = this.getAttribute(`itemName${i}`)
      let itemImage = this.getAttribute(`itemImage${i}`)
      let itemSrc = this.getAttribute(`itemSrc${i}`)

      if (itemName || itemImage || itemSrc) {
        globalItemsName.push(itemName)
        globalItemsImage.push(itemImage)
        globalItemsSrc.push(itemSrc)

        menuSpan[i] = document.createElement('span')
        menuSpanDiv[i] = document.createElement('div')
        menuSpanDivImg[i] = document.createElement('img')
        menuSpanA[i] = document.createElement('a')

        menuSpanA[i].textContent = itemName || `Nome`
        menuSpanDivImg[i].src = itemImage || `assets/img/svg/about.svg` //aki
        menuSpanDivImg[i].alt = itemName || `Nome_Alt`
        menuSpanA[i].href = itemSrc || `https://www.linkedin.com/in/pedrobolfute/`
        menuSpanA[i].setAttribute('target', '_blank')
      }
    }
    headerRoot.appendChild(headerContainer)
    headerContainer.appendChild(logo)
    headerContainer.appendChild(menu)

    logo.appendChild(logoImg)
    logo.appendChild(logoSpan)


    for (let i = 0; i < globalItemsName.length; i++) {
      menu.appendChild(menuSpan[i])
      menuSpan[i].appendChild(menuSpanDiv[i])

      menuSpan[i].appendChild(menuSpanA[i])
      menuSpanDiv[i].appendChild(menuSpanDivImg[i])


    }
    this.trackMatchMedia(logoSpan)
    return headerRoot
  }

  style() {
    const style = document.createElement('style')
    style.textContent = `
    header {
      // position: fixed;
      display: flex;
      justify-content: center;
      align-items: center;
      max-width: 100vw;
      width: 100%;
      height: 8rem;
      background-color: #333;
    }
    
    .headerContainer a {
      text-decoration: none;
      color: black;
    }
    
    .headerContainer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 95%;
      background-color: #e7a61a;
      border-radius: 0.5rem;
    
      -webkit-box-shadow: 10px 10px 5px 0px rgba(0, 0, 0, 0.75);
      -moz-box-shadow: 10px 10px 5px 0px rgba(0, 0, 0, 0.75);
      box-shadow: 10px 10px 5px 0px rgba(0, 0, 0, 0.75);
    }
    
    .headerContainer .logo {
      display: flex;
      align-items: center;
      width: fit-content;
      margin-left: 5px;
    }
    
    .headerContainer .logo img {
      width: 4rem;
      height: 4rem;
    }
    
    .headerContainer .menu {
      display: flex;
      justify-content: space-evenly;
      width: 100%;
      font-size: 1rem;
    }
    
    .headerContainer .menu span {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    
    .headerContainer .menu span:hover {
      cursor: pointer;
      scale: 1.1;
      transition: 0.1s all;
    }
    
    .headerContainer .menu span img {
      width: 1rem;
      height: 1rem;
      animation: menuImgs 2s ease-in-out infinite alternate;
    }
    
    @media screen and (min-width: 576px) {
      .headerContainer .logo img {
        width: 5rem;
        height: 5rem;
      }
    
      .headerContainer .menu {
        font-size: 1.25rem;
      }
    
      .headerContainer .menu span img {
        width: 1.25rem;
        height: 1.25rem;
      }
    
    }
    
    @media screen and (min-width: 768px) {
      .headerContainer .logo img {
        width: 5rem;
        height: 5rem;
      }
    
      .headerContainer .menu {
        font-size: 1.5rem;
      }
    }
    
    @media screen and (min-width: 992px) {
    
      .headerContainer .logo span {
        padding-left: 1rem;
        padding-right: 1rem;
        font-family: 'Open-Sans', 'Helvetica', sans-serif;
        font-weight: 500;
        font-size: 1rem;
        animation: logoImg 1s ease-in;
      }
    
      .headerContainer .logo img {
        width: 6rem;
        height: 6rem;
      }
    
      .headerContainer .menu {
        font-size: 1.5rem;
      }
    }
    
    @media screen and (min-width: 1440px) {
      .headerContainer .logo {
        white-space: nowrap;
      }
    
      .headerContainer .logo span {
        padding-left: 1rem;
        padding-right: 1rem;
        font-family: 'Open-Sans', 'Helvetica', sans-serif;
        font-weight: 500;
        font-size: 1.5rem;
        animation: logoImg 1s ease-in;
      }
    }
    
    @keyframes menuImgs {
      from {
        transform: scale(1.1);
      }
    
      to {
        transform: scale(0.9);
      }
    }
    
    @keyframes logoImg {
      from {
        opacity: 0;
      }
    
      to {
        opacity: 1;
      }
    }
    `

    return style
  }

  trackMatchMedia(element) {
    if (window.matchMedia("(min-width:1440px)").matches) {
      element.textContent = this.getAttribute('message') || `Menssagem curta aqui!`

    } else {
      element.textContent = ''
    }

    window.addEventListener('resize', () => {
      if (window.innerWidth >= 1440) {
        element.textContent = this.getAttribute('message') || `Menssagem curta aqui!`
      } else {
        element.textContent = ''
      }
    })
  }
}
customElements.define('header-simple', Cardmenu)
