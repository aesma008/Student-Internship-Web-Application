const form = document.getElementById('form')
const firstname_input = document.getElementById('first_name-input')
const lastname_input = document.getElementById('last_name-input')
const email_input = document.getElementById('email-input')
const password_input = document.getElementById('password1-input')
const repeat_password_input = document.getElementById('password2-input')
const username_input = document.getElementById('username-input')
const university_select = document.getElementById('university-select')
const error_message = document.getElementById('error-message')

form.addEventListener('submit', (e) => {
    let errors = []

    if (firstname_input) {
        errors = getSignupFormErrors(firstname_input.value, lastname_input.value, email_input.value, password_input.value, repeat_password_input.value, username_input.value, university_select.value)
    } else {
        // TODO: ADD THIS FOR LOGIN PAGE
        errors = getLoginFormErrors(email_input.value, password_input.value)
    }
    if (errors.length > 0) {
        e.preventDefault()
        error_message.innerText = errors.join(". ")
    }

})

if (typeof serverErrors !== 'undefined' && Object.keys(serverErrors).length > 0) {
    let errors = [];
    for (const [field, message] of Object.entries(serverErrors)) {
        if (message === 'This password is too common.') {
            password_input.parentElement.classList.add('incorrect');
        }
        const inputElement = document.getElementById(`${field}-input`);
        if (inputElement) {
            inputElement.parentElement.classList.add('incorrect');
        }
        errors.push(message);
    }
    error_message.innerText = errors.join(". ");
}

function getSignupFormErrors(firstname, lastname, email, password, repeatPassword, username, university) {
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
    if (password.length < 8) {
        errors.push('Password must have at least 8 characters')
        password_input.parentElement.classList.add('incorrect')
    }
    if (password !== repeatPassword) {
        errors.push('Password does not match confirm password')
        password_input.parentElement.classList.add('incorrect')
        repeat_password_input.parentElement.classList.add('incorrect')
    }
    if (university === '' || university == null) {
        errors.push('School is required')
        university_select.parentElement.classList.add('incorrect')
    }
    return errors
}

const allInputs = [firstname_input, lastname_input, email_input, username_input, password_input, repeat_password_input, university_select]
allInputs.forEach(input => {
    input.addEventListener('input', () => {
        if (input.parentElement.classList.contains('incorrect')) {
            input.parentElement.classList.remove('incorrect')
            error_message.innerText = ''
        }
    })
})