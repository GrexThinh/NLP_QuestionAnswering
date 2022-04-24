let welcome = document.querySelector('.welcome')
let body = document.querySelector('body')
let header = document.querySelector('header')

function init() {
    setTimeout(() => {
        setTimeout(()=>{welcome.style.opacity = 0;},500);
        welcome.style.display = 'none';

        header.style.display = 'flex';
        header.style.alignItems = 'center';
        header.style.justifyContent = 'center';
        header.style.flexDirection = 'column';
        setTimeout(()=>{header.style.opacity = 1},50);

        body.style.background = 'background: linear-gradient(135deg, #24ff72 10%, #2196f3 100%);';
        body.style.animation = 'none';
    },3000);

}

init();