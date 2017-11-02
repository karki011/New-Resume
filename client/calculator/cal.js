window.onload = function () {
    var button = document.getElementById('button');
    var clear = document.getElementById('clear');
    var answer = document.getElementById('answer');


    button.addEventListener("click", function (e) {
        if (e.target.nodeName === "LI") {
            // console.log(e.target.innerHTML);
            var v = e.target.innerHTML;
            if (v === "=") {
                try {
                    answer.innerHTML = eval(answer.innerHTML);                
                } catch (error) {
                    answer.innerHTML = error.message;
                }
            }else{
                answer.innerHTML += v;                
            }
        }
    });
    clear.addEventListener('click', function(){
        answer.innerHTML = ''
    });
};