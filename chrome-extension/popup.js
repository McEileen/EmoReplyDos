const serverURL = 'http://localhost:5000'

function makeXhrPostRequest(targetUrl, requestBody) {
    return new Promise((resolve, reject) => {
        let xhr = new XMLHttpRequest();
        xhr.open('POST', targetUrl, true)
        xhr.setRequestHeader('Content-Type', 'application/json')
        xhr.onload = function(){
            if (xhr.status >= 200 && xhr.status < 300){
                return resolve(xhr.response);
            } 
            else {
                reject(Error(JSON.stringify({
                    status: xhr.status,
                    statusText: xhr.statusText
                })))
            }
        }
        xhr.onerror = function(){
            reject(Error({
                status: xhr.status,
                statusText: xhr.statusText
            }))
        }
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4) {
                document.getElementById('outputField').innerText = xhr.responseText;
            }
        }
        xhr.send(requestBody)
    })
}



document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('submit');
    const inputField = document.getElementById('inputField');

    button.addEventListener('click', function(event) {
        var parameters = {
            'input': inputField.value
        }
        console.log('a!', parameters)
        makeXhrPostRequest(serverURL + '/responses', parameters)
        .then(data => {
            console.log('look, it worked', data)
        })
        .catch(err => console.log('this is an error', err))


        // var xhr = new XMLHttpRequest();
        // xhr.open('POST', serverURL + '/responses', true);
        // xhr.setRequestHeader('Content-type', 'application/json');
        // xhr.onreadystatechange = function() {
        //     if (xhr.readyState == 4) {
        //         document.getElementById('outputField').innerText = xhr.responseText;
        //     }
        // }
        // xhr.send(parameters)
    });
})



