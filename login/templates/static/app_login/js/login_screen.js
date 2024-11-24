document.querySelector('form').addEventListener('submit', async function(e) {
    e.preventDefault()
    const formData = new FormData(this)
    try{
        const response = await fetch('/login/', {
            method: 'POST',
            body: formData,
        })
        const data = await response.json()
        if(data.status === 'success'){
            window.location.href = '/welcome/'
        } else if(data.status === 'invalid') {
            alert(data.message)
            window.location.href = '/login/'
        }else if(data.status === 'empty'){
            alert(data.message)
        }
    } catch(error){
        alert('Error processing solicitation')
    }
}
)
console.log('login_screen.js')