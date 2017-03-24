var log = function() {
    console.log.apply(console, arguments)
}

var find = function(sel) {
        return document.querySelector(sel)
    }

var buttonClick = function() {
    var input = find('#id-input-account')
    account = input.value
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if (alphabet.indexOf(account[0]) < 0 || account.length < 2){
        log('用户名错误')
    } else {
        log('检查合格')
    }
}

var button = find('#id-button-login')
button.addEventListener('click', buttonClick)
