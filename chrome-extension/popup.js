const serverURL = 'http://localhost:5000'

function makeXhrPostRequest(targetUrl, requestBody) {
    return new Promise((resolve, reject) => {
        let xhr = new XMLHttpRequest()
        xhr.open('POST', targetUrl, true)
        xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8')
        xhr.onload = function() {
            if (xhr.status >= 200 && xhr.status < 300){
                return resolve(xhr.response);
            } else {
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
        xhr.send(JSON.stringify(requestBody))
    })
}

document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('submit')
    const inputField = document.getElementById('inputField')

    button.addEventListener('click', function(event) {
        var parameters = {
            'input': inputField.value
        }
        makeXhrPostRequest(serverURL + '/responses', parameters)
        .then(data => {
            console.log('response', data)
        })
        .catch(err => console.log('error', err))
    });
})



