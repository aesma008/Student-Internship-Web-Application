const form = document.getElementById('form')
const firstname_input = document.getElementById('firstname-input')
const lastname_input = document.getElementById('lastname-input')
const email_input = document.getElementById('email-input')
const password_input = document.getElementById('password-input')
const repeat_password_input = document.getElementById('repeat-password-input')
const username_input = document.getElementById('username-input')
const error_message = document.getElementById('error-message')

form.addEventListener('submit', (e) => {
    //e.preventDefault()
    let errors = []

    if (firstname_input) {
        errors = getSignupFormErrors(firstname_input.value, lastname_input.value, email_input.value, password_input.value, repeat_password_input.value, username_input.value)
    } else {
        errors = getLoginFormErrors(email_input.value, password_input.value)
    }
    if (errors.length > 0) {
        e.preventDefault()
        error_message.innerText = errors.join(". ")
    }

})

function getSignupFormErrors(firstname, lastname, email, password, repeatPassword, username) {
    let errors = []
    if (firstname === '' || firstname == null) {
        errors.push('Firstname is required')
        firstname_input.parentElement.classList.add('incorrect')
    }
    if (lastname === '' || lastname == null) {
        errors.push('Lastname is required')
        lastname_input.parentElement.classList.add('incorrect')
    }
    if (email === '' || email == null) {
        errors.push('Email is required')
        email_input.parentElement.classList.add('incorrect')
    }
    if (username === '' || username == null) {
        errors.push('Username is required')
        username_input.parentElement.classList.add('incorrect')
    }
    if (password === '' || password == null) {
        errors.push('Password is required')
        password_input.parentElement.classList.add('incorrect')
    }
    if (repeatPassword === '' || repeatPassword == null) {
        errors.push('Confirm password is required')
        repeat_password_input.parentElement.classList.add('incorrect')
    }
    return errors
}

const allInputs = [firstname_input, lastname_input, email_input, username_input, password_input, repeat_password_input]
allInputs.forEach(input => {
    input.addEventListener('input', () => {
        if (input.parentElement.classList.contains('incorrect')) {
            input.parentElement.classList.remove('incorrect')
            error_message.innerText = ''
        }
    })
})